# filter kgraph (percentile)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph edges that have attribute values are below/above the given percentile.

### examples

- [input](../examples/fill_and_filter/messages/05_filtered_kgraph_stat_input.json), [output](../examples/fill_and_filter/messages/06_filtered_kgraph_std_dev_output.json)

### input requirements

None

### output guarantees

- no edges in the kgraph which have attribute values are below/above the given percentile.

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
  qnode_keys:
    default: null
    description: This indicates if you only want nodes corresponding to a specific
      list of qnode_keys to be removed. If not provided oe empty no nodes will be
      removed when filtering.
    example:
    - n01
    type: array
  remove_above:
    default: false
    description: Indictes whether to remove above or below the given threshold.
    example: true
    type: bool
  threshold:
    default: 95
    description: The percentile to threshold on.
    example: 96.8
    maximum: 100
    minimum: 0
    type: float
required:
- edge_attribute
type: object
```
