# MAXVAC

Count vacations in each zero run and evaluate the gain from joining each adjacent pair across one workday.

Correctness: Flipping a workday changes only its neighboring zero runs. The merged run has floor((left+right+1)/X) vacations, and all other runs retain their contribution.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
