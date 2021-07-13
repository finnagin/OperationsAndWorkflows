# annotate (edges)

_subclass of [annotate](./annotate.md)_

This operation adds attributes to knowledge graph edges. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/annotation/messages/01_knowledge.json), [output](../examples/annotation/messages/04_annotated_edges.json)

### input requirements

None

### output guarantees

None

### allowed changes

- add attributes to kedges

### parameters

```yaml
properties:
  attributes:
    description: A list of attributes to anotate the edges with. If not included then
      all available data will be anotated.
    example:
    - pmids
    type: array
type: object
```
