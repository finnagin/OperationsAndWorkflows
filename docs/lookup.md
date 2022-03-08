# lookup

This operation adds knodes/kedges and (complete) results. It is equivalent to the workflow fill + bind + complete_results. Any constraints specified in the TRAPI must be respected. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/fill_and_bind/messages/01_qgraph.json), [output](../examples/fill_and_bind/messages/04_complete_results.json)

### input requirements

None

### output guarantees

- results complete

### allowed changes

- add knodes
- add kedges
- add results

### parameters

```yaml
{}
```
