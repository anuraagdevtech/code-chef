# ABROADS

Undo queries offline: deleted roads become additions, handled by disjoint sets, and population updates are restored using their recorded old values. Maintain component populations in a max heap with lazy invalidation by root and current sum. Read the maximum before undoing each query.

Complexity: O((N+M+Q) log(N+M+Q)) time and O(N+M+Q) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
