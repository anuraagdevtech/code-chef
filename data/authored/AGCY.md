---
topic: Prefix Sums
subtopic: Range updates of a linear function with two difference arrays
time: $O(N + Q)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A day with cities $L \dots R$ adds $i - L + 1$ statues to city $i$ for every $i$ in the range, which is the linear function $1 \cdot i + (1 - L)$.

Keep two difference arrays, one for the coefficient of $i$ and one for the constant term. A query adds 1 to the slope and $1 - L$ to the intercept on $[L, R]$, i.e. it touches four cells. After all queries a prefix sum over both arrays gives, for every city, the total slope $s_i$ and intercept $c_i$ of the ranges covering it, and the answer for the city is $s_i \cdot i + c_i$.

## Edge cases

- A range of one city ($L = R$) destroys a single statue.
- The totals grow like $Q \cdot N$ and exceed 32 bits.
- The difference arrays need one extra cell for the update at $R + 1$.
- Cities not covered by any day print 0.

## Dry run

`N = 5`, days `[1,3] [1,2] [4,5]`.

Slope after prefix sums: `2 2 1 1 1`. Intercept: days 1 and 2 add 0 each, day 3 adds $1 - 4 = -3$ on cities 4-5: `0 0 0 -3 -3`.

Totals: $2 \cdot 1 = 2$, $2 \cdot 2 = 4$, $1 \cdot 3 = 3$, $4 - 3 = 1$, $5 - 3 = 2$.

Output `2 4 3 1 2`.
