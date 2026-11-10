# AWESUM_OR

Use inclusion-exclusion on assignments of each set bit of N to one of three numbers.

Correctness: OR equal to the sum implies no carries and exactly one owner for each set bit. There are 3^p assignments; excluding empty owners gives 3^p-3*2^p+3 for p>0.

Complexity: O(log N) modular exponentiation time, O(1) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
