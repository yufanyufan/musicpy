import os
import traceback
from typing import Any, Literal
import xml.etree.ElementTree as ET
from lxml import etree

# Global context for building the XML tree
_current_context = None

# Global variables for schema, parser, and schema details.
_MUSICXML_GLOBAL_SCHEMA = None
_MUSICXML_GLOBAL_SCHEMA_PARSER = None
_MUSICXML_SCHEMA_FILE_NAME = "musicxml.xsd"


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
      # Check if the mapped local file actually exists
      # Assumes local_path is relative to the current working directory
      # or an absolute path.
      if os.path.exists(local_path):
        return self.resolve_filename(local_path, context)
      else:
        print(
            f"Warning: Local schema file '{local_path}' for URL '{system_url}'"
            " not found."
        )
    return None


def loaded_musicxml_schema():
  """Loads the MusicXML schema if not already loaded. Uses global variables."""
  global _MUSICXML_GLOBAL_SCHEMA, _MUSICXML_GLOBAL_SCHEMA_PARSER, _MUSICXML_SCHEMA_FILE_NAME
  if _MUSICXML_GLOBAL_SCHEMA and _MUSICXML_GLOBAL_SCHEMA_PARSER:
    return
  local_files_map = {
      "http://www.musicxml.org/xsd/xml.xsd": "xml.xsd",
      "http://www.musicxml.org/xsd/xlink.xsd": "xlink.xsd",
  }
  custom_resolver = LocalSchemaResolver(local_files_map)
  # This parser is for loading the schema itself
  _MUSICXML_GLOBAL_SCHEMA_PARSER = etree.XMLParser(
      resolve_entities=False, load_dtd=False
  )
  _MUSICXML_GLOBAL_SCHEMA_PARSER.resolvers.add(custom_resolver)
  try:
    schema_doc = etree.parse(
        _MUSICXML_SCHEMA_FILE_NAME, parser=_MUSICXML_GLOBAL_SCHEMA_PARSER
    )
    if schema_doc is None:
      # This case is unlikely as etree.parse usually raises an exception on failure
      raise etree.XMLSyntaxError("Failed to parse schema document.", 0, 0, 0)

    _MUSICXML_GLOBAL_SCHEMA = etree.XMLSchema(schema_doc)
  except Exception as e:
    print(
        f"CRITICAL: Failed to load or parse MusicXML schema: {e}. "
        "Validation will be skipped."
    )
    _MUSICXML_GLOBAL_SCHEMA = None  # Explicitly set to None on failure


# Load the schema when the module is imported.
loaded_musicxml_schema()


def create_schema(element_name):
  wrapper_schema_str = f"""
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
          elementFormDefault="qualified">
  <xs:include schemaLocation="musicxml.xsd"/>
  <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="xml.xsd"/>

  <xs:element name="{element_name}"/>
</xs:schema>
"""
  wrapper_schema_doc_lxml = etree.fromstring(
      wrapper_schema_str.encode("utf-8"), parser=_MUSICXML_GLOBAL_SCHEMA_PARSER
  )
  return etree.XMLSchema(wrapper_schema_doc_lxml)


class MusicElementBase:
  """A base class for MusicXML elements to handle common context management."""

  schema = None
  element: ET.Element

  def __enter__(self):
    global _current_context
    self.previous_context = _current_context
    _current_context = self
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    global _current_context
    _current_context = self.previous_context
    self._validate_xml_subtree(self.element, allow_missing_elements=False)
    return False  # Propagate exceptions

  def add_child(self, child: "MusicElementBase", parent: "MusicElementBase" = None):
    if parent and not isinstance(parent, MusicElementBase):
      return
    self.element.append(child.element)
    self.sort()
    self._validate_xml_subtree(self.element)

  def sort(self):
    pass

  def _validate_xml_subtree(
      self, element_et_to_validate: ET.Element, allow_missing_elements=True
  ):
    if self.schema is None:
      return
    try:
      xml_string_for_validation = ET.tostring(
          element_et_to_validate, encoding="unicode"
      )
      instance_parser = etree.XMLParser(resolve_entities=False, load_dtd=False)
      lxml_tree_for_validation = etree.fromstring(
          xml_string_for_validation.encode("utf-8"), parser=instance_parser
      )
      self.schema.assertValid(lxml_tree_for_validation)
    except etree.DocumentInvalid as e:
      stack = traceback.extract_stack()
      # stack[-1] is this current method (_validate_xml_subtree)
      # stack[-2] is the caller of _validate_xml_subtree
      relevant_frame = stack[-3] if len(stack) >= 2 else None
      caller_info = "Unknown location"
      if relevant_frame:
        filename = os.path.basename(relevant_frame.filename)
        caller_info = f"{filename}:{relevant_frame.lineno}"
      if allow_missing_elements and str(e).find("Missing element"):
        return
      print(
          f"{caller_info}: Schema Validation Error for "
          f"{element_et_to_validate.tag}: {e}"
      )


