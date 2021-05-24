# overlay compute jaccard

_subclass of [overlay](./overlay.md)_

This operation computes the Jaccard Similarity which measures how many intermediate_node_key's are directly connected to both the start_node_key and end_node_key for all pairs of start_node_keys and end_node_keys. It will then add edges to the knowledge graph along with edge attributes (with the property name jaccard_index) between each start_node_key and object_node_key. A query graph edge will also be added using the key specified by virtual_relation_label. This is used for purposes such as "find me all drugs (start_node_key) that have many proteins (intermediate_node_key) in common with this disease (end_node_key)." This can be used for downstream filtering to concentrate on relevant bioentities.

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
  end_node_keys:
    description: A list of qnode keys specifying the ending nodes.
    example:
    - n0
    - n2
    type: array
  intermediate_node_key:
    description: A qnode key specifying the intermediate node.
    example: n1
    type: string
  virtual_relation_label:
    description: The key of the query graph edge that corresponds to the knowledge
      graph edges that were added by this operation.
    example: J1
    type: string
required:
- intermediate_node_key
- end_node_keys
- virtual_relation_label
type: object
```
