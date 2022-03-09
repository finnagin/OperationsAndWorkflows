# lookup_and_score

This operation adds knodes/kedges, (complete) results, and scores (to the results). It is equivalent to the workflow fill + bind + complete_results + score. Any constraints attached to QNodes and QEdges specified in the TRAPI must be respected. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/fill_and_bind/messages/01_qgraph.json), [output](../examples/fill_and_bind/messages/05_scored_results.json)

### input requirements

None

### output guarantees

- results complete

### allowed changes

- add knodes
- add kedges
- add results
- add properties to results

### parameters

```yaml
{}
```