class Pitch(MusicElementBase):
  schema = create_schema("pitch")

  def __init__(self, step_text=None, octave_text=None, alter_text=None):
    self.element = ET.Element("pitch")

    if step_text:
      step = ET.SubElement(self.element, "step")
      step.text = str(step_text)
    if alter_text:  # For sharps, flats, etc. e.g., 1 for sharp, -1 for flat
      alter = ET.SubElement(self.element, "alter")
      alter.text = str(alter_text)
    if octave_text:
      octave = ET.SubElement(self.element, "octave")
      octave.text = str(octave_text)

    _current_context.add_child(self, Note)


class ScorePartwise(MusicElementBase):
  schema = _MUSICXML_GLOBAL_SCHEMA

  def __init__(self):
    self.element = ET.Element("score-partwise")
    # Validation will occur when children are added.

  def __str__(self):
    xml_declaration = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    doctype_declaration = (
        '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0'
        ' Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\n'
    )
    score_xml = ET.tostring(self.element, encoding="unicode")
    return xml_declaration + doctype_declaration + score_xml


class Part(MusicElementBase):
  schema = create_schema("part")

  def __init__(self, id):
    self.element = ET.Element("part")
    self.element.set("id", id)
    _current_context.add_child(self)


class Measure(MusicElementBase):
  schema = create_schema("measure")

  def __init__(self, number):
    self.element = ET.Element("measure")
    self.element.set("number", str(number))
    _current_context.add_child(self)


class Attributes(MusicElementBase):
  schema = create_schema("attributes")

  def __init__(
      self,
      divisions=None,
      key_fifths=None,
      time_beats=None,
      time_beat_type=None,
      clef_sign=None,
      clef_line=None,
  ):
    self.element = ET.Element("attributes")
    if divisions is not None:
      divisions_el = ET.Element("divisions")
      divisions_el.text = str(divisions)
      self.element.append(divisions_el)

    if key_fifths is not None:
      key_el = ET.Element("key")
      fifths_el = ET.Element("fifths")
      fifths_el.text = str(key_fifths)
      key_el.append(fifths_el)  # Appending to a detached element is fine
      self.element.append(key_el)

    if time_beats is not None and time_beat_type is not None:
      time_el = ET.Element("time")
      beats_el = ET.Element("beats")
      beats_el.text = str(time_beats)
      time_el.append(beats_el)
      beat_type_el = ET.Element("beat-type")
      beat_type_el.text = str(time_beat_type)
      time_el.append(beat_type_el)
      self.element.append(time_el)

    if clef_sign is not None and clef_line is not None:
      clef_el = ET.Element("clef")
      sign_el = ET.Element("sign")
      sign_el.text = clef_sign
      clef_el.append(sign_el)
      line_el = ET.Element("line")
      line_el.text = str(clef_line)
      clef_el.append(line_el)
      self.element.append(clef_el)
    _current_context.add_child(self)


