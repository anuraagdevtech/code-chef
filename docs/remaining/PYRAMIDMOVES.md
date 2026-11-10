# PYRAMIDMOVES

Recover row and column by integer square root and choose which downward steps go right.

Correctness: Over d row increases the column increases by exactly the number k of right steps. Reachability is 0<=k<=d, and choosing those steps gives binomial(d,k).

Complexity: O(sqrt(max label)) factorial preprocessing, O(1) per query, O(sqrt(max label)) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
