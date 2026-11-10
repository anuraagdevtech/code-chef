# SYMARRSWAP

Sort both choices tagged by index and find the smallest sliding window covering all indices.

Correctness: Any selected array lies in an interval containing an option for each index. Conversely any such interval yields a valid selection, so the minimum covering interval is exactly the optimum range.

Complexity: O(N log N) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
