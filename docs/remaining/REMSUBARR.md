# REMSUBARR

Add positions of values N,N-1,... and track their minimum and maximum.

Correctness: The removed elements must be exactly a suffix of the value set; these values form a removable subarray precisely when their positional span equals their count.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
