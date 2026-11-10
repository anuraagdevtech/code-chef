# MAX1S

Position i appears in i(N-i+1) substrings. Its flip gain is that weight for zero and its negation for one. The optimal single flip is the maximum sum contiguous segment of gains, found by Kadane’s algorithm, with zero allowed.

Complexity: O(N) time and O(1) extra space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
