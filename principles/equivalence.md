# Equivalence

The following defines when TRAPI components should be considered equivalent.

* **query graph nodes** - when keys and values are identical
* **query graph edges** - when keys and values are identical
* **knowledge graph nodes** - when keys are equivalent per node-norm
* **knowledge graph edges** - when subjects, predicates, objects, and original_knowledge_source are identical
* **results** - when node bindings and edge bindings are identical, after accounting for knowledge graph element equivalence

If we consider the *graph nodes/edges as lists of key-value pairs, set operations including union, intersection, and difference should be well defined.
