# MINIMUMOP

Return zero for equal arrays, the common gcd if greater than one, otherwise an unused prime or operations two and three.

Correctness: If gcd(A)=1 a one-operation solution must make every value one. A prime factor of its X must therefore divide none of the inputs, and such a prime itself suffices. If none exists, two and three force every value to one and two moves are necessary.

Complexity: O(Mmax log log Mmax) preprocessing; O(N log max A) factoring per case, O(Mmax+N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
