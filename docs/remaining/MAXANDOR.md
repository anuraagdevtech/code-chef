# MAXANDOR

Count bits where A and B differ and return two to that count.

Correctness: Each bit contributes independently to (B|X)-(A&X). Equal A/B bits force one choice of X for optimality; differing bits have equal contributions for both choices.

Complexity: O(C) bit complexity, O(1) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
