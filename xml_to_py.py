import xml.etree.ElementTree as ET
import logging
import musicxml_schema
import inspect

def to_snake_case(name: str) -> str:
  """Converts a hyphen-separated, camelCase, or PascalCase string to snake_case.

  Examples:
  - "camelCase" -> "camel_case"
  - "PascalCase" -> "pascal_case"
  - "attr1" -> "attr1"
  - "sourceURL" -> "source_url"
  - "my-attribute" -> "my_attribute"
  """
  return "_".join(name.split("-")).lower()


def to_pascal_case(name: str) -> str:
  """Converts a hyphen-separated string to PascalCase.

  Examples:
  - "my-tag" -> "MyTag"
  - "tag1" -> "Tag1"
  """
  # Split the string by hyphens, capitalize each part, and join them.
  return "".join(word.capitalize() for word in name.split("-"))


def translate_xml_to_python(xml_string: str) -> str:
  """Translates an XML string into a Python code string based on specific rules.

  Rules:
  1. Each XML element becomes a Python object creation with a PascalCase name.
     <my-tag/> -> MyTag()
  2. Element attributes become snake_case keyword arguments.
     <tag myAttr="val"/> -> Tag(my_attr="val")
  3. Nested elements are placed inside a 'with' block of the parent.
     <parent><child/></parent> -> with Parent():\n    Child()

  Args:
      xml_string: A string containing the XML to be translated.

  Returns:
      A string containing the formatted Python code.

  Raises:
      ET.ParseError: If the XML string is malformed.
  """
  try:
    # Sanitize input by removing leading/trailing whitespace
    clean_xml = xml_string.strip()
    if not clean_xml:
      return ""

    root = ET.fromstring(clean_xml)
    return _generate_code(root, 0)
  except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
    raise


def _generate_code(element: ET.Element, indent_level: int, parent_schema_class: type = None) -> str:
  """Recursively traverses the ElementTree and generates the Python code string.

  Args:
      element: The current xml.etree.ElementTree.Element node.
      indent_level: The current level of indentation for pretty-printing.

  Returns:
      The generated Python code string for the element and its children.
  """
  indent = "    " * indent_level

  # Convert tag to PascalCase for the Python class name
  class_name = to_pascal_case(element.tag)
  children = list(element)

  has_plain_text_arg = False
  schema_class = None
  try:
    # Dynamically get the class from the musicxml_schema module
    if parent_schema_class:
      schema_class = getattr(parent_schema_class, class_name, None)
    if not schema_class:
      schema_class = getattr(musicxml_schema, class_name)
    # Inspect the __init__ method for plain_text argument
    init_signature = inspect.signature(schema_class.__init__)
    if "plain_text" in init_signature.parameters:
      has_plain_text_arg = True
  except AttributeError:
    logging.warning(f"Class {class_name} not found in schema. Skipping.")
    return ""
  except TypeError:
    logging.warning(f"Failed to inspect class {class_name} in schema. Skipping.")
    return ""

  args = []
  if has_plain_text_arg:
    text_content = element.text.strip().replace('"', '\\"') if element.text else ""
    args.append(f'"{text_content}"')

  # Handle attributes as keyword arguments.
  attr_args = [
      f'{to_snake_case(key)}="{value}"' for key, value in element.attrib.items()
  ]
  args.extend(attr_args)

  # Combine all arguments into a single string.
  all_args_str = ", ".join(args)

  # Get child elements

  # If the element has children, use a 'with' statement
  if children:
    # Generate the 'with' statement line
    code_lines = [f"{indent}with {class_name}({all_args_str}):"]

    # Recursively generate code for each child element
    for child in children:
      code_lines.append(_generate_code(child, indent_level + 1, schema_class))

    return "\n".join(code_lines)
  else:
    # If there are no children, it's a simple object instantiation
    return f"{indent}{class_name}({all_args_str})"


# --- Example Usage ---
if __name__ == "__main__":
  with open("score.xml", "r") as f:
    xml_string = f.read()
  print("""from musicxml_schema import *
from musicxml import _\n\n""")
  print(translate_xml_to_python(xml_string))
