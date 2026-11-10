# SUBARRAYXOR

Set A_i=i xor (i-1).

Correctness: Prefix XORs telescope to 0,1,...,N, which are distinct. Every subarray XOR is the XOR of two distinct prefixes, hence nonzero, and bounds are satisfied.

Complexity: O(N) time and output space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
