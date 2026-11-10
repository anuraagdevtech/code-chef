# Prime Game (PRIGAME)

[Problem statement](https://www.codechef.com/problems/PRIGAME) · [Python solution](../../solutions/PRIGAME.py)

## Approach

The game's criterion is whether the number of distinct primes in X! is at most Y, equivalently pi(X)<=Y. Sieve and prefix-count primes through V=1000000, then answer each case in constant time.

## Complexity

- Time: O(V log log V+T).
- Space: O(V).
