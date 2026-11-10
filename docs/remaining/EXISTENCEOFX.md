# EXISTENCEOFX

Process addition from low bits upward. The required sum bit uniquely determines the corresponding bit of X from the three input bits and carry. Once all input bits are zero, an outstanding carry can never disappear; otherwise the finite constructed X works.

Complexity: O(log(max(A,B,C)+1)) time and O(1) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
