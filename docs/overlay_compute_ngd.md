# overlay compute ngd

_subclass of [overlay](./overlay.md)_

This operation computes the normalized Google distance (co-occurrence frequency) in PubMed abstracts and adds virual edges between qnodes AND/OR knodes.

### examples

- [input](../examples/overlay/messages/07_input_ngd.json), [output](../examples/overlay/messages/08_output_ngd.json)

### input requirements

- Input qgraph contains the two qnodes specified in 'subject_qnode_key' and 'object_qnode_key'

### output guarantees

- At least 1 new edge between qnodes

### allowed changes

- add kedges
- add qedges
- add bindings to results

### parameters

```yaml
properties:
  default_value:
    default: inf
    description: The default value of the normalized Google distance (if its value
      cannot be determined)
    example: 0
    maximum: inf
    minimum: 0
    type: string
  object_qnode_key:
    description: A specific object query node id
    example: n01
    type: string
  subject_qnode_key:
    description: A specific subject query node id
    example: n00
    type: string
  virtual_relation_label:
    description: An label to help identify the virtual edge in the relation field
    example: NGD1
    type: string
required:
- virtual_relation_label
- subject_qnode_key
- object_qnode_key
type: object
```
