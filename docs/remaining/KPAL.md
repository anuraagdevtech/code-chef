# KPAL

For K=N require the original palindrome. Otherwise only even N/even K with odd total is impossible.

Correctness: When all indices increment, mirrored differences stay fixed. With K<N, operation-vector differences can transfer a unit between any two coordinates; adding a sufficiently large common baseline makes a feasible transfer nonnegative. The only surviving obstruction is parity of the total when both N and K are even.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
