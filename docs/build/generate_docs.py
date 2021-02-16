#!/usr/bin/env python
"""Generate README documentation for operation."""
import glob
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import yaml
from yaml.loader import SafeLoader

THIS_DIR = Path(__file__).parent
DOCS_DIR = THIS_DIR.parent
OPERATIONS_DIR = DOCS_DIR.parent / "operations"

j2_env = Environment(
    loader=FileSystemLoader(THIS_DIR),
    trim_blocks=False,
    keep_trailing_newline=True,
)
op_template = j2_env.get_template("op_template.md")
index_template = j2_env.get_template("index_template.md")


def generate_md(op: str):
    """Generate README."""
    yamlpath = OPERATIONS_DIR / f"{op}.yml"

    with open(yamlpath, "r") as stream:
        data = yaml.load(stream, Loader=SafeLoader)
    data["parameters"] = yaml.dump(data["parameters"])
    markdown = op_template.render(data=data)

    with open(DOCS_DIR / f"{op}.md", "w") as stream:
        stream.write(markdown)


def generate_index(operations):
    """Generate operation index."""
    markdown = index_template.render(operations=operations)
    with open(DOCS_DIR / "index.md", "w") as stream:
        stream.write(markdown)


if __name__ == "__main__":
    operations = [    
        Path(filename).stem
        for filename in glob.glob(str(OPERATIONS_DIR / "*.yml"))
    ]
    generate_index(operations)
    for op in operations:
        generate_md(op)
