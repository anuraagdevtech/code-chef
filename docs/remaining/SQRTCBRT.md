# SQRTCBRT

Find the least fixed point j=X+floor(cuberoot(j squared)) by increasing iteration, then return j squared.

Correctness: The first attainment of F is at a square. At that square F=j-floor(cuberoot(j squared)); its sequence in j is nondecreasing. Iteration from X never passes any feasible j and stabilizes at the smallest one.

Complexity: O(log X) fixed-point iterations (in practice a handful), O(1) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
