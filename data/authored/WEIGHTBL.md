---
topic: Basic Math
subtopic: Reachable range over repeated choices
time: $O(1)$ per test case
space: $O(1)$
---
Over $M$ months Chef gains between $x_1$ and $x_2$ kilograms each month, and the monthly gains need not be equal. So the **total** gain can be anything from $M \cdot x_1$ to $M \cdot x_2$ — and, since the per-month values vary freely, every value in that range is attainable.

The scale is consistent with the science exactly when the observed gain lands inside:

$$M \cdot x_1 \leq w_2 - w_1 \leq M \cdot x_2$$

The step worth justifying is that the range has no gaps. With each month free to take any value in $[x_1, x_2]$, the achievable totals form a continuous interval rather than a scattered set — so a single two-sided comparison suffices and there is nothing to search over.

Both bounds are needed, and the samples prove it. Case 1 fails the **lower** bound: a gain of $1$ kg over two months is less than the minimum $2$, so the scale is reading too low. Case 5 fails the **upper** bound with a gain of $99$ against a maximum of $4$. Dropping either comparison passes one of these wrongly.

Cases 2 through 4 land on and inside the range — case 2 exactly on the minimum and case 3 exactly on the maximum — confirming both ends are inclusive.

Note that $x_1$ may be $0$, so a gain of zero can be legitimate; but $w_1 < w_2$ is guaranteed, so the observed gain is always at least $1$.

## Edge cases

- **Below the minimum** (the first row: a gain of $1$ against a required $2 \times 1 = 2$): `0`.
- **Above the maximum** (the last row: a gain of $99$ against a ceiling of $2 \times 2 = 4$): `0`.
- **Exactly on either bound**: the second row sits on the lower bound and the third on the upper, and both answer `1` — so both comparisons are non-strict, and the sample covers each.
- **$x_1 = x_2$**: the range collapses to a single value and the gain must match it exactly.
- **$x_1$ may be $0$**, which makes the lower bound $0$ and admits any gain up to $m x_2$.
- Monthly gains vary freely within $[x_1, x_2]$, so **every** integer total in $[m x_1, m x_2]$ is reachable — that is why a plain range test suffices and no divisibility condition is needed.

## Dry run

| $w_1$ | $w_2$ | gain | $x_1$ | $x_2$ | $M$ | range $[Mx_1, Mx_2]$ | inside? | output |
|---:|---:|---:|---:|---:|---:|---|:---:|---|
| 1 | 2 | 1 | 1 | 2 | 2 | $[2,4]$ | no | `0` |
| 2 | 4 | 2 | 1 | 2 | 2 | $[2,4]$ | yes (lower) | `1` |
| 4 | 8 | 4 | 1 | 2 | 2 | $[2,4]$ | yes (upper) | `1` |
| 5 | 8 | 3 | 1 | 2 | 2 | $[2,4]$ | yes | `1` |
| 1 | 100 | 99 | 1 | 2 | 2 | $[2,4]$ | no | `0` |
