# MEXYARR

Reserve each constrained mex until its last occurrence; greedily insert the smallest currently unreserved value and check constraints.

Correctness: A constrained mex cannot appear before its final constraint. Among currently legal values, inserting the smallest maximizes progress toward all future required mexes without violating any future forbidden value. If this maximal-progress construction misses a constraint, no valid construction can meet it.

Complexity: O(N log N) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
