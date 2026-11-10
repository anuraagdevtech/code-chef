# PARPERM

Select isolated values one and primes greater than N/2, or their complement.

Correctness: All other values belong to one gcd-connected component: primes at most N/2 connect to two through twice the prime, and composites connect through their factors. A valid partition cannot split a component. Isolated singleton components therefore characterize all feasible smaller sides.

Complexity: O(N log log N) sieve preprocessing, O(N) per case, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
