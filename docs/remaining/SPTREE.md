# SPTREE

Give every special source u initial weight d(a,u). Propagating a candidate across one edge subtracts one, so its value at b is exactly d(a,u)-d(b,u). A postorder pass finds the best descendant source and a preorder pass imports the best source from above. Retain the source index with each best value.

Complexity: O(N+K) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
