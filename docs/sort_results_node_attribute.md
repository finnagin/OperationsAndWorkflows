# sort results (node attribute)

_subclass of [sort_results](./sort_results.md)_

This operation sorts the results by the given node attribute. If in ascending order, the maximum value of the results nodes with the given attribute will be taken while the minimum will be taken for descending order. If a result has no nodes with the given attribute, it will be listed last. If `max_results` is given, it truncates the results to at most the given value.

### examples

- [input](../examples/sort/messages/01_results_full.json), [output](../examples/sort/messages/04_sorted_results_node_attribute.json)

### input requirements

None

### output guarantees

- max `max_results` results

### allowed changes

- change results
- remove results

### parameters

```yaml
properties:
  ascending_or_descending:
    description: Indicates whether results should be sorted in ascending or descending
      order.
    enum:
    - ascending
    - descending
    type: string
  max_results:
    description: The maximum number of results to return. If not given all results
      will be returned.
    example: 50
    minimum: 0
    type: integer
  node_attribute:
    description: The name of the node attribute to order by.
    example: normalized_google_distance
    type: string
  qnode_keys:
    description: This indicates if you only want to consider nodes with specific node_keys.
      If not provided or empty, all nodes will be looked at.
    example:
    - e01
    items:
      type: string
    type: array
required:
- node_attribute
- ascending_or_descending
type: object
```