class Note(MusicElementBase):
  schema = create_schema("note")
  NOTE_ELEMENT_ORDER = [  # Order based on MusicXML 4.0 schema for <note>
      "grace",
      "cue",
      "chord",  # Indicates note is part of a chord
      "pitch",
      "unpitched",
      "rest",
      "duration",
      "tie",  # Can be multiple
      "instrument",
      "voice",
      "type",  # Note type (e.g., quarter, half)
      "dot",  # Can be multiple
      "accidental",
      "time-modification",  # For tuplets, etc.
      "stem",
      "notehead",
      "notehead-text",
      "staff",  # Staff number
      "beam",  # Can be multiple
      "notations",  # Can be multiple (e.g., slurs, articulations)
      "lyric",  # Can be multiple
      "play",  # Playback information
      "listen",  # Listening information
  ]

  def __init__(self, pitch=None, rest=None, duration=None, lyric=None):
    self.element = ET.Element("note")
    # Ensure _current_context is set for potential children like Pitch
    # that might be instantiated and then passed in.
    # Handle pitch input (can be Pitch object or tuple)
    if isinstance(pitch, Pitch):
      self.element.append(pitch.element)  # pitch is a Pitch object
    elif pitch is not None:  # Assumed to be a tuple like ("C", 4)
      _pitch_el = ET.Element("pitch")
      step = ET.SubElement(_pitch_el, "step")
      step.text = pitch[0]
      octave = ET.SubElement(_pitch_el, "octave")
      octave.text = str(pitch[1])
      self.element.append(_pitch_el)
    elif rest is not None:
      if isinstance(rest, Rest):
        self.element.append(rest.element)
      elif isinstance(rest, dict):  # e.g. {'measure': 'yes'}
        rest_obj = Rest(**rest)
        self.element.append(rest_obj.element)
      elif rest is True:  # Simple rest, no specific attributes
        rest_obj = Rest()
        self.element.append(rest_obj.element)

    if duration:
      duration_element = ET.Element("duration")
      duration_element.text = str(duration)
      self.element.append(duration_element)
    if lyric:  # Added to handle direct lyric argument
      if isinstance(lyric, Lyric):
        self.element.append(lyric.element)  # Direct append of Lyric's element

    _current_context.add_child(self)

  def sort(self):
    """Sorts the child elements of this note according to MusicXML schema order."""
    if not list(self.element):  # No children to sort
      return

    # Create a dictionary for quick order lookup
    order_map = {name: i for i, name in enumerate(self.NOTE_ELEMENT_ORDER)}

    def sort_key(element):
      # Get the order index, default to a large number for unknown elements
      # so they are placed at the end (preserving their relative order).
      return order_map.get(element.tag, len(self.NOTE_ELEMENT_ORDER))

    children = sorted(list(self.element), key=sort_key)

    # Remove all current children
    for child_element in list(self.element):
      self.element.remove(child_element)

    # Add sorted children back
    for child_element in children:
      self.element.append(child_element)

    self._validate_xml_subtree(self.element)


class Work(MusicElementBase):
  schema = create_schema("work")

  def __init__(self, work_title=None):
    self.element = ET.Element("work")
    if work_title:
      work_title_el = ET.Element("work-title")
      work_title_el.text = work_title
      self.element.append(work_title_el)  # Add to self.element
    _current_context.add_child(self)


class MovementTitle(MusicElementBase):
  schema = create_schema("movement-title")

  def __init__(self, title_text=None):
    self.element = ET.Element("movement-title")
    if title_text:
      self.element.text = title_text  # Direct text content, no child element
    _current_context.add_child(self)


class Identification(MusicElementBase):
  schema = create_schema("identification")

  def __init__(
      self,
      creator_text=None,
      creator_type=None,
      rights_text=None,
      rights_type=None,
      software_name=None,
  ):
    self.element = ET.Element("identification")
    if creator_text:
      creator_element = ET.Element("creator")
      creator_element.text = creator_text
      if creator_type:
        creator_element.set("type", creator_type)
      self.element.append(creator_element)

    if rights_text:
      rights_element = ET.Element("rights")
      rights_element.text = rights_text
      if rights_type:
        rights_element.set("type", rights_type)
      self.element.append(rights_element)

    if software_name:
      encoding_element = ET.Element("encoding")
      software_element = ET.Element("software")
      software_element.text = software_name
      encoding_element.append(software_element)
      self.element.append(encoding_element)
    _current_context.add_child(self)


class Credit(MusicElementBase):
  schema = create_schema("credit")

  def __init__(self, credit_words_text=None, **credit_words_kwargs):
    self.element = ET.Element("credit")
    if credit_words_text:
      credit_words_element = ET.Element("credit-words")
      credit_words_element.text = credit_words_text
      for key, value in credit_words_kwargs.items():
        credit_words_element.set(key.replace("_", "-"), str(value))
      self.element.append(credit_words_element)

    _current_context.add_child(self)


class PartList(MusicElementBase):
  schema = create_schema("part-list")

  def __init__(self):
    self.element = ET.Element("part-list")
    _current_context.add_child(self)


class ScorePart(MusicElementBase):
  schema = create_schema("score-part")

  def __init__(self, id, part_name=None):
    self.element = ET.Element("score-part")
    self.element.set("id", id)

    if part_name:
      part_name_el = ET.Element("part-name")
      part_name_el.text = part_name
      self.element.append(part_name_el)
    _current_context.add_child(self)


