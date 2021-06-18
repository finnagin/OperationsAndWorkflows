# Merging messages

The following assumes that we are merging exactly two messages together. To merge more than two, successively merge pairs. The merge operation should be associative and commutative.

After pre-processing, the `query_graph`, `knowledge_graph`, and `results` from the messages should be merged independently.

## Pre-processing

* Each knowledge graph node key, knowledge graph edge endpoint, query graph node id, and node binding should be normalized to use a shared set of preferred identifiers.
* Any superfluous predicates, categories, and ids should be removed (those whose ancestor is also present)
* All `name` properties should be removed.

## Query graph

The query graph `nodes` and `edges` should be merged independently.

Query graph nodes should be merged if and only if they are equivalent. Identical keys with inconsistent values should result in an error.

Query graph edges should be merged if and only if they are equivalent. Identical keys with inconsistent values should result in an error.

## Knowledge graph

The normalized knowledge graph `nodes` and `edges` should be merged independently.

Knowledge graph nodes should be merged if and only if they are equivalent.

Knowledge graph edges should be merged if and only if they are equivalent.

### Knowledge graph nodes

Knowledge graph node values should be merged by:

* finding the union of their `categories` lists
* finding the union of their `attributes` lists

### Knowledge graph edges

Knowledge graph edge values should be merged by:

* finding the union of their `attributes` lists

## Results

Results should be merged if and only if they are equivalent. Two equivalent results should be merged by:

* extracting all key-value pairs aside from node_bindings and edge_bindings into separate objects
* using these objects as values in a `metadata` field, keyed by the corresponding source

For example,
```json
{
    "node_bindings": {"n0": [{"id": "MONDO:xxx"}]},
    "edge_bindings": {},
    "score": 1.0
}
```
and
```json
{
    "node_bindings": {"n0": [{"id": "MONDO:xxx"}]},
    "edge_bindings": {},
    "score": 0.5,
    "description": "This is interesting!"
}
```
will be merged into
```json
{
    "node_bindings": {"n0": [{"id": "MONDO:xxx"}]},
    "edge_bindings": {},
    "metadata": {
        "a": {
            "score": 1.0
        },
        "b": {
            "score": 0.5,
            "description": "This is interesting!"
        }
    }
}
```
