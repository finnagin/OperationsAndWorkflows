# filter results (top-n)

_subclass of [Filter results](./filter_results.md)_

This operation truncates the results to at most `max_results` that appear in the TRAPI JSON message.

### examples

- [input](../examples/fill_and_filter/messages/02_results_full.json), [output](../examples/fill_and_filter/messages/03_filtered_results_top_n.json)

### input requirements

None

### output guarantees

Output will contain no more than `max_results` results.

### allowed changes

- remove results
- remove knodes
- remove kedges

### parameters

```yaml
type: object
properties:
- name: max_results
  description: The maximum number of results to return. If not provided all results will be returned.
  type: integer
  minimum: 0
  example: 50
required:
- max_results
```
