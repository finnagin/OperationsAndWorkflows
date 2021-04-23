"""Validate operations."""
import json
from pathlib import Path

import jsonschema
import yaml
from yaml.loader import SafeLoader

THIS_DIR = Path(__file__).parent
OPS_DIR = THIS_DIR.parent

with open(THIS_DIR / "schema.json", "r") as stream:
    meta_schema = json.load(stream)

for filename in OPS_DIR.glob("*.yml"):
    with open(filename, "r") as stream:
        op_spec = yaml.load(stream, Loader=SafeLoader)
    jsonschema.validate(op_spec, meta_schema)
