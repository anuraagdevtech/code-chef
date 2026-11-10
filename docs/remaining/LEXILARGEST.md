# LEXILARGEST

For each prefix step choose the largest multiplier coprime to A_(i-1)/A_i.

Correctness: Writing B_i=A_i*t reduces the gcd condition to gcd(t,A_(i-1)/A_i)=1. A choice affects no future prefix gcd, so the greatest admissible value at every index gives the lexicographic optimum.

Complexity: O(N+sum of searched multiplier gaps times log M) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
