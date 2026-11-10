# TRPTSTIC

Build 2D prefix sums and binary-search the Chebyshev radius, trying positive-capacity mentor rooms.

Correctness: A radius includes a clipped square around its center, so the summed capacity criterion is exactly at least K+1. Feasibility is monotone in radius; zero-capacity rooms cannot host the mentor.

Complexity: O(N*M log max(N,M)) time, O(N*M) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
