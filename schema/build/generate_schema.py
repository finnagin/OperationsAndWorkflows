#!/usr/bin/env python
"""Generate JSON Schema for operations."""
import glob
import json
from pathlib import Path
import re

import yaml
from yaml.loader import SafeLoader

THIS_DIR = Path(__file__).parent
SCHEMA_DIR = THIS_DIR.parent
OPERATIONS_DIR = SCHEMA_DIR.parent / "operations"


def generate_component(op: str):
    """Generate operation component schema."""
    yamlpath = OPERATIONS_DIR / f"{op}.yml"

    with open(yamlpath, "r") as stream:
        data = yaml.load(stream, Loader=SafeLoader)

    return {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "enum": [
                    op,
                ],
            },
            "parameters": data["parameters"],
        },
        "required": [
            "id",
        ] + (["parameters"] if data["parameters"].get("required") else []),
        "additionalProperties": False,
    }


def snakecase_to_pascalcase(string):
    """Convert this_case to ThisCase."""
    return re.sub(
        r"(?:_|^)([a-z])",
        lambda matchobj: matchobj.group(1).upper(),
        string,
    )


def op_to_component(op):
    """Convert operation id into JSON Schema component name."""
    return "Operation" + snakecase_to_pascalcase(op)


if __name__ == "__main__":
    operations = sorted([    
        Path(filename).stem
        for filename in glob.glob(str(OPERATIONS_DIR / "*.yml"))
    ])
    operation = {
        "$schema": "https://json-schema.org/draft-07/schema",
        "$id": "http://standards.ncats.io/operation.json",
        "anyOf": [
            {
                "$ref": f"#/$defs/{op_to_component(op)}"
            }
            for op in operations
        ],
        "$defs": {
            op_to_component(op): generate_component(op)
            for op in operations
        },
    }
    with open(SCHEMA_DIR / "operation.json", "w") as stream:
        json.dump(operation, stream, indent=4)
