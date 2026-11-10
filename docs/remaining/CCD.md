# CCD

Build prefix sums of alternating character differences modulo 26.

Correctness: Successive adjacent-operation counts are forced by the first coordinate. Eliminating them from left to right leaves exactly the alternating sum at the last coordinate; it must vanish modulo 26 and that condition also constructs all required counts.

Complexity: O(N+Q) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
