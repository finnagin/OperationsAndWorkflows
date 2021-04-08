# Overlay example

The OVERLAY operation accepts (a message with) a query graph and returns (a message with) a query graph with at least one additional query graph edge. It also may (but is not garuenteed to) add aditional knowledge graph edges.

This example contains two messages:

1. An initial example of a message contianing a query graph, knowledge graph and results is provided in [_07\_input\_ngd.json_](messages/07\_input\_ngd.json).
2. The output of the overlay(compute ngd) operation applied to _07\_input\_ngd.json_ is provided in [_08\_output\_ngd.json _](messages/08\_output\_ngd.json). This example adds an additional query graph edge as well as two aditional knowledge graph edges containing normalized google distance values linking pairs of nodes.
