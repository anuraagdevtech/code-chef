# ADMIT

Process students by exam rank. Each takes the available college of minimum college rank among their choices. This is the admission rule itself; stop when Chef is processed since later students cannot change his assignment.

Complexity: O(M log M + total preferences) time and O(N+M+total preferences) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
