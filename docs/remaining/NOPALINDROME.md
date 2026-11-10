# NOPALINDROME

Count ones and twos in repetitions of 1, K zeros, 2, floor((K-1)/2) zeros.

Correctness: Greedy lexicographic construction first permits K zeros, then forces a two; after that the centered-palindrome restriction allows exactly floor((K-1)/2) zeros before a one. This resets the same state, giving a periodic optimal word.

Complexity: O(1) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.

Official editorial reference: https://discuss.codechef.com/t/108255
