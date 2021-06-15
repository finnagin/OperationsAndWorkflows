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
  qnode_key:
    default: null
    description: If remove_connected_nodes is set to True this indicates if you only
      want nodes corresponding to a specific qnode_key to be removed. If not provided
      the qnode_key will not be considered when filtering.
    example: n01
    type: string
  remove_above:
    default: false
    description: Indictes whether to remove above or below the given threshold.
    example: true
    type: bool
  remove_connected_nodes:
    default: false
    description: Indicates whether or not to remove the nodes connected to the edges.
    example: true
    type: bool
  threshold:
    default: 1
    description: The number of standard deviations to threshold on.
    example: 1.2
    minimum: 0
    type: float
  top:
    default: true
    description: Indicate whether or not the threshold should be placed in the top
      or bottom of the values. E.g. top set as True will set the cutoff for filtering
      as the mean + threshold * std_dev while setting top to False will set the cutoff
      as the mean - std_dev * threshold.
    example: false
    type: bool
required:
- edge_attribute
type: object
```
