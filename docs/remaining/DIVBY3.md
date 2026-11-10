# DIVBY3

Track ones on even positions modulo three; return zero, one allowed swap, two disjoint opposite swaps, or three, after checking parity-slot capacity.

Correctness: Divisibility is equivalent to twice the even-position count minus total ones being zero modulo three. Every adjacent unequal swap changes that count by one. A desired-direction boundary gives one move; otherwise two disjoint reverse boundaries give two. If neither exists but the count is feasible, moving a boundary through a neighboring run gives a three-move adjustment.

Complexity: O(N) time, O(1) auxiliary space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
