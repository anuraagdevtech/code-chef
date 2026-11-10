# CHINSM

Precompute divisors of x-K and maintain the latest index that can form a bad pair for each next value.

Correctness: For y>K, x mod y=K means x=K or y divides x-K. The latest violating predecessor moves the sliding-window left endpoint just past that index; every suffix beginning afterward is valid.

Complexity: O(V log V+N*tau(V)) time, O(V log V) divisor storage, V=max A.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
