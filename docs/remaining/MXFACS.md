# MXFACS

Factor N and choose the smallest prime whose exponent is largest.

Correctness: Removing a composite factor loses at least as many divisors as removing one of its prime factors. Removing one copy of a prime of exponent e multiplies the divisor count by e/(e+1), maximized by the largest e.

Complexity: O(sqrt(N)) time, O(1) auxiliary space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
