# COPAR

Factor each element with a smallest-prime-factor sieve and record each prime’s last occurrence. Scan a prefix while extending its required endpoint to cover every prime it contains. The first boundary with no prime crossing it is precisely the first coprime-product split.

Complexity: O(V log log V + N log V) time and O(V+N log V) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
