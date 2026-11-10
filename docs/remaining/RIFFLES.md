# RIFFLES

In zero-based indexing, each output position i reads old position 2i modulo N-1, with the final position fixed. Compose K times to obtain multiplication by 2^K modulo N-1.

Complexity: O(N+log K) time and O(N) output space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
