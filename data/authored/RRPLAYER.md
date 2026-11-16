---
topic: Probability
subtopic: Coupon collector - a sum of geometric waiting times
time: $O(\max N + T)$
space: $O(\max N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
This is the coupon collector problem. Once $k$ distinct songs have been heard, each new play is an unheard song with probability $(N - k) / N$, so the expected number of plays until the next new song is $N / (N - k)$.

By linearity of expectation the total is

$$\sum_{k=0}^{N-1} \frac{N}{N-k} = N \cdot H_N,$$

with $H_N$ the $N$-th harmonic number. Precompute the harmonic numbers up to the largest query.

## Edge cases

- $N = 1$: the first song finishes the album, answer 1.
- The first play is always new - the $k = 0$ term is exactly 1.
- Floating-point harmonic sums are accurate far beyond the required tolerance for the given limits.
- All queries share one prefix table.

## Dry run

`N = 3`: waiting times $3/3 + 3/2 + 3/1 = 1 + 1.5 + 3 = 5.5$.

`N = 2`: $2/2 + 2/1 = 3$.
