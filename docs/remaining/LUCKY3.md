# LUCKY3

For each possible result length use a multidimensional cumulative count at digit thresholds 3,4,6,7. Inclusion-exclusion applies F(4)-F(3)+F(7)-F(6) in every coordinate; F counts all nonempty subsets with digits bounded by the thresholds.

Complexity: O(D² 4^D + N D²) time and O(4^D) space, D<=9.
