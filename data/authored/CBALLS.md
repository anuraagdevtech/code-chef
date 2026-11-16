---
topic: Number Theory
subtopic: Try prime common divisors with bucketed rounding costs
time: $O(V\log\log V+N+V\sum_{p\le V+1}1/p+\pi(V+1))$ per test case
space: $O(N+V)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Fix a prime divisor $p$ for the final common GCD. The least feasible final value at position $i$ is the smallest multiple of $p$ at least the running maximum of the original values up to $i$. Rounding a nondecreasing running maximum preserves order and gives the minimal cost for this $p$.

Every GCD greater than one has a prime divisor, so trying primes suffices. Let $V$ be the maximum original value. Prime two gives every final value at most $V+1$, so primes larger than $V+1$ cannot improve the cost. Build a frequency prefix table of the running maxima. For a prime $p$, values in $((k-1)p,kp]$ round to $kp$; prefix counts sum each bucket in constant time. This avoids rescanning all $N$ entries for every prime.

## Edge cases

- Original order must be preserved.
- An already nondecreasing array may still need increments to give GCD greater than one.
- For an all-one array, changing every value to two is optimal.

## Dry run

For `[11,13,15]`, prime two rounds to `[12,14,16]`, requiring three additional balls. No candidate prime gives a smaller total.
