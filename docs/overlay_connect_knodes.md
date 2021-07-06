# Overlay connect knodes

_subclass of [overlay](./overlay.md)_

Given a TRAPI message, create new kedges between existing knodes.  These may be created using arbitrary methods or data sources, though provenance should be attached to the new kedges.   Each new kedge is also added to all results containing node bindings to both the subject and object knodes.  This may be independent of any qedge connections, i.e. kedges can be created between any nodes in the kgraph.

### examples

- [input](../examples/overlay/messages/13_input_connectknodes.json), [output](../examples/overlay/messages/14_output_connectknodes.json)

### input requirements

None

### output guarantees

None

### allowed changes

- add kedges
- add bindings to results

### parameters

```yaml
{}
```
