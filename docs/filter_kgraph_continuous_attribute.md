# filter kgraph (continuous attribute)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph edges based on the value of a continuous edge attribute. Edges without the given attribute are left alone.

### examples

- [input](../examples/fill_and_filter/messages/09_filtered_kgraph_attribute_input.json), [output](../examples/fill_and_filter/messages/10_filtered_kgraph_continuous_attribute_output.json)

### input requirements

None

### output guarantees

- no edges in the kgraph which have attribute values that are below/above the given value.

### allowed changes

- remove knodes
- remove kedges

### parameters

```yaml
properties:
  edge_attribute:
    description: The name of the edge attribute to filter on.
    example: normalized_google_distance
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
  remove_above:
    description: Indictes whether to remove above or below the given threshold.
    example: true
    type: bool
  threshold:
    description: The value to compare attribute values to.
    example: 1.2
    type: float
required:
- edge_attribute
- threshold
- remove_above
type: object
```
