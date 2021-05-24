# overlay compute jaccard

_subclass of [overlay](./overlay.md)_

This operation computes the Jaccard similarity that measures how many intermediate_node_key's are shared in common between each start_node_key and object_node_key. And it will then create virtual edges and add edge attributes (with the property name jaccard_index) between each start_node_key and object_node_key. This is used for purposes such as "find me all drugs (start_node_key) that have many proteins (intermediate_node_key) in common with this disease (end_node_key)." This can be used for downstream filtering to concentrate on relevant bioentities.

### examples

- [input](../examples/overlay/messages/09_input_jaccard.json), [output](../examples/overlay/messages/10_output_jaccard.json)

### input requirements

None

### output guarantees

None

### allowed changes

- add kedges
- add qedges
- add bindings to results

### parameters

```yaml
properties:
  end_node_key:
    description: A qnode key specifying the ending node.
    example: n2
    type: string
  intermediate_node_key:
    description: A qnode key specifying the intermediate node.
    example: n1
    type: string
  start_node_key:
    description: A qnode key specifying the starting node.
    example: n0
    type: string
  virtual_relation_label:
    description: An label to help identify the virtual edge in the relation field.
    example: J1
    type: string
required:
- start_node_key
- intermediate_node_key
- end_node_key
- virtual_relation_label
type: object
```
