# PALIXOR

Count frequencies and sum over decimal palindrome XOR values; use a Walsh-Hadamard convolution for large supports.

Correctness: The convolution counts ordered pairs with each XOR. Non-diagonal valid pairs occur twice and the N diagonal pairs once, so (ordered+N)/2 is required.

Complexity: O(min(D*P,U log U)) time; O(U) space, U=32768, P palindrome count, D distinct values.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
