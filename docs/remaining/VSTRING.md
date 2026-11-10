# VSTRING

Count circular gaps between consecutive ones that exceed C; allow at most one.

Correctness: A rotation can cut one circular gap so it no longer lies between adjacent ones in the linear string. Every other gap remains constrained. With fewer than two ones the condition is vacuous.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
