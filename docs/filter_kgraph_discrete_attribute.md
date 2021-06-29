# filter kgraph (discrete attribute)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph edges which have a discrete attribute containing the specified value. Edges without the given attribute are left alone.

### examples

- [input](../examples/fill_and_filter/messages/11_filtered_kgraph_discrete_attribute_input.json), [output](../examples/fill_and_filter/messages/12_filtered_kgraph_discrete_attribute_output.json)

### input requirements

None

### output guarantees

- no edges in the kgraph which have the specified attribute with the given attribute.

### allowed changes

- remove knodes
- remove kedges

### parameters

```yaml
properties:
  edge_attribute:
    description: The name of the edge attribute to filter on.
    example: provided_by
    type: string
  edge_keys:
    default: null
    description: This indicates if you only want to remove edges with specific edge_keys.
      If not provided or empty, all edges will be filtered on.
    example:
    - e01
    type: array
  qnode_keys:
    default: null
    description: This indicates if you only want nodes corresponding to a specific
      list of qnode_keys to be removed. If not provided or empty, no nodes will be
      removed when filtering.
    example:
    - n01
    type: array
  threshold:
    description: The value to compare attribute values to.
    example: infores:semmeddb
    type: string
required:
- edge_attribute
- value
type: object
```
