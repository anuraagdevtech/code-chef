# CIRMERGE

Duplicate the circle and use interval merge DP with Knuth optimization, taking the best length-N interval.

Correctness: The final merge splits an interval into two independently merged intervals and adds its sum. Positive weights satisfy Knuth’s quadrangle and monotone inequalities, restricting split searches to neighboring optima. Every circular merge tree has a cut represented among the duplicated intervals.

Complexity: O(N^2) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
