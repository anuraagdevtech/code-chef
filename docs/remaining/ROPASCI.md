# ROPASCI

Scan right to left, composing the three possible winner states through each move.

Correctness: A suffix acts as a function on an incoming R/P/S winner. Prepending one duel composes its transition with this function; evaluating the current move gives the suffix tournament winner.

Complexity: O(N) time, O(N) output space and O(1) state.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
