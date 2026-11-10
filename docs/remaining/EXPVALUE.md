# EXPVALUE

Maintain the expected score and its second moment under each independent half-probability increment.

Correctness: For increment w*B with E[B]=E[B squared]=1/2, the new second moment is old second moment+w*old mean+w squared/2. Updating the mean by w/2 gives the recurrence.

Complexity: O(N) time and output space, O(1) state.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