class Rest(MusicElementBase):
  schema = create_schema("rest")

  def __init__(self, measure=None, display_step=None, display_octave=None):
    self.element = ET.Element("rest")
    if measure:  # 'yes' or 'no'
      self.element.set("measure", measure)

    if display_step and display_octave:
      ds_el = ET.SubElement(self.element, "display-step")
      ds_el.text = display_step
      do_el = ET.SubElement(self.element, "display-octave")
      do_el.text = str(display_octave)
    # This element is primarily constructed and passed to Note's constructor
    # or added if Note becomes a context manager for it.
    # For now, it's mainly a data carrier for Note.


class Notations(MusicElementBase):
  schema = create_schema("notations")

  def __init__(self, print_object=None, id=None):
    self.element = ET.Element("notations")
    if print_object:
      self.element.set("print-object", print_object)
    if id:
      self.element.set("id", id)

    _current_context.add_child(self)


class Slur(MusicElementBase):
  schema = create_schema("slur")

  def __init__(self, type, number=None, placement=None, **kwargs):
    self.element = ET.Element("slur")
    self.element.set("type", type)  # "start", "stop", "continue"
    if number:
      self.element.set("number", str(number))
    if placement:
      self.element.set("placement", placement)  # "above", "below"

    for key, value in kwargs.items():
      if value is not None:
        attr_name = key.replace("_", "-")
        self.element.set(attr_name, str(value))
    _current_context.add_child(self)


class Defaults(MusicElementBase):
  schema = create_schema("defaults")

  def __init__(self):
    self.element = ET.Element("defaults")
    # The comment below is no longer fully accurate as add_child will validate.
    # No immediate validation, children will trigger it or ScorePartwise exit.
    _current_context.add_child(self)


class Scaling(MusicElementBase):
  schema = create_schema("scaling")

  def __init__(self, millimeters=None, tenths=None):
    self.element = ET.Element("scaling")
    if millimeters is not None:
      mm_el = ET.Element("millimeters")
      mm_el.text = str(millimeters)
      self.element.append(mm_el)
    if tenths is not None:
      tenths_el = ET.Element("tenths")
      tenths_el.text = str(tenths)
      self.element.append(tenths_el)
    _current_context.add_child(self)


class Tied(MusicElementBase):  # For visual ties <tied>
  schema = create_schema("tied")

  def __init__(self, type, **kwargs):
    self.element = ET.Element("tied")
    self.element.set("type", type)  # "start", "stop", "continue", "let-ring"

    # Attributes like: number, line_type, dashed_formatting, position,
    # placement, orientation, bezier, color, optional_unique_id
    for key, value in kwargs.items():
      if value is not None:
        attr_name = key.replace("_", "-")
        self.element.set(attr_name, str(value))
    _current_context.add_child(self)


class Fermata(MusicElementBase):
  schema = create_schema("fermata")

  def __init__(self, shape=None, type=None, **kwargs):
    self.element = ET.Element("fermata")
    if shape:  # An empty string for shape is equivalent to "normal"
      self.element.text = shape
    if type:  # "upright" or "inverted"
      self.element.set("type", type)

    # Handle print-style attributes (default_x, default_y, color, etc.)
    # and optional-unique-id (id)
    for key, value in kwargs.items():
      if value is not None:
        attr_name = key.replace("_", "-")
        self.element.set(attr_name, str(value))
    _current_context.add_child(self)


class PageLayout(MusicElementBase):
  schema = create_schema("page-layout")

  def __init__(self, page_height=None, page_width=None):
    self.element = ET.Element("page-layout")
    if page_height is not None:
      ph_el = ET.Element("page-height")
      ph_el.text = str(page_height)
      self.element.append(ph_el)
    if page_width is not None:
      pw_el = ET.Element("page-width")
      pw_el.text = str(page_width)
      self.element.append(pw_el)
    _current_context.add_child(self)


class PageMargins(MusicElementBase):
  schema = create_schema("page-margins")

  def __init__(
      self,
      type=None,
      left_margin=None,
      right_margin=None,
      top_margin=None,
      bottom_margin=None,
  ):
    self.element = ET.Element("page-margins")
    if type:
      self.element.set("type", type)
    if left_margin is not None:
      lm_el = ET.Element("left-margin")
      lm_el.text = str(left_margin)
      self.element.append(lm_el)
    if right_margin is not None:
      rm_el = ET.Element("right-margin")
      rm_el.text = str(right_margin)
      self.element.append(rm_el)
    if top_margin is not None:
      tm_el = ET.Element("top-margin")
      tm_el.text = str(top_margin)
      self.element.append(tm_el)
    if bottom_margin is not None:
      bm_el = ET.Element("bottom-margin")
      bm_el.text = str(bottom_margin)
      self.element.append(bm_el)
    _current_context.add_child(self)


