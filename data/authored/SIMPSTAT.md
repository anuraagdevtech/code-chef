---
topic: Sorting
subtopic: Trimmed mean
time: $O(N \log N)$ per test case
space: $O(N)$
---
Sort the measurements, discard the first $K$ and the last $K$, and average what remains. In Python the trimmed slice is `a[k:n-k]`, and the mean is its sum over its length.

This is the **trimmed mean**, a standard robust statistic: dropping the extremes keeps a few wild readings from dragging the average around. Sample cases 1 and 2 show the effect on the same data — with $K = 1$ the mean is $4$, but with $K = 0$ the outlier $25$ pulls it to $5.4$.

The constraint $2K < N$ guarantees at least one measurement survives, so the division never hits zero. That is worth noticing, since $K$ can be large relative to $N$: sample case 3 trims $[1,1,1]$ down to a single value.

Two practical points. Measurements may be **negative** (down to $-10^6$), so the sum can be negative and no clamping is appropriate. And the output must carry enough precision — printing with six decimal places via an f-string comfortably satisfies the stated tolerance of $10^{-6}$ absolute or relative error.

Doing the sum in integers and dividing once at the end keeps the arithmetic exact up to the final division, which avoids accumulating floating-point drift across up to $10^4$ additions.

## Edge cases

- **$K = 0$ trims nothing** (the second row): the slice must be `a[0:n]`, so writing the bounds as `a[k:n-k]` rather than special-casing zero is what keeps this correct.
- **$2K < N$ is guaranteed**, so the kept slice always holds at least one element and the division is never by zero.
- **Negative values must sort numerically.** The $-10$ in the first two rows is trimmed at $K = 1$ but counted at $K = 0$; sorting the raw byte tokens would place `-10` by its leading `-` instead of its value.
- **Summing in integers and dividing once** keeps the result exact until the final division, avoiding the drift of a running float average.
- **Equal values trimmed from both ends** (the third row, all ones): the answer is still exact, and six decimal places are required in the output.

## Dry run

First sample: $N = 5$, $K = 1$, values $2, 9, -10, 25, 1$.

| step | result |
|---|---|
| sorted | $-10, 1, 2, 9, 25$ |
| trim $K=1$ from each end | drop $-10$ and $25$ |
| kept | $1, 2, 9$ |
| sum / count | $12 / 3$ |
| output | `4.000000` |

With $K = 0$ the same values give $27 / 5 = $ `5.400000`, as in the second row.
