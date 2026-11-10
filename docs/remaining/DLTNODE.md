# DLTNODE

Compute subtree gcds and reroot outside-subtree gcds using prefix/suffix gcds of children.

Correctness: Deleting a node produces its child subtrees and the complementary parent component. Their cached gcds give the exact damage, and prefix/suffix exclusion computes each child complement without quadratic scans.

Complexity: O(N log max A) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
