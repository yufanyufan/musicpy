"""MusicXML Generation Library

Overview:
This library provides a Pythonic way to generate MusicXML files. It defines a
set of classes that correspond to MusicXML elements. These classes utilize
Python's context managers (`with` statements) to facilitate the creation of a
hierarchical structure that mirrors the MusicXML format. The library also
integrates schema validation using `lxml`, ensuring that the generated XML
conforms to the MusicXML standard. It dynamically creates and uses schemas for
individual MusicXML elements, validating them as they are constructed. The final
output is an XML string representing the musical score.

Key Concepts:
- Context Managers: The library heavily relies on context managers. Entering a
  `with` block for a MusicXML element class (e.g., `ScorePartwise`, `Part`,
  `Measure`) creates the corresponding XML element and sets it as the current
  active context. Exiting the block finalizes the element and triggers schema
  validation for that element.
- Hierarchical Structure: Elements are nested by entering their respective
  context manager blocks within an outer element's block. For example, a
  `Measure` is created within a `Part`, and a `Note` within a `Measure`.
- Global Context (`_current_context`): A global variable, `_current_context`,
  is used internally to keep track of the current parent element in the XML
  hierarchy. When a new MusicXML element object is instantiated, it typically
  appends its XML representation to the XML element of the `_current_context`.
  Upon entering a `with` block, the new object becomes the `_current_context`,
  and upon exiting, the `_current_context` is restored.
- XML Generation: The library uses `xml.etree.ElementTree` to build the XML
  document in memory. The `ScorePartwise` class, as the root context, is
  responsible for serializing the entire structure into an XML string upon
  exiting its context manager.
- Schema Validation: The library uses `lxml` for schema validation. It loads a
  local copy of the MusicXML schema (`musicxml.xsd` and related files like
  `xml.xsd`, `xlink.xsd`) using a custom resolver (`LocalSchemaResolver`).
  For each MusicXML element class, a specific schema is dynamically created
  (if not already cached) using `create_schema`. The `_validate_xml_subtree`
  method in `MusicElementBase` validates the element's generated XML against
  this schema when its context manager is exited.
- Auto-Aliasing: A metaclass `AutoAlias` is used to automatically create
  alias classes, potentially for different naming conventions or shorthand.
- Argument Handling: The `MusicElementArg` dataclass and `_` helper function
  are used for more flexible argument passing to element constructors.

Basic Usage Example:
```python
from musicxml import _

with ScorePartwise(version="4.0") as score:
    Work(WorkTitle="My First Song")
    with PartList():
        with Defaults():
            Scaling(Millimeters="7.2", Tenths="40")
            with PageLayout(PageHeight="1200", PageWidth="900"):
                PageMargins(type="both", LeftMargin="70", RightMargin="70",
                            TopMargin="70", BottomMargin="70")
            MusicFont(font_family="Arial", font_size="20.5")
        ScorePart(id="P1", PartName="Piano")
    with Part(id="P1"):
        with Measure(number="1"):
            Attributes(
                Divisions="1",
                Key=_(Fifths="0"),
                Time=_(Beats="4", BeatType="4"),
                Clef=_(Sign="G", Line="2")
            )
            with Note(Pitch=_(Step="C", Octave="4"), Duration="4"):
                Lyric(number="1", Text="Hel-", Syllabic="begin")
            with Note(Pitch=_(Step="D", Octave="4"), Duration="4"):
                Lyric(number="1", Text="lo", Syllabic="end")
print(score)
```

This example creates a simple score with one part (Piano), one measure,
and two notes with lyrics. The output will be a MusicXML string.
"""

import dataclasses
import inspect
import logging
import os
import sys
import traceback
from typing import Any
import xml.etree.ElementTree as ET
from lxml import etree

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s() -"
        " %(message)s"
    ),
)


# Global context for building the XML tree
_current_context = None


class MusicPy:

  def __init__(self):
    global _current_context
    _current_context = self

  def add_child(self, child):
    self.child = child

  def get_xml(self):
    return str(self.child)

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    pass


# Global variables for schema, parser, and schema details.
_MUSICXML_GLOBAL_SCHEMA_PARSER = None
_MUSICXML_SCHEMA_FILE_NAME = "musicxml.xsd"


def get_xml():
  return _current_context.get_xml()


@dataclasses.dataclass(frozen=True)
class MusicElementArg:
  args: tuple[Any, ...]
  kwargs: dict[str, Any]


