# SUMARRAY

Start with N/2 ones and N/2 twos and distribute remaining sum in increments of two.

Correctness: Parity is fixed by the required number of odd entries. The baseline and maximal same-parity values give necessary bounds, and any even difference inside those bounds can be distributed without exceeding a per-entry capacity.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