class SystemMargins:
  """Data container for system margin values."""

  def __init__(self, left_margin=None, right_margin=None):
    self.left_margin = left_margin
    self.right_margin = right_margin


class SystemLayout(MusicElementBase):
  schema = create_schema("system-layout")

  def __init__(
      self,
      system_distance=None,
      top_system_distance=None,
      margins: SystemMargins = None,
  ):
    self.element = ET.Element("system-layout")
    if margins and (
        margins.left_margin is not None or margins.right_margin is not None
    ):
      system_margins_el = ET.Element("system-margins")
      if margins.left_margin is not None:
        lm_el = ET.SubElement(system_margins_el, "left-margin")
        lm_el.text = str(margins.left_margin)
      if margins.right_margin is not None:
        rm_el = ET.SubElement(system_margins_el, "right-margin")
        rm_el.text = str(margins.right_margin)
      self.element.append(system_margins_el)
    if system_distance is not None:
      sd_el = ET.Element("system-distance")
      sd_el.text = str(system_distance)
      self.element.append(sd_el)
    if top_system_distance is not None:
      tsd_el = ET.Element("top-system-distance")
      tsd_el.text = str(top_system_distance)
      self.element.append(tsd_el)
    _current_context.add_child(self)


class StaffLayout(MusicElementBase):
  schema = create_schema("staff-layout")

  def __init__(self, staff_distance=None, number=None):
    self.element = ET.Element("staff-layout")
    if number is not None:
      self.element.set("number", str(number))
    if staff_distance is not None:
      sd_el = ET.Element("staff-distance")
      sd_el.text = str(staff_distance)
      self.element.append(sd_el)
    _current_context.add_child(self)


class Appearance(MusicElementBase):
  schema = create_schema("appearance")

  def __init__(self):
    self.element = ET.Element("appearance")
    # The comment below is no longer fully accurate as add_child will validate.
    # No immediate validation, children will trigger it or on exit.
    _current_context.add_child(self)


class MusicFont(MusicElementBase):
  schema = create_schema("music-font")

  def __init__(
      self, font_family=None, font_style=None, font_size=None, font_weight=None
  ):
    self.element = ET.Element("music-font")
    if font_family:
      self.element.set("font-family", font_family)
    if font_style:
      self.element.set("font-style", font_style)
    if font_size:
      self.element.set("font-size", str(font_size))
    if font_weight:
      self.element.set("font-weight", font_weight)
    _current_context.add_child(self)


class WordFont(MusicElementBase):
  schema = create_schema("word-font")

  def __init__(
      self, font_family=None, font_style=None, font_size=None, font_weight=None
  ):
    self.element = ET.Element("word-font")
    if font_family:
      self.element.set("font-family", font_family)
    if font_style:
      self.element.set("font-style", font_style)
    if font_size:
      self.element.set("font-size", str(font_size))
    if font_weight:
      self.element.set("font-weight", font_weight)
    _current_context.add_child(self)


class LyricFont(MusicElementBase):
  schema = create_schema("lyric-font")

  def __init__(
      self,
      number=None,
      name=None,
      font_family=None,
      font_style=None,
      font_size=None,
      font_weight=None,
  ):
    self.element = ET.Element("lyric-font")
    if number:
      self.element.set("number", str(number))
    if name:
      self.element.set("name", name)
    if font_family:
      self.element.set("font-family", font_family)
    if font_style:
      self.element.set("font-style", font_style)
    if font_size:
      self.element.set("font-size", str(font_size))
    if font_weight:
      self.element.set("font-weight", font_weight)
    _current_context.add_child(self)


class LyricLanguage(MusicElementBase):
  schema = create_schema("lyric-language")

  def __init__(self, number=None, name=None, lang=None):
    self.element = ET.Element("lyric-language")
    if number:
      self.element.set("number", str(number))
    if name:
      self.element.set("name", name)
    if lang:
      self.element.set("xml:lang", lang)
    _current_context.add_child(self)


class Direction(MusicElementBase):
  schema = create_schema("direction")

  def __init__(self, placement=None, **kwargs):
    self.element = ET.Element("direction")
    if placement:
      self.element.set("placement", placement)

    for key, value in kwargs.items():
      if value is not None:
        attr_name = key.replace("_", "-")
        self.element.set(attr_name, str(value))
    _current_context.add_child(self)


