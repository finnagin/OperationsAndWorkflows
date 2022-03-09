# fill

This operation adds knodes and kedges. Any constraints attached to QNodes and QEdges specified in the TRAPI must be respected. Implementations of this operation are _unique_; their behavior is not fully-specified by the operation parameters.

### examples

- [input](../examples/fill_and_bind/messages/01_qgraph.json), [output](../examples/fill_and_bind/messages/02_kgraph.json)

### input requirements

None

### output guarantees

None

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
    qedge_keys:
      description: A list of qedge keys. If included only edges corresponding to the
        given qedge keys, as well as their connected nodes, will be filled. If not
        included all edges will be filled.
      example:
      - e00
      items:
        type: string
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
    qedge_keys:
      description: A list of qedge keys. If included only edges corresponding to the
        given qedge keys, as well as their connected nodes, will be filled. If not
        included all edges will be filled.
      example:
      - e00
      items:
        type: string
      type: array
type: object
```
