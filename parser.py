import yaml
import re
from datetime import datetime

# Define which keys should use quoted symbols instead of strings
symbol_fields = {"part_no"}

def make_symbol(s):
    """Sanitize keys for use in LISP-style symbols."""
    return re.sub(r'\s+', '_', s.lower())

def format_value(key, value):
    """Format different value types into S-expression-compatible values."""
    if isinstance(value, str):
        # Check for date format
        try:
            dt = datetime.strptime(value, "%Y-%m-%d")
            return f'(make-date {dt.year:04d} {dt.month:02d} {dt.day:02d})'
        except ValueError:
            pass

        # Quote as LISP symbol if key requires it
        if key in symbol_fields:
            return f"'{value}'"  # LISP-style quoted symbol
        else:
            return '"' + value.replace('"', '\\"') + '"'

    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'nil'
    else:
        return str(value)

def yaml_to_sexpr(data, namespace='yaml'):
    """Recursively convert parsed YAML data into S-expressions."""
    if isinstance(data, dict):
        items = []
        for key, value in data.items():
            sym_key = f"{namespace}:{make_symbol(str(key))}"
            expr = yaml_to_sexpr(value, namespace)
            if isinstance(expr, list):
                items.append(f"({sym_key} {' '.join(expr)})")
            else:
                items.append(f"({sym_key} {expr})")
        return items

    elif isinstance(data, list):
        items = []
        for item in data:
            expr = yaml_to_sexpr(item, namespace)
            if isinstance(expr, list):
                items.append(f"({namespace}:item {' '.join(expr)})")
            else:
                items.append(f"({namespace}:item {expr})")
        return items

    else:
        return format_value('', data)

def convert_yaml_to_sexpr(yaml_str):
    """Load YAML string and return a complete top-level S-expression."""
    parsed_yaml = yaml.safe_load(yaml_str)
    exprs = yaml_to_sexpr(parsed_yaml)
    return f"({'\n '.join(exprs)})"
