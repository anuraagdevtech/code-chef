# SIMPLEARRAY

Group elements by remainder. Remainder 0 and K/2 allow at most one chosen index. For every other complementary pair, choose any subset from either side, subtracting the double-counted empty choice. Different groups are independent.

Complexity: O(N+K) time and O(K) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
