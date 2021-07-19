# filter kgraph (standard deviation)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph edges that have attribute values are below/above the mean +/- n standard deviations.

### examples

- [input](../examples/fill_and_filter/messages/05_filtered_kgraph_stat_input.json), [output](../examples/fill_and_filter/messages/06_filtered_kgraph_std_dev_output.json)

### input requirements

None

### output guarantees

- no edges in the kgraph which have attribute values are below/above the mean +/- n standard deviations.

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
  num_sigma:
    default: 1
    description: The number of standard deviations to threshold on.
    example: 1.2
    minimum: 0
    type: float
  plus_or_minus_std_dev:
    default: plus
    description: Indicate whether or not the threshold should be found using plus
      or minus the standard deviation. E.g. when plus_or_minus_std_dev is set to plus
      will set the cutoff for filtering as the mean + num_sigma * std_dev while setting
      plus_or_minus_std_dev to minus will set the cutoff as the mean - num_sigma *
      std_dev.
    enum:
    - plus
    - minus
    type: string
  qedge_keys:
    description: This indicates if you only want to filter on specific edge_keys.
      If not provided or empty, all edges will be filtered on.
    example:
    - e01
    type: array
  qnode_keys:
    default: []
    description: This indicates if you only want nodes corresponding to a specific
      list of qnode_keys to be removed. If not provided or empty, no nodes will be
      removed when filtering.
    example:
    - n01
    type: array
  remove_above_or_below:
    default: below
    description: Indictes whether to remove above or below the given threshold.
    enum:
    - above
    - below
    type: string
required:
- edge_attribute
type: object
```
