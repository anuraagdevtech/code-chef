# EQUIVALENT

Reduce each number to a primitive power base by dividing prime exponents by their gcd.

Correctness: Two positive powers agree exactly when their prime-exponent vectors are proportional. Dividing by the exponent gcd creates the unique primitive integer vector.

Complexity: O(sqrt(A)+sqrt(B)) time per uncached pair, O(number of cached values) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
