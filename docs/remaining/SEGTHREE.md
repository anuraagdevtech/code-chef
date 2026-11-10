# SEGTHREE

Try all nine choices for the first two residues and force the third; sum costs by index modulo three.

Correctness: Subtracting adjacent valid triple sums proves residues repeat every three positions. Each residue change costs its nonnegative difference modulo three, so enumerating all permitted patterns is exhaustive.

Complexity: O(N) time, O(1) auxiliary space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
