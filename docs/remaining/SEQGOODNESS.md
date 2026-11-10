# SEQGOODNESS

Maintain normalized binomial upper tails as the value threshold and cumulative frequency increase.

Correctness: Value v contributes when at least v selected values are at most v, but fewer than v are less than v. This is the difference of two binomial tails. Pascal’s identity updates a tail when adding an element; removing its boundary coefficient increases the threshold. Multiplying by 2^N converts probabilities to counts.

Complexity: O(N) time, O(max N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
