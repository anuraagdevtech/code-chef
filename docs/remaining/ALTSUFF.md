# ALTSUFF

Compute the string after one step, then use distances to its nearest set bit and time parity.

Correctness: After the first step each run of ones has length at most two and each set bit has a zero neighbor. Subsequent fronts advance one position per step and visited positions alternate; meeting fronts have compatible parity or form a two-cell boundary.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
