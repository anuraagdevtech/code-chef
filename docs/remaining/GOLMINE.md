# GOLMINE

Sum G*B/(A+B) for Chef and the complementary shares for Chefu.

Correctness: A mine worked concurrently yields exactly these shares. The optimal-play equilibrium gives the same total allocation independently per mine; changing the shared processing order does not improve a miner’s guaranteed share.

Complexity: O(N) time, O(1) auxiliary space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.

Official editorial reference: https://discuss.codechef.com/t/69982
