# sort results (edge attribute)

_subclass of [sort_results](./sort_results.md)_

This operation sorts the results by the given edge attribute. If in ascending order, the minimum value of the results edges with the given attribute will be taken while the maximum will be taken for descending order. If a result has no edges with the given attribute, it will be listed last. If `max_results` is given, it truncates the results to at most the given value.

### examples

- [input](../examples/sort/messages/01_results_full.json), [output](../examples/sort/messages/02_sorted_results_edge_attribute.json)

### input requirements

None

### output guarantees

None

### allowed changes

- change results

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
  edge_attribute:
    description: The name of the edge attribute to order by.
    example: normalized_google_distance
    type: string
  qedge_keys:
    description: This indicates if you only want to consider edges with specific edge_keys.
      If not provided or empty, all edges will be looked at.
    example:
    - e01
    items:
      type: string
    type: array
required:
- edge_attribute
- ascending_or_descending
type: object
```
