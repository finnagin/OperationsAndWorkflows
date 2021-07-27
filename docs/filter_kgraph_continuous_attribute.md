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
  qedge_keys:
    description: This indicates if you only want to remove edges with specific edge_keys.
      If not provided or empty, all edges will be filtered on.
    example:
    - e01
    items:
      type: string
    type: array
  qnode_keys:
    default: []
    description: This indicates if you only want nodes corresponding to a specific
      list of qnode_keys to be removed. If not provided or empty, no nodes will be
      removed when filtering. Allows us to know what to do with the nodes connected
      to edges that are removed.
    example:
    - n01
    items:
      type: string
    type: array
  remove_above_or_below:
    description: Indicates whether to remove above or below the given threshold.
    enum:
    - above
    - below
    type: string
  threshold:
    description: The value to compare attribute values to.
    example: 1.2
    type: number
required:
- edge_attribute
- threshold
- remove_above_or_below
type: object
```
