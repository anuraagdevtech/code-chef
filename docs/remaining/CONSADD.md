# CONSADD

Eliminate each row from left to right with difference arrays, then eliminate the residual columns top to bottom.

Correctness: A leftmost residual entry can only be removed by the window beginning there after earlier coordinates are fixed. These window generators form an integer basis; after eliminating row and column generators, a nonzero remainder is an obstruction.

Complexity: O(R*C) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
