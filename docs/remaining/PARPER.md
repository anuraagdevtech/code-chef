# PARPER

Count odd values and assign uniform parity to each index-parity class.

Correctness: The condition concerns every pair across the two index classes. For K=0 every value must share parity (apart from N=1); for K=1 the two classes have opposite parity. Factorials count orderings within the classes.

Complexity: O(N) time per case with O(max N) factorial storage.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
