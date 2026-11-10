# GSEQ

Map each boundary to the prefix sum of +1 for one and -1 for zero. A good sequence is exactly an increasing-index chain of prefix values rising by one at each step. Maintain the best chain ending at every prefix value, plus predecessor pointers to reconstruct a longest chain.

Complexity: O(N) expected time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
