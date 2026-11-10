# AGCY

Use two difference arrays for the slope one and intercept 1-L of each range update.

Correctness: Each contribution at i is i+(1-L) while the interval is active. Prefix sums recover active slope and intercept, whose linear combination gives the total.

Complexity: O(N+Q) time, O(N) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
