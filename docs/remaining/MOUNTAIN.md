# MOUNTAIN

Choose the shortest row prefix whose full capacity covers S, assign one cell per row, then greedily allocate extra cells from the largest row downward.

Correctness: The minimum prefix length has triangular base sum at most S. Coins 1,...,K each available M-1 times represent every total through their combined sum; descending greedy succeeds since consecutive smaller denominations cover every remainder.

Complexity: O(N) time and space per query.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
