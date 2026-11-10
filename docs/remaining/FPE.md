# FPE

Compute subtree gcds, then a bottom-up DP selecting which child continues the removed root path.

Correctness: Deleting a node exposes all child subtrees. Continuing through child v replaces its gcd contribution with that child’s optimal continuation value; at most one child continues the path.

Complexity: O(N log max A) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