class DirectionType(MusicElementBase):
  schema = create_schema("direction-type")

  def __init__(self, id=None):
    self.element = ET.Element("direction-type")
    if id:
      self.element.set("id", id)
    _current_context.add_child(self)


class Pedal(MusicElementBase):
  schema = create_schema("pedal")

  def __init__(self, type, line=None, sign=None, **kwargs):
    self.element = ET.Element("pedal")
    self.element.set("type", type)  # "start", "stop", "sostenuto", etc.
    if line:
      self.element.set("line", line)  # "yes", "no"
    if sign:
      self.element.set("sign", sign)  # "yes", "no"

    for key, value in kwargs.items():
      if value is not None:
        attr_name = key.replace("_", "-")
        self.element.set(attr_name, str(value))
    _current_context.add_child(self)


class Lyric(MusicElementBase):
  schema = create_schema("lyric")

  def __init__(self, number=None, text=None, syllabic=None):
    self.element = ET.Element("lyric")
    if number:
      self.element.set("number", str(number))
    if syllabic is not None:
      syllabic_el = ET.Element("syllabic")
      syllabic_el.text = syllabic
      self.element.append(syllabic_el)  # Add to self.element
    if text is not None:
      text_el = ET.Element("text")
      text_el.text = text
      self.element.append(text_el)  # Add to self.element
    _current_context.add_child(self)


with ScorePartwise() as score:
  Work(work_title="Sample Work")
  MovementTitle("Sample Movement")
  Identification(
      creator_text="John Doe",
      creator_type="composer",
      rights_text="Copyright 2023 John Doe",
      software_name="My Music Software",
  )
  with Defaults():
    Scaling(millimeters=7.23, tenths=40)
    with PageLayout(page_height=1250, page_width=950):
      PageMargins(
          type="both",
          left_margin=75,
          right_margin=75,
          top_margin=80,
          bottom_margin=80,
      )
    system_margins_obj = SystemMargins(left_margin=0, right_margin=0)
    with SystemLayout(  # pytype: disable=wrong-arg-types
        system_distance=120, top_system_distance=70, margins=system_margins_obj
    ):
      pass  # SystemLayout is a context manager; SystemMargins is now an argument.
    StaffLayout(staff_distance=80)
    with Appearance():
      pass  # LineWidth, NoteSize, etc. could be added here
    MusicFont(font_family="Maestro", font_size="20.5")
    WordFont(font_family="Times New Roman", font_size="10")
    LyricFont(number="1", font_family="Arial", font_size="9")
    LyricLanguage(number="1", lang="en")
  Credit(credit_words_text="Sample Credit", font_size="10", justify="center")
  with PartList():
    ScorePart(id="P1", part_name="Violin")
    ScorePart(id="P2", part_name="Cello")
  with Part(id="P1"):
    with Measure(1):
      Attributes(
          divisions=1,
          key_fifths=0,
          time_beats=4,
          time_beat_type=4,
          clef_sign="G",
          clef_line=2,
      )
      slur_1_number = "1"  # Explicitly manage slur numbers for pairing
      with Note(
          pitch=Pitch(step_text="C", octave_text="4"), duration=4
      ) as note1:
        Lyric(number=1, text="Hell", syllabic="begin")
        with Notations():
          Slur(type="start", placement="above", number=slur_1_number)
      with Note(
          pitch=Pitch(step_text="D", octave_text="4", alter_text="1"),
          duration=4,
      ) as note2:
        Lyric(number=1, text="-lo", syllabic="end")
        with Notations():
          Slur(type="stop", number=slur_1_number)
      Note(rest=True, duration=2)  # A half rest
      Note(pitch=Pitch(step_text="E", octave_text="4"), duration=2)

      with Direction(placement="below"):
        with DirectionType():
          Pedal(type="start", line="yes")

  with Part(id="P2"):
    with Measure(1):
      Attributes(
          divisions=1,
          key_fifths=0,
          time_beats=4,
          time_beat_type=4,
          clef_sign="F",
          clef_line=4,
      )
      with Note(pitch=Pitch(step_text="E", octave_text="3"), duration=4):
        Lyric(number=1, text="World", syllabic="single")
      Note(pitch=Pitch(step_text="F", octave_text="3"), duration=4)
      with Direction(placement="below"):
        with DirectionType():
          Pedal(type="stop", line="yes")