def _(*args, **kwargs):
  return MusicElementArg(args, kwargs)


# Define LocalSchemaResolver before its use in _ensure_schema_loaded
class LocalSchemaResolver(etree.Resolver):
  """A custom lxml resolver to load specific schema files from local paths

  instead of their online URLs.
  """

  def __init__(self, local_mapping):
    # local_mapping is a dictionary e.g.:
    # {"http://www.musicxml.org/xsd/xml.xsd": "xml.xsd"}
    self.local_mapping = local_mapping

  def resolve(self, system_url, public_id, context):
    local_path = self.local_mapping.get(system_url)
    if local_path:
      if os.path.exists(local_path):
        return self.resolve_filename(local_path, context)
      else:
        logging.warning(
            f"Local schema file '{local_path}' for URL '{system_url}'"
            " not found."
        )
    return None


def to_kebab_case(name: str, namespace: str = "") -> str:
  """Converts a PascalCase or CamelCase string to snake_case.

  Args:
    name: The input string.

  Returns:
    The snake_case version of the input string.
  """
  if not name:
    return ""
  result = [name[0].lower()]

  for char in name[1:]:
    if char.isupper():
      result.append("-")
    result.append(char.lower())
  result = "".join(result)
  if namespace:
    return  f"{namespace}:{result}"
  return result


def to_pascal_case(snake_str: str) -> str:
  """Converts a snake_case string to PascalCase."""
  return "".join(word.capitalize() for word in snake_str.split("_"))


def loaded_musicxml_schema():
  """Loads the MusicXML schema if not already loaded. Uses global variables."""
  global _MUSICXML_GLOBAL_SCHEMA_PARSER
  local_files_map = {
      "http://www.musicxml.org/xsd/xml.xsd": "xml.xsd",
      "http://www.musicxml.org/xsd/xlink.xsd": "xlink.xsd",
  }
  custom_resolver = LocalSchemaResolver(local_files_map)
  _MUSICXML_GLOBAL_SCHEMA_PARSER = etree.XMLParser(
      resolve_entities=False, load_dtd=False
  )
  _MUSICXML_GLOBAL_SCHEMA_PARSER.resolvers.add(custom_resolver)


loaded_musicxml_schema()


def create_schema(element_name: str) -> etree.XMLSchema:
  element = (
      ""
      if element_name in ("score-partwise", "score-timewise")
      else f' <xs:element name="{element_name}" type="{element_name}"/>'
  )

  wrapper_schema_str = f"""
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
          elementFormDefault="qualified">
  <xs:include schemaLocation="musicxml.xsd"/>
  {element}
</xs:schema>
"""
  wrapper_schema_doc_lxml = etree.fromstring(
      wrapper_schema_str.encode("utf-8"), parser=_MUSICXML_GLOBAL_SCHEMA_PARSER
  )
  return etree.XMLSchema(wrapper_schema_doc_lxml)


class AutoAlias(type):

  def __new__(mcs, name, bases, dct):
    if name == "MusicElementBase":
      return super().__new__(mcs, name, bases, dct)
    for attr_name, value in dct.items():
      if (
          isinstance(value, type(MusicElementBase))
          and attr_name != value.__name__
      ):
        dct[attr_name] = type(
            attr_name,  # Name of the new class
            (value,),  # Tuple of base classes
            {},  # Dictionary of attributes/methods
        )
      elif value is _:
        dct[attr_name] = to_kebab_case(attr_name)
    return super().__new__(mcs, name, bases, dct)

  def __setattr__(cls, name, value):
    if isinstance(value, type(MusicElementBase)) and name != value.__name__:
      value = type(
          name, (value,), {}  # Name of the new class  # Tuple of base classes
      )
    super().__setattr__(name, value)


