# Merging messages

The following assumes that we are merging exactly two messages together. To merge more than two, successively merge pairs. The merge operation should be associative and commutative.

After pre-processing, the `query_graph`, `knowledge_graph`, and `results` from the messages should be merged independently.

## Pre-processing

* Each knowledge graph and associated bindings should be normalized to use a shared set of preferred identifiers.
* All `name` properties should be removed.

## Query graph

The query graph `nodes` and `edges` should be merged independently.

Query graph nodes should be merged if and only if their keys _and_ values are identical. Identical keys with different values should result in an error.

Query graph edges should be merged if and only if their keys _and_ values are identical. Identical keys with different values should result in an error.

## Knowledge graph

The normalized knowledge graph `nodes` and `edges` should be merged independently.

Knowledge graph nodes should be merged if and only if their keys are identical.

Knowledge graph edges should be merged if and only if they share a `subject`, `predicate`, `object`, and `relation`. If `relation` is provided for one edge and omitted by the other, they should not be merged.

### Knowledge graph nodes

Knowledge graph node values should be merged by:

* finding the union of their `categories` lists
* concatenating their `attributes` lists

### Knowledge graph edges

Knowledge graph edge values should be merged by:

* concatenating their `attributes` lists

## Results

Results should be concatenated.
