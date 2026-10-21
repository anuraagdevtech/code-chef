---
topic: Basic Math
subtopic: Range of achievable sums
time: $O(1)$ per test case
space: $O(1)$
---
Adding two values from $\{L, \ldots, R\}$, with repetition allowed, gives a smallest sum of $L + L = 2L$ and a largest of $R + R = 2R$.

The important claim is that **every** integer in between is reachable. Starting from $(L, L)$, raising one of the two chosen values by one increases the sum by exactly one, and either value may be raised until it hits $R$. So the sums sweep the whole interval with no gaps, and the count is

$$2R - 2L + 1$$

Confirming that there are no gaps is the step that matters. The instinct that pair sums might skip values is reasonable in general — it is true for a set like $\{1, 10\}$ — but a **contiguous** range of integers produces a contiguous range of sums, precisely because unit steps are available.

The "not necessarily distinct" clause is what makes $2L$ and $2R$ themselves reachable. Requiring distinct values would shrink the range to $[2L+1, 2R-1]$ and make $L = R$ a degenerate case with no valid pair at all.

Sample case 1 has $L = R = 2$: the only sum is $4$, and the formula gives $4 - 4 + 1 = 1$. Sample case 2 spans $4$ to $6$ for $3$ reachable values.

The usual fencepost applies — the $+1$ is needed because both endpoints are included.

## Edge cases

- **The two integers need not be distinct**, which the statement says explicitly — that is what makes $2L$ and $2R$ themselves reachable, and why $L = R$ gives one sum rather than none.
- **There are no gaps in $[2L, 2R]$**, because either addend can be nudged by one: starting from $L + L$ and incrementing one side at a time sweeps every integer up to $R + R$.
- **$L = R$** (the first row) → exactly one reachable value, $2L$.
- **The count is of distinct sums, not of pairs** — the second row has nine ordered pairs but only three distinct sums.
- **$L, R$ up to $10^6$** keeps the answer under $2 \times 10^6$, so no large arithmetic is involved.
- **$T$ up to $10^5$** with constant work per case.

## Dry run

| $L$ | $R$ | reachable sums | count |
|---:|---:|---|---:|
| 2 | 2 | $4$ | `1` |
| 2 | 3 | $4$ ($2{+}2$), $5$ ($2{+}3$), $6$ ($3{+}3$) | `3` |
