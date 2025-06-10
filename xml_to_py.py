import inspect
import types
import typing
import logging
import xml.etree.ElementTree as ET
import musicxml_schema


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
  return _generate_code(ET.fromstring(xml_string), 0)


def _convert_to_python_value(value: str, param_type: str) -> str:
  """Converts an attribute value from string to the specified type.

  Args:
      value: The string value of the attribute.
      param_type: The expected type of the attribute.

  Returns:
      The converted value as a string, or the original value if conversion
      fails.
  """
  param_type = param_type.split("|")[0].strip()
  if param_type == "int":
    return str(int(value))
  elif param_type == "float":
    return str(float(value))
  elif param_type == "bool":
    if value.lower() == "true":
      return "True"
    elif value.lower() == "false":
      return "False"
    else:
      raise ValueError(f"Invalid boolean value: {value}")
  else:
    return repr(value)


def _generate_code(
    element: ET.Element, indent_level: int, parent_schema_class: type = None
) -> str:
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
  # Dynamically get the class from the musicxml_schema module
  if parent_schema_class:
    schema_class = getattr(parent_schema_class, class_name, None)
  if not schema_class:
    schema_class = getattr(musicxml_schema, class_name)
  # Inspect the __init__ method for plain_text argument
  init_signature = inspect.signature(schema_class.__init__)
  if "plain_text" in init_signature.parameters:
    has_plain_text_arg = True

  args = []

  if has_plain_text_arg:
    plain_text_param = init_signature.parameters.get("plain_text")
    if (
        plain_text_param
        and plain_text_param.annotation != inspect.Parameter.empty
    ):
      converted_text = _convert_to_python_value(
          element.text, plain_text_param.annotation
      )
      args.append(converted_text)
    else:
      raise ValueError(f"no plain text param found in {class_name}")

  # Handle attributes as keyword arguments.
  attr_args = []
  init_signature = inspect.signature(schema_class.__init__)
  for key, value in element.attrib.items():
    param_name = to_snake_case(key)
    param = init_signature.parameters.get(param_name)
    if param and param.annotation != inspect.Parameter.empty:
      converted_value = _convert_to_python_value(value, param.annotation)
      attr_args.append(f"{param_name}={converted_value}")
    else:
      attr_args.append(f'{param_name}="{value}"')
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
from musicxml import _

""")
  result = translate_xml_to_python(xml_string)
  print(result)
