# MAXIMALEXP

Consider residue sums N mod K and N mod K+K and choose their balanced split.

Correctness: The two residues sum to one of these values. For a fixed feasible sum their product is maximal when balanced; evaluating the resulting X candidates includes an optimum.

Complexity: O(1) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
