# REDGREEN

Count contributions path by path. There are C(N+M-2,N-1) paths; each visits N+M-1 cells and is balanced in C(length,length/2) colorings, with all other cells freely colored. An odd path length cannot balance.

Complexity: O(N+M) preprocessing, O(log(NM)) time per case and O(N+M) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
