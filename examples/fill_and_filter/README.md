# FILL & FILTER example

The FILL operation accepts (a message with) a query graph and returns (a message with) results binding the query graph to knowledge.

The FILTER RESULTS operation accepts (a message with) results and returns (a message with) a subset of those results.

The FILTER KGRAPH (ORPHANS) operation removes "orphaned" knowledge graph elements, i.e. nodes and edges that are not referenced by any result.

This example contains four messages:

1. The initial message is provided in [_01\_qgraph.json_](messages/01\_qgraph.json).
1. The result of the FILL operation applied to _01\_qgraph.json_ is provided in [_02\_results\_full.json_](messages/02\_results\_full.json).
1. The result of the FILTER RESULTS (TOP-N) operation applied to _02\_results\_full.json_ is provided in [_03\_filtered\_results\_top\_n.json_](messages/03\_filtered\_results\_top\_n.json). This example operation removes all except for the top result.
1. The result of the FILTER operation applied to _03\_filtered\_results\_top\_n.json_ is provided in [_04\_filtered\_kgraph\_orphans.json_](messages/04\_filtered\_kgraph\_orphans.json).
