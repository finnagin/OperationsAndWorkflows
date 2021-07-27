# enrich_results

Create new results by applying enrichment analysis to existing results.  In particular, combines results by transforming a qnode into a set, formed of knodes that share a property or relation more often than expected by chance. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/enrich/messages/01_input_enrich_results.json), [output](../examples/enrich/messages/02_output_enrich_results.json)

### input requirements

None

### output guarantees

None

### allowed changes

- add qnodes
- add qnodes
- modify qnodes
- add kedges
- add kedges
- add results

### parameters

```yaml
properties:
  pvalue_threshold:
    default: 1e-6
    description: The cutoff p-value for enrichment.
    example: 1e-7
    maximum: 1
    minimum: 0
    type: float
  qnode_keys:
    default: []
    description: If specified, then only knodes bound to these qnodes will be examined
      for enrichment and combination.
    example:
    - n01
    type: array
type: object
```
