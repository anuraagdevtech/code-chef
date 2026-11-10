# MERGEBS

A merge state is the number of consumed characters of each string. Appending one costs zero; appending zero costs the number of previously consumed ones, which depends only on the state. Dynamic programming over the two prefix lengths yields the minimum.

Complexity: O(N^2) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
