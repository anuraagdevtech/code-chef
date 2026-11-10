# RECHEND

Scan connected diagonal runs of blocked cells and test whether any touches both separating boundary arcs.

Correctness: In the grid, an eight-connected blocked chain from the top/right arc to the bottom/left arc prevents any monotone route. With one block per row and column its components are exactly consecutive rows with columns differing by one. If none separates the endpoints a monotone free path exists.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
