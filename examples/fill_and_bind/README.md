# FILL & BIND example

The FILL operation adds a knowledge graph.

The BIND operation accepts (a message with) a query graph and a knowledge graph, and returns (a message with) results binding the two.

The COMPLETE RESULTS operation accepts (a message with) results, and returns (a message with) only _complete_ results, i.e. ones where all query graph elements are bound.

This example contains four messages:

1. The initial message is provided in [_01\_qgraph.json_](messages/01\_qgraph.json).
1. The result of the FILL operation applied to _01\_qgraph.json_ is provided in [_02\_kgraph.json_](messages/02\_kgraph.json).
1. The result of the BIND operation applied to _02\_kgraph.json_ is provided in [_03\_partial\_results.json_](messages/03\_partial\_results.json).
1. The result of the COMPLETE RESULTS operation applied to _03\_partial\_results.json_ is provided in [_04\_complete\_results.json_](messages/04\_complete\_results.json).
