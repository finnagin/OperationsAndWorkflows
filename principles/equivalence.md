# Equivalence

The following defines when TRAPI components should be considered equivalent.

* **query graph nodes** - when keys are identical and values are equivalent
  * predicates - when (unordered) lists are identical _after_ removing any predicates whose ancestors are present
* **query graph edges** - when keys are identical and values are equivalent
  * ids - when (unordered) lists are identical _after_ removing any ids whose ancestors are present and accounting for equivalence per node-norm
  * categories - when (unordered) lists are identical _after_ removing any categories whose ancestors are present
* **knowledge graph nodes** - when keys are equivalent per node-norm
* **knowledge graph edges** - when subjects, predicates, objects, and original_knowledge_source are identical (any edge without original_knowledge_source is never equivalent)
* **results** - when node bindings and edge bindings are identical, after accounting for knowledge graph element equivalence

If we consider the *graph nodes/edges as sets of key-value pairs, set operations including union, intersection, and difference should be well defined.
