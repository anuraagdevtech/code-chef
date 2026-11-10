# MAJIK

Reserve the initial extrema and take the largest P+Q absolute values among the remaining elements.

Correctness: Either available operation can increase the separation by |x|: add/subtract x to the appropriate extreme. Each operation absorbs at most one additional original element; using the largest absolute contributions attains this upper bound.

Complexity: O(N log N) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.

Official editorial reference: https://discuss.codechef.com/t/113480
