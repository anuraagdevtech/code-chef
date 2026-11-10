# CHEFSHOPPING

Sum min(R_i,L_(i+1)) over original adjacent boundaries.

Correctness: Every original boundary must be crossed once by a removal; its cheapest possible direction gives the lower bound. Orienting each boundary toward that chosen remover admits a valid elimination order, with each ingredient using each direction at most once, attaining the bound.

Complexity: O(N) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.

Official editorial reference: https://discuss.codechef.com/t/121461
