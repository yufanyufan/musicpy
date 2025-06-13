import argparse
import ast
import textwrap


def _get_callable_name(node):
  """Helper function to extract the name of a callable from an AST node."""
  if isinstance(node, ast.Name):
    return node.id
  elif isinstance(node, ast.Attribute):
    return f"{_get_callable_name(node.value)}.{node.attr}"
  else:
    return f"<{type(node).__name__}>"


def _get_ast_node_representation(value_to_repr):
  """Helper function to get a human-readable string representation of a value."""
  if isinstance(value_to_repr, list):
    return (
        f"[{', '.join(_get_ast_node_representation(item) for item in value_to_repr)}]"
    )
  elif isinstance(value_to_repr, ast.Constant):
    return repr(value_to_repr.value)
  elif isinstance(value_to_repr, ast.Name):
    return value_to_repr.id
  elif isinstance(value_to_repr, ast.Attribute):
    return _get_callable_name(value_to_repr)
  elif isinstance(value_to_repr, ast.Call):
    return f"{_get_callable_name(value_to_repr.func)}(...)"
  elif isinstance(value_to_repr, ast.Tuple):
    return (
        f"({', '.join(_get_ast_node_representation(elt) for elt in value_to_repr.elts)})"
    )
  elif isinstance(value_to_repr, ast.AST):
    return f"<{type(value_to_repr).__name__}>"
  else:
    return repr(value_to_repr)


ALLOWED_AST_NODE_TYPES = {
    "Call",
    "Constant",
    "Expr",
    "Load",
    "Module",
    "Name",
    "USub",
    "UnaryOp",
    "With",
    "keyword",
    "withitem",
    "Tuple",
    "Pass",
    "Store",
}


def get_ast_node_types(file_path):
  """Parses a Python file, validates AST node types and invoked callables.

  Args:
    file_path: Path to the Python file.

  Returns:
    A tuple containing:
      - A boolean indicating if the file is compliant.
      - A set of disallowed AST node types found.
      - A set of system built-in functions called.
  """
  with open(file_path, "r") as source:
    return is_vallina_musicpy(source.read())


def is_vallina_musicpy(musicpy: str) -> bool:
  tree = ast.parse(musicpy)
  node_types = set()
  invoked_callables = set()
  for node in ast.walk(tree):
    node_types.add(type(node).__name__)
    if isinstance(node, ast.Call):
      callable_name = _get_callable_name(node.func)
      invoked_callables.add(callable_name)

  disallowed_node_types = node_types - ALLOWED_AST_NODE_TYPES
  disallowed_callables = {
      name for name in invoked_callables if name[0].islower()
  }

  is_compliant = not disallowed_node_types and not disallowed_callables
  return is_compliant, disallowed_node_types, disallowed_callables


PREEMBLE = """
from musicpy_schema import *
from musicpy import MusicPy
with MusicPy() as __score:
"""


def safe_exec_musicpy(musicpy: str) -> str:
  """Safely executes the musicpy code and returns the result."""
  result = {}
  if not is_vallina_musicpy(musicpy)[0]:
    raise ValueError("musicpy not vallina")
  exec(PREEMBLE + textwrap.indent(musicpy, "  "), {}, result)
  return str(result["__score"].get_xml())


def print_ast_node_field_values(file_path):
  """Parses a Python file, collects and prints all unique fields and their observed values for each AST node type.

  Args:
    file_path: Path to the Python file.
  """
  with open(file_path, "r") as source:
    tree = ast.parse(source.read())

  node_field_values = {}
  for node in ast.walk(tree):
    node_type = type(node).__name__
    if node_type not in node_field_values:
      node_field_values[node_type] = {}

    if hasattr(node, "_fields"):
      for field_name in node._fields:
        if field_name not in node_field_values[node_type]:
          node_field_values[node_type][field_name] = set()
        field_value = getattr(node, field_name)
        field_value_repr = _get_ast_node_representation(field_value)
        node_field_values[node_type][field_name].add(field_value_repr)

  for node_type, fields_data in node_field_values.items():
    print(f"Node type: {node_type}")
    for field_name, value_set in fields_data.items():
      print(f"  {field_name}:")
      print(f"    {sorted(list(value_set))}")
    print("-" * 20)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Analyze Python file AST.")
  parser.add_argument(
      "file_path", type=str, help="Path to the Python file to analyze."
  )
  parser.add_argument(
      "--print_args",
      action="store_true",
      help=(
          "Print detailed AST node fields and their unique values instead of"
          " compliance check."
      ),
  )
  args = parser.parse_args()
  file_to_analyze = args.file_path

  try:
    if args.print_args:
      print_ast_node_field_values(file_to_analyze)
    else:
      is_compliant, disallowed_node_types, system_builtins_called = (
          get_ast_node_types(file_to_analyze)
      )
      if is_compliant:
        print(f"The file '{file_to_analyze}' is compliant.")
      else:
        print(f"The file '{file_to_analyze}' is NOT compliant.")
        if disallowed_node_types:
          print(f"Disallowed AST node types found: {disallowed_node_types}")
        if system_builtins_called:
          print(f"System built-in functions called: {system_builtins_called}")
  except FileNotFoundError:
    print(f"Error: File not found at '{file_to_analyze}'")
  except SyntaxError as e:
    print(f"Error: Syntax error in '{file_to_analyze}': {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