class MusicElementBase(metaclass=AutoAlias):
  """A base class for MusicXML elements to handle common context management."""

  schema = None
  element: ET.Element

  def __init__(self, *args, **kwargs):
    self.element = ET.Element(to_kebab_case(self.__class__.__name__))
    global _current_context
    previous_context = _current_context
    _current_context = self
    for k, v_args in kwargs.items():
      if v_args is None:
        continue
      if k == "plain_text":
        self.element.text = str(v_args)
        continue
      if k == k.lower():
        namespace = getattr(self.__class__, k, "")
        self.element.set(to_kebab_case(k, namespace), str(v_args))
        continue
      # Try to get the class from the musicxml_schema module first
      music_schema_module = sys.modules.get("musicpy_schema")
      child_class_type = getattr(self.__class__, k, None)
      if child_class_type is None:
        for base_class in inspect.getmro(self.__class__):
          child_class_type = getattr(base_class, k, None)
          if child_class_type is not None:
            break
      if child_class_type is None:
        child_class_type = getattr(music_schema_module, k, None)
      if isinstance(v_args, MusicElementBase):
        raise ValueError("use _() instead.")
      elif child_class_type and issubclass(child_class_type, MusicElementBase):
        self.create_child(child_class_type, v_args)
      else:
        raise ValueError(f"No class found for {k}")
    _current_context = previous_context
    if _current_context:
      _current_context.add_child(self)

  def init(self, **kwargs):
    caller_frame = inspect.currentframe().f_back
    MusicElementBase.__init__(**caller_frame.f_locals)

  def __enter__(self):
    global _current_context
    self.previous_context = _current_context  # For XML context management
    _current_context = self

    # For injecting class-level MusicElementBase instances into caller's locals
    self._added_to_caller_locals = {}
    caller_frame = inspect.currentframe().f_back

    for cls in inspect.getmro(self.__class__):
      for name, attr_value in cls.__dict__.items():
        if inspect.isclass(attr_value) and issubclass(
            attr_value, MusicElementBase
        ):
          if name not in caller_frame.f_locals:
            caller_frame.f_locals[name] = attr_value  # Inject the class (type)
            self._added_to_caller_locals[name] = attr_value
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    global _current_context

    # Restore caller's locals
    caller_frame = inspect.currentframe().f_back
    if hasattr(self, "_added_to_caller_locals"):
      for name, original_value in self._added_to_caller_locals.items():
        if (
            name in caller_frame.f_locals
            and caller_frame.f_locals[name] is original_value
        ):
          del caller_frame.f_locals[name]
      del self._added_to_caller_locals  # Clean up

    # Restore XML context
    _current_context = self.previous_context

    self._validate_xml_subtree(allow_missing_elements=False)

    if not _current_context:
      print(self)
    return False  # Propagate exceptions

  def add_child(self, child: "MusicElementBase"):
    self.element.append(child.element)

  def create_child(self, child_class: type["MusicElementBase"], arg: Any):
    if arg is None:
      return
    if isinstance(arg, MusicElementArg):
      child_class(*arg.args, **arg.kwargs)
    elif isinstance(arg, tuple):
      child_class(*arg)
    elif isinstance(arg, dict):
      child_class(**arg)
    else:
      child_class(arg)

  def sort(self):
    pass

  def __str__(self):
    ET.indent(self.element)
    return ET.tostring(self.element, encoding="unicode")

  def _validate_xml_subtree(self, allow_missing_elements=True):
    if self.__class__.schema is None:
      try:
        self.__class__.schema = create_schema(
            to_kebab_case(self.__class__.__name__)
        )
      except Exception as e:
        logging.warning(
            f"Failed to create schema for {self.__class__.__name__}: {e}"
        )
        return True
    try:
      ET.indent(self.element)
      xml_string_for_validation = ET.tostring(self.element, encoding="unicode")
      instance_parser = etree.XMLParser(resolve_entities=True, load_dtd=False)
      lxml_tree_for_validation = etree.fromstring(
          xml_string_for_validation.encode("utf-8"), parser=instance_parser
      )
      self.schema.assertValid(lxml_tree_for_validation)
      logging.info(f"Validated {self.element.tag}")
      return True
    except etree.DocumentInvalid as e:
      stack = traceback.extract_stack()
      # stack[-1] is this current method (_validate_xml_subtree)
      # stack[-2] is the caller of _validate_xml_subtree
      relevant_frame = stack[-3] if len(stack) > 2 else None
      caller_info = "Unknown location"
      if relevant_frame:
        filename = os.path.basename(relevant_frame.filename)
        caller_info = f"{filename}:{relevant_frame.lineno}"
      if allow_missing_elements and "Missing" in str(e):
        return True
      logging.info(
          f"{caller_info}: Schema Validation Error for {self.element.tag}: {e}"
      )
      lineno = 0
      for line in xml_string_for_validation.splitlines():
        lineno += 1
        if lineno < e.error_log[0].line - 3 or lineno > e.error_log[0].line + 3:
          continue
        logging.info(f"{lineno} {line}")
      return False
