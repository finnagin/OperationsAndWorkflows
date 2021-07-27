# annotate (nodes)

_subclass of [annotate](./annotate.md)_

This operation adds attributes to knowledge graph nodes. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/annotation/messages/01_knowledge.json), [output](../examples/annotation/messages/03_annotated_nodes.json)

### input requirements

None

### output guarantees

None

### allowed changes

- add attributes to knodes

### parameters

```yaml
properties:
  attributes:
    description: A list of attributes to annotate the nodes with. If not included
      then all available data will be annotated.
    example:
    - pmids
    items:
      type: string
    type: array
type: object
```
