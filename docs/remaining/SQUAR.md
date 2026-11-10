# SQUAR

Replace each number by its squarefree kernel. Every pair has square product exactly when their kernels agree, and each singleton must be nonsquare. Therefore a valid subsequence consists entirely of one nontrivial kernel, and any such subsequence works for all even and odd lengths. Count the most common kernel.

Complexity: O(V log log V+N log V) time and O(V+N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
