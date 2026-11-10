# ELWINTER

Maintain a heap of newly frozen vertices with their freeze times; expand events only when time advances.

Correctness: An event at t freezes unvisited neighbors at t+1. Processing events chronologically reproduces the spreading rule, and each vertex and edge is expanded at most once.

Complexity: O((N+M) log N + Q) time, O(N+M) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
