# GCD_QUERIES

Create a min heap of sorted-array indices for each prime divisor. An element has gcd greater than one with X exactly when it shares one of X’s prime factors. Query the smallest live index across those heaps, lazily deleting removed indices; fall back to the global first live index.

Complexity: O(V log log V+(N+Q) log V log N) time and O(V+N log V) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
