---
topic: Arrays
subtopic: Feasibility by parity, then distance to the target count
time: $O(N)$ per test case
space: $O(1)$
---
The array holds only $+1$ and $-1$. If $p$ of them are $+1$ and $m$ are $-1$, the sum is $p - m$, so a sum of zero requires $p = m = N/2$.

**Feasibility first.** That is only possible when $N$ is even. For odd $N$ the sum of an odd number of odd values is odd and can never be zero, so the answer is $-1$ — sample case 2, with $N = 5$.

**Then the cost.** Each flip turns a $+1$ into a $-1$ or the reverse, changing $p$ by exactly one. Starting at $p$ and needing $N/2$, the minimum number of flips is

$$\left|\,p - \frac{N}{2}\,\right|$$

Every flip moves $p$ one step toward the target, and no flip moves it more, so this bound is both necessary and achievable — flip the surplus majority elements and stop.

The absolute value covers both directions: there may be too many $+1$s or too many $-1$s. Sample case 1 has $p = 4$ against a target of $2$, needing $2$ flips; sample case 3 has $p = 4$ against a target of $3$, needing $1$.

Sample case 4 is already balanced, giving $0$ — the formula handles it without a special case.

A neat equivalent is $|{\rm sum}|/2$, since the sum is $2p - N$; dividing the imbalance by two gives the same count, because each flip shifts the sum by $2$.

## Edge cases

- **Odd $N$** is impossible: a sum of an odd number of $\pm 1$ values is itself odd, so it can never reach $0$. The answer is $-1$, as in the sample's second case, and no amount of flipping helps.
- **Already balanced** ($[1, -1]$): zero flips, so the answer can legitimately be $0$.
- **All $+1$** ($[1,1,1,1]$): $N/2$ flips, the worst case for a given $N$.
- **Too many $-1$ instead**: the absolute value covers both directions, since flips can go either way.
- Each flip moves the count of $+1$ values by exactly one, so the distance from the current count to $N/2$ *is* the answer — no search is needed.

## Dry run

| $N$ | array | $+1$ count | target $N/2$ | distance | output |
|---:|---|---:|---:|---:|---|
| 4 | $1, 1, 1, 1$ | 4 | 2 | 2 | `2` |
| 5 | $1, -1, 1, -1, 1$ | — | — | — | `-1` (odd $N$) |
| 6 | $1, -1, -1, 1, 1, 1$ | 4 | 3 | 1 | `1` |
| 2 | $1, -1$ | 1 | 1 | 0 | `0` |

Row 2 is rejected on parity before any counting happens.
