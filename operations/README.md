# Translator Operations

[Operation Index](../docs/index.md)

## rules

- all of these operations are predicated on adherence to the TRAPI OpenAPI spec
  - e.g. allowing the change “remove properties from bindings” does not permit removal of the required property `id`
- allowing a non-leaf change allows all of its descendants and no other edits
- all changes not explicitly allowed are disallowed
- allowed changes followed by a “?” are configurable
  - e.g. with a flag indicating whether the “score” operation is permitted to edit existing result properties

## definitions

| term    | definition |
| ------- | --- |
| qgraph  | the query graph: `message.query_graph` |
| qnode   | a node in the query graph: `message.query_graph.nodes.*` |
| qedge   | an edge in the knowledge graph: `message.query_graph.edges.*` |
| kgraph  | the knowledge graph: `message.knowledge_graph` |
| knode   | a node in the knowledge graph: `message.knowledge_graph.nodes.*` |
| kedge   | an edge in the knowledge graph: `message.knowledge_graph.edges.*` |
| result  | an element of the results array: `message.results[i]` |
| binding | a node or edge binding: `message.results[i].node_bindings.*` or `message.results[i].edge_bindings.*` |
| pinned  | (for a qnode) having an `id` CURIE specified |

## change hierarchy

- change qgraph
  - change qnodes
    - add qnodes
    - remove qnodes
    - edit qnodes
      - add properties to qnodes
      - remove properties from qnodes
      - edit properties of qnodes
  - change qedges
    - add qedges
    - remove qedges
    - edit qedges
      - add properties to qedges
      - remove properties from qedges
      - edit properties of qedges
- change kgraph
  - change knodes
    - add knodes
    - remove knodes
    - edit knodes
      - add attributes to knodes
      - remove attributes from knodes
      - edit attributes of knodes
  - change kedges
    - add kedges
    - remove kedges
    - edit kedges
      - add attributes to kedges
      - remove attributes from kedges
      - edit attributes of kedges
- change results
  - add results
  - remove results
  - edit results
    - add properties to results
    - remove properties from results
    - edit properties of results
      - add bindings to results
      - remove bindings from results
      - edit bindings of results

## general message formatting requirements

- **no orphaned edges**: The `subject` and `object` for all qedges and kedges MUST map to qnode and knode keys, respectively.
- **no orphaned bindings**: Each binding MUST map a knode or kedge key to a qnode or qedge key, respectively, OR to the dummy id “_”.
- [optional] unbound things: There MAY be un-bound qnodes, qedges, knodes, and/or kedges.
- **unique query graph ids**: All qnode and qedge keys MUST be unique within the qgraph.
- **unique knowledge graph ids**: All knode and kedge keys MUST be unique globally. i.e. the same id should not be used to refer to two distinct kedges, even in response to two completely distinct queries.
