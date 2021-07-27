# sort results (score)

_subclass of [sort_results](./sort_results.md)_

This operation sorts the results by the result score. If `max_results` is given, it truncates the results to at most the given value.

### examples

- [input](../examples/sort/messages/01_results_full.json), [output](../examples/sort/messages/03_sorted_results_score.json)

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
required:
- ascending_or_descending
type: object
```
