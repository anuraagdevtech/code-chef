# Churu and Balls (CBALLS)

[Problem statement](https://www.codechef.com/problems/CBALLS) · [Python solution](../../solutions/CBALLS.py)

## Approach

First replace every bucket count by its prefix maximum, the unavoidable nondecreasing lower bound. For a fixed prime divisor p, round each such value up to a multiple of p. Some prime divides every valid common divisor, so minimizing these costs over primes through the first prime at least V is exhaustive.

## Complexity

- Time: O(N+pi(V) V).
- Space: O(V).
