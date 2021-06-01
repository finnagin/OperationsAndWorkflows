# Overlay Fisher exact test

_subclass of [overlay](./overlay.md)_

Fisher exact test computes the Fisher's Exact Test p-values of the connection between a list of given nodes with specified query id (subject_qnode_key e.g. n01) to their adjacent nodes with specified query id (object_qnode_key e.g. n02) in the message knowledge graph. This information is then added as an edge attribute to a virtual edge which is then added to the query graph and knowledge graph. It can also allow you to filter out the user-defined insignificance of connections based on a specified p-value cutoff or return the top n smallest p-value of connections and only add their corresponding virtual edges to the knowledge graph.

### examples

- [input](../examples/overlay/messages/11_input_fisher.json), [output](../examples/overlay/messages/12_output_fisher.json)

### input requirements

None

### output guarantees

None

### allowed changes

- add kedges
- add qedges
- add bindings to results

### parameters

```yaml
properties:
  object_qnode_key:
    description: A specific object query node id.
    example: n2
    type: string
  rel_edge_key:
    description: A specific Qedge id connected to both subject nodes and object nodes
      in message KG (optional, otherwise all edges connected to both subject nodes
      and object nodes in message KG are considered).
    example: e01
    type: string
  subject_qnode_key:
    description: A specific subject query node id.
    example: n1
    type: string
  virtual_relation_label:
    description: An label to help identify the virtual edge.
    example: f1
    type: string
required:
- subject_qnode_key
- object_qnode_key
- virtual_relation_label
type: object
```
