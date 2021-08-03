# filter kgraph (discrete knode attribute)

_subclass of [filter_kgraph](./filter_kgraph.md)_

This operation removes kgraph nodes which have a discrete attribute containing the specified value. In TRAPI 1.1+ this will look in the `attribute_type_id` and `original_attribute_name` attribute fields for the attribute name. Node without the given attribute are left alone. Edges connecting to the removed nodes will also be removed.

### examples

- [input](../examples/fill_and_filter/messages/13_filtered_kgraph_discrete_knode_attribute_input.json), [output](../examples/fill_and_filter/messages/14_filtered_kgraph_discrete_knode_attribute_output.json)

### input requirements

None

### output guarantees

- no nodes exist in the kgraph that have the specified attribute with the given value.

### allowed changes

- remove knodes
- remove kedges

### parameters

```yaml
properties:
  node_attribute:
    description: The name of the node attribute to filter on.
    example: molecule_type
    type: string
  qnode_keys:
    description: This indicates if you only want to remove nodes corresponding to
      a specific list of qnode_keys to be removed. If not provided or empty, all nodes
      will be considered when filtering.
    example:
    - n01
    items:
      type: string
    type: array
  remove_value:
    description: The value for which all edges containing this value in the specified
      edge_attribute should be removed.
    example: small_molecule
required:
- node_attribute
- remove_value
type: object
```
