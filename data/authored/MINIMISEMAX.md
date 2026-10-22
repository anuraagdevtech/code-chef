---
topic: Greedy
subtopic: Two independent lower bounds that are jointly attainable
time: $O(1)$ per test case
space: $O(1)$
---
Two unavoidable costs bound the answer from below, and spreading the ones evenly meets both.

**The largest block.** The $Y$ copies of $-2$ cut the array into at most $Y+1$ maximal runs of ones, so some run holds at least $\lceil X/(Y+1) \rceil$ ones, and that run is itself a subarray.

**The whole array.** The full array is always a subarray, with sum $X - 2Y$ regardless of the order.

So the answer is at least $\max\bigl(\lceil \frac{X}{Y+1} \rceil,\; X - 2Y\bigr)$, and distributing the ones as evenly as possible — one $-2$ between consecutive runs — attains it. The reason is that taking $k$ consecutive runs yields roughly $kq - 2(k-1) = k(q-2) + 2$ where $q = \lfloor X/(Y+1) \rfloor$, which is **linear in $k$**: it is maximised at $k = 1$ or at $k = Y+1$, the two bounds above. No intermediate $k$ can beat them.

Clustering the $-2$s never helps, since it reduces the number of runs and so enlarges the biggest one.

$$\text{answer} = \max\!\left(\left\lceil \frac{X}{Y+1} \right\rceil,\; X - 2Y\right)$$

The samples land on each bound. $X = 5, Y = 1$ gives $\max(3, 3) = 3$, where the two bounds coincide — the arrangement $1\,1\,1\,{-2}\,1\,1$ has a block of three and a total of three. $X = 2, Y = 2$ gives $\max(1, -2) = 1$ via $1\,{-2}\,1\,{-2}$, and $X = 1$ with either $Y$ gives $1$, since a single $1$ is always a subarray.

The answer is never below $1$ because $X \geq 1$, so the empty-subarray convention never comes into play.

## Edge cases

- **Two independent lower bounds, and both are met at once.** The $Y$ copies of $-2$ cut the ones into at most $Y+1$ runs, so some run holds $\lceil X/(Y+1) \rceil$ ones; and the whole array is itself a subarray, with sum $X - 2Y$.
- **Either bound can dominate.** The third row is limited by the run length ($\lceil 5/2 \rceil = 3$ against a total of $3$ — a tie here), while the first and last are limited by the run length over a negative total.
- **A negative total is fine.** When $X < 2Y$ the whole-array bound is negative and irrelevant, and the answer is just the longest run of ones.
- **Spreading the ones as evenly as possible attains both bounds simultaneously**, which is why the maximum of the two is exact rather than merely a bound.
- **$Y + 1$, not $Y$, is the divisor** — the $-2$s create one more gap than their own count, including the positions before the first and after the last.
- **The answer is always at least $1$**, since $X \geq 1$ guarantees a positive element somewhere.
- **$X, Y$ up to $10^6$** with constant work per case.

## Dry run

| $X$ | $Y$ | longest run $\lceil X/(Y{+}1) \rceil$ | whole array $X - 2Y$ | answer | a witnessing layout |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | $-1$ | `1` | $-2, 1$ |
| 1 | 3 | 1 | $-5$ | `1` | $-2, 1, -2, -2$ |
| 5 | 1 | 3 | 3 | `3` | $1,1,-2,1,1,1$ |
| 2 | 2 | 1 | $-2$ | `1` | $1, -2, 1, -2$ |
