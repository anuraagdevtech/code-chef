# DEQUEUE

The elements left unpopped form a middle subarray. Popped ends cover every value exactly when the middle contains strictly fewer than its total frequency for every value. A sliding window finds the longest valid middle, minimizing the number removed.

Complexity: O(N+M) time and O(N+M) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
