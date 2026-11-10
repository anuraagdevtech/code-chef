# BALSUFF

Construct from left to right while keeping the multiset of remaining characters balanced within K, including zero counts for the original alphabet. Removing a character is legal precisely if the resulting range is at most K. Every balanced nonempty vector admits such a removal (remove a maximum), so choosing the smallest legal character is lexicographically optimal.

Complexity: O(26N) time and O(N) output space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
