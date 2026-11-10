# CENS20A

Mark rectangle corners in an XOR difference matrix and take its 2D prefix XOR.

Correctness: Each four-corner update contributes one exactly inside its rectangle. XOR superposes all flips; taking the prefix recovers the final flip parity at every cell.

Complexity: O(N*M+Q) time, O(N*M) space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
