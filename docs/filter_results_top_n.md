# filter results (top-n)

_subclass of [filter_results](./filter_results.md)_

This operation truncates the results to at most `max_results` that appear in the TRAPI JSON message.

### examples

- [input](../examples/fill_and_filter/messages/02_results_full.json), [output](../examples/fill_and_filter/messages/03_filtered_results_top_n.json)

### input requirements

None

### output guarantees

- max `max_results` results

### allowed changes

- remove results

### parameters

```yaml
properties:
  max_results:
    description: The maximum number of results to return.
    example: 50
    minimum: 0
    type: integer
required:
- max_results
type: object
```
