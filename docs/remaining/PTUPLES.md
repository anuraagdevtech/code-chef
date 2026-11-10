# Prime Tuples (PTUPLES)

[Problem statement](https://www.codechef.com/problems/PTUPLES) · [Python solution](../../solutions/PTUPLES.py)

## Approach

Two odd primes sum to an even composite, so every tuple starts with two and ends with a twin-prime pair (p,p+2). Sieve to V=1000000 and prefix-count valid larger twin endpoints.

## Complexity

- Time: O(V log log V+T).
- Space: O(V).
