# fill

This operation adds knodes and kedges. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/fill_and_bind/messages/01_qgraph.json), [output](../examples/fill_and_bind/messages/02_kgraph.json)

### input requirements

None

### output guarantees

- kgraph exists

### allowed changes

- add knodes
- add kedges

### parameters

```yaml
oneOf:
- additionalProperties: false
  properties:
    allowlist:
      description: List of knowledge providers/sources that may be used to provide
        knowledge.
      example:
      - icees
      items:
        type: string
      minLength: 1
      type: array
- additionalProperties: false
  properties:
    denylist:
      description: List of knowledge providers/sources that may NOT be used to provide
        knowledge.
      example:
      - ctd
      items:
        type: string
      minLength: 1
      type: array
type: object
```
