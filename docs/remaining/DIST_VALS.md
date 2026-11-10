# DIST_VALS

A largest and second-largest pair in a subarray must be visible across elements no larger than the smaller endpoint. A decreasing monotone stack enumerates exactly these pairs, including equal endpoints; collect their differences. Every enumerated pair has a witnessing interval.

Complexity: O(N) expected time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
