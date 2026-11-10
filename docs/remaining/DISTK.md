# DISTK

Spend K-N extra contributions on an initial distinct prefix, then one partial repeat and a constant tail.

Correctness: A distinct prefix of length L contributes 1+...+L good subarrays. Repeating the element r positions before its end adds r+1; each subsequent identical value adds one. The greedy remainder lies in the required range.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
