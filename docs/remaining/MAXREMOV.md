# MAXREMOV

Compute all coverage heights and a prefix sum scoring +1 at height K+1 and -1 at height K.

Correctness: Removing an interval creates a height-K cake exactly at previous height K+1, and destroys one exactly at previous height K. Its net gain is the interval sum of those scores.

Complexity: O(N+C) time and space, C=100000.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
