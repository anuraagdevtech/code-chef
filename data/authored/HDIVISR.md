---
topic: Brute Force
subtopic: Searching a small range downward
time: $O(1)$ — at most 10 divisibility tests
space: $O(1)$
---
Find the largest $d$ in $[1, 10]$ dividing $N$. The search space has ten elements, so simply try them from $10$ downward and return the first that divides:

```python
next(d for d in range(10, 0, -1) if n % d == 0)
```

Counting **down** is what makes this correct with an early exit — the first hit is already the largest. Counting up would require scanning all ten and remembering the best, which is no slower here but is the version that invites an off-by-one.

The search can never fail, because $d = 1$ divides every integer. So no fallback or sentinel is needed, and `next` is safe without a default.

It is worth noticing that this is *not* the same as "the largest proper divisor capped at 10", nor does it have anything to do with the greatest common divisor of $N$ with anything. Sample case $N = 91 = 7 \times 13$ answers $7$: the divisors of $91$ are $1, 7, 13, 91$, and $7$ is the largest that fits inside the range.

For a range this small, brute force is not a compromise — it is the right answer. Factorising $N$ first would be more work for no benefit, and would still need a pass to pick the largest factor under $10$.

There is **no $T$**: the input is a single integer.

## Edge cases

- **$d = 1$ always divides**, so the search can never come up empty — a prime above $10$ such as $11$ or $13$ returns $1$.
- **Counting downward is essential.** The first divisor found is then the largest; iterating $1$ upward and returning the first hit would answer $1$ for every input.
- **$N = 10$**: the answer is $10$, the top of the search range.
- **$N = 2$** (the minimum): $2$.
- The range is fixed at $1 \ldots 10$ regardless of $N$, so this is a constant-time search of at most ten tests.

## Dry run

Sample 1, $N = 91$, counting down:

| $d$ | 10 | 9 | 8 | 7 |
|---:|---:|---:|---:|---:|
| $91 \bmod d$ | 1 | 1 | 3 | **0** |

The first zero is at $d = 7$, so the output is `7`. Sample 2, $N = 24$, stops earlier: $10$ and $9$ fail, $8$ divides, so `8`.
