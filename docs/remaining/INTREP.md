# INTREP

For even N, N and 2N have identical prime support. For odd N choose the smallest odd prime p not dividing N: every odd prime factor of p-1 is smaller and already divides N. Thus pN adds precisely p to N’s prime support and (p-1)N adds precisely 2. Their difference is N. The product of odd primes through 47 exceeds 10^16, so p<=47 and both outputs are below 10^18.

Complexity: O(1) arithmetic operations and space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
