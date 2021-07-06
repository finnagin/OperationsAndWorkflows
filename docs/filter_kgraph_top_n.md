# filter kgraph (top n)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph edges that have attribute values are below/above the top/bottom n values.

### examples

- [input](../examples/fill_and_filter/messages/05_filtered_kgraph_stat_input.json), [output](../examples/fill_and_filter/messages/08_filtered_kgraph_top_n_output.json)

### input requirements

None

### output guarantees

- no edges in the kgraph which have attribute values are below/above the top/bottom n values.

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
    description: This indicates if you only want to filter on specific edge_keys.
      If not provided or empty all edges will be filtered on and edge_key will not
      be considered when filtering.
    example:
    - e01
    type: array
  max_edges:
    default: 50
    description: The number of edges to keep.
    example: 10
    minimum: 0
    type: integer
  qnode_keys:
    default: null
    description: This indicates if you only want nodes corresponding to a specific
      list of qnode_keys to be removed. If not provided oe empty no nodes will be
      removed when filtering.
    example:
    - n01
    type: array
  top:
    default: true
    description: Indicate whether or not the the top or bottom n values should be
      kept.
    example: false
    type: bool
required:
- edge_attribute
type: object
```