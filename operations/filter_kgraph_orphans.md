# filter kgraph (orphans)

_subclass of [Filter kgraph](./filter_kgraph.md)_

This operation removes kgraph elements that are not referenced by any results.

### examples

- [input](../examples/fill_and_filter/messages/03_filtered_results_top_n.json), [output](../examples/fill_and_filter/messages/04_filtered_kgraph_orphans.json)

### input requirements

None

### output guarantees

Output will contain no kgraph elements that are not referenced by any results.

### allowed changes

- remove knodes
- remove kedges

### parameters

None
