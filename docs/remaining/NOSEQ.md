# NOSEQ

Extract signed base-K digits using remainders 0,1,K-1.

Correctness: For K>2 the least digit is forced by the residue; dividing the remaining value by K preserves the equation. Base two ordinary binary suffices whenever the target lies in the achievable signed range. A nonzero remainder after N digits is impossible.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
