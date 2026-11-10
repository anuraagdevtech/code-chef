# SPOOKYSEQ

Friendship components impose independent sorted-strength orders. Their positions can be interleaved in N!/product(size!) ways, while equal-strength vertices within each component can permute freely. Multiply by each equal-strength group’s factorial.

Complexity: O((N+M) alpha(N)) time after factorial preprocessing and O(N+M) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
