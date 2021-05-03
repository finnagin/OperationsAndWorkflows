# overlay compute ngd

_subclass of [overlay](./overlay.md)_

This operation computes the normalized Google distance (co-occurrence frequency) in PubMed abstracts and adds virual edges between qnodes AND/OR knodes AND/OR results edge bindings.

### examples

- [input](../examples/overlay/messages/07_input_ngd.json), [output](../examples/overlay/messages/08_output_ngd.json)

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
  default_value:
    default: -1
    description: The default value of the normalized Google distance. (if no publications
      can be found) The value -1 will be treated as infinity.
    example: 999
    minimum: -1
    type: number
  qnode_keys:
    description: A list of qnode keys to overlay pairwise edges onto. Must be be a
      list of at least 2 valid qnodes.
    example:
    - n00
    - n01
    items:
      type: string
    type: list
  virtual_relation_label:
    description: An label to help identify the virtual edge in the relation field
    example: NGD1
    type: string
required:
- virtual_relation_label
- qnode_keys
type: object
```
