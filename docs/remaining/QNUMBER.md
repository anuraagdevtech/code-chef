# QNUMBER

Factor the fixed N once and answer queries from prime exponents.

Correctness: Common divisors are divisors of gcd(N,K). Divisors of N divisible by K exist only if K divides N and choose each exponent from the exponent in K through its exponent in N. Complementation gives type three.

Complexity: O(sqrt(N)+Q log K) time, O(log N) factor space plus output.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
