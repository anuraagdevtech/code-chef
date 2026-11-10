# Levy Conjecture (LEVY)

[Problem statement](https://www.codechef.com/problems/LEVY) · [Python solution](../../solutions/LEVY.py)

## Approach

Sieve primes through V=10000 and enumerate all ordered prime pairs (p,q) with p+2q<=V. Store the number of representations for every sum, then answer queries directly.

## Complexity

- Time: O(V log log V+pi(V) squared+T).
- Space: O(V).
