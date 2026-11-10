# PRIMEFACDIV

Repeatedly divide B by gcd(A,B).

Correctness: Every common prime factor can be stripped until exhausted. A remaining value greater than one with gcd one contains a prime absent from A; reaching one proves every prime was present.

Complexity: O(log B) gcd calls, O(1) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
