# TRAVELLING

Run 0-1 BFS with original edges of weight zero and neighboring labels of weight one.

Correctness: Any edge spanning d labels costs d squared; replacing it by d unit edges costs d, no more. Thus unit edges together with free original edges preserve the optimum.

Complexity: O(N+M) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
