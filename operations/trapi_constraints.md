# TRAPI Message Constraints

Beyond the constraints described by the TRAPI OpenAPI schema, we wish to selectively enforce some additional constraints on specific operations.

* "no orphaned edges" - The `subject` and `object` for all qedges and kedges MUST map to qnode and knode keys, respectively.

  ```python
  for qedge in message["query_graph"]["edges"]:
      assert qedge["subject"] in message["query_graph"]["nodes"]
      assert qedge["object"] in message["query_graph"]["nodes"]
  for kedge in message["knowledge_graph"]["edges"]:
      assert kedge["subject"] in message["knowledge_graph"]["nodes"]
      assert kedge["object"] in message["knowledge_graph"]["nodes"]
  ```

* "no orphaned bindings" - Each binding MUST map a knode or kedge key to a qnode or qedge key, respectively.

  ```python
  for result in message["results"]:
      for qnode_id, bindings in result["node_bindings"]:
          assert qnode_id in message["query_graph"]["nodes"]
          for binding in bindings:
              assert binding["id"] in message["knowledge_graph"]["nodes"]
      for qedge_id, bindings in result["edge_bindings"]:
          assert qedge_id in message["query_graph"]["edges"]
          for binding in bindings:
              assert binding["id"] in message["knowledge_graph"]["edges"]
  ```

* "unique query graph ids" - All qnode and qedge keys MUST be unique.

  ```python
  qelement_ids = list(message["query_graph"]["nodes"]) + list(message["query_graph"]["edges"])
  assert len(qelement_ids) == len(set(qelement_ids))
  ```

* "unique knowledge graph ids" - All knode and kedge keys MUST be unique.

  ```python
  kelement_ids = list(message["knowledge_graph"]["nodes"]) + list(message["knowledge_graph"]["edges"])
  assert len(kelement_ids) == len(set(kelement_ids))
  ```

* "results complete" - All results MUST include bindings for every qgraph element.

  ```python
  for result in message["results"]:
      for qnode_id in message["query_graph"]["nodes"]:
          assert qnode_id in result["node_bindings"]
      for qedge_id in message["query_graph"]["edges"]:
          assert qedge_id in result["edge_bindings"]
  ```

* "no orphaned knowledge graph elements" - All knowledge graph nodes and edges MUST be referenced by at least one result binding.

  ```python
  bound_knodes = [
      binding["id"]
      for result in message["results"]
      for bindings in result["node_bindings"].values()
      for binding in bindings
  ]
  bound_kedges = [
      binding["id"]
      for result in message["results"]
      for bindings in result["edge_bindings"].values()
      for binding in bindings
  ]
  for knode_id in message["knowledge_graph"]["nodes"]:
      assert knode_id in bound_knodes
  for kedge_id in message["knowledge_graph"]["edges"]:
      assert kedge_id in bound_kedges
  ```

* "max X results" - There MUST be no more than X results.

  ```python
  assert len(message["results"]) <= X
  ```
