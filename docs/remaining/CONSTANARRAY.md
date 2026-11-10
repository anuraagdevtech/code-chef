# CONSTANARRAY

Partition B into blocks of M positions, each containing distinct values. At a position, emit A_i if unused in the current block, otherwise emit any unused value. A_i has then appeared in the current block, so its frequency is the maximum baseline+1, as required.

Complexity: O(N+M) expected time and O(M+N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
