# SSO

Count contributions to each bit and propagate half the count to the next bit, marking every nonempty bit.

Correctness: A present bit occurs in a singleton subset sum. Pairs of available contributions at one bit can carry to the next; continuing carries exposes exactly every bit that can occur in any subset sum. Bits absent from this process cannot be produced by any subset.

Complexity: O(N log max A) time, O(log sum A) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
