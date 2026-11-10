# INTARR

Sort and interleave reversed lower and upper halves for valleys; if needed try the opposite orientation.

Correctness: An interesting array must alternate strict peaks and valleys. Matching the smallest available low values with the largest high values maximizes every required separation; if both orientations fail, no strict alternating assignment can exist.

Complexity: O(N log N) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
