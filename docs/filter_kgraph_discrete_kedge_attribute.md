# filter kgraph (discrete kedge attribute)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph edges which have a discrete attribute containing the specified value. Edges without the given attribute are left alone.

### examples

- [input](../examples/fill_and_filter/messages/11_filtered_kgraph_discrete_attribute_input.json), [output](../examples/fill_and_filter/messages/12_filtered_kgraph_discrete_attribute_output.json)

### input requirements

None

### output guarantees

- no edges exist in the kgraph that have the specified attribute with the given value.

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
      to edges that are removed
    example:
    - n01
    items:
      type: string
    type: array
  remove_value:
    description: The value for which all edges containing this value in the specified
      edge_attribute should be removed.
    example: infores:semmeddb
required:
- edge_attribute
- remove_value
type: object
```
