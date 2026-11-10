# MUSROD

Sort rods by increasing B/A using exact cross products.

Correctness: Placing x before y contributes A_x*B_y between this pair, versus A_y*B_x in reverse. Sorting by the indicated ratio makes every pair contribute its larger possible value.

Complexity: O(N log N) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
