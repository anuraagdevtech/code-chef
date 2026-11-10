# Subarray XOR (SUB_XOR)

[Problem statement](https://www.codechef.com/problems/SUB_XOR) · [Python solution](../../solutions/SUB_XOR.py)

## Approach

For a fixed output bit, each source bit contributes once for every possible left endpoint. Only even zero-based source positions have odd multiplicity. Maintain their prefix XOR and read the resulting output bits from most to least significant, reducing modulo 998244353 with Horner's rule.

## Complexity

- Time: O(N).
- Space: O(N).
