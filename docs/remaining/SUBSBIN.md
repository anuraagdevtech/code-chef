# SUBSBIN

If both bits occur, repeatedly replace an unequal adjacent pair by the minority bit until balanced, then replace the whole string.

Correctness: Every operation changes the global zero-minus-one difference by exactly one. Before the final operation the difference must be zero, requiring at least its original absolute value prior operations. The adjacent-pair construction achieves that bound. Uniform strings admit no move.

Complexity: O(N^2) time from string edits/searches, O(N) space; N<=1000.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
