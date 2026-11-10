# BURGER

For each possible number k of streaks, test whether Y/X+k has exactly k set bits and no bit zero.

Correctness: A streak of length a contributes 2^a-1 units. Distinct lengths correspond exactly to distinct positive set-bit positions in Y/X+k. Their sum plus k-1 breaks determines the time. The positive streak weights 2^a-1 are superincreasing (each exceeds the sum of all smaller weights), so the representing subset, if it exists, is unique.

Complexity: O(log^2(Y/X)) time, O(1) auxiliary space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
