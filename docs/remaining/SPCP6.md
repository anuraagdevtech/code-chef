# SPCP6

DP by total cleared lines and whose turn it is; sum Chef-turn states within four lines of the finish.

Correctness: Moves two through four preserve turn and a move one changes it. Each valid winning sequence has a unique prefix totaling L-4 through L-1 with Chef to move, followed by four.

Complexity: O(max L+T) time and O(max L) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
