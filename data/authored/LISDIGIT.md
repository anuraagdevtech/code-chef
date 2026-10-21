---
topic: Constructive
subtopic: Using the LIS value itself as the digit
time: $O(n)$ per test case
space: $O(n)$
---
The inverse problem looks harder than the forward one, but there is a construction so short it needs no search: **use the LIS value as the digit**.

$$d_i = \mathrm{LIS}_i$$

Why it works comes from the defining recurrence of the LIS array over any sequence $d$:

$$\mathrm{LIS}(i) = 1 + \max\{\mathrm{LIS}(j) : j < i,\ d_j < d_i\}$$

(with the max taken as $0$ when the set is empty). Suppose by induction that the array produced by $d = \mathrm{LIS}$ matches $\mathrm{LIS}$ at all earlier positions. Then the set above is $\{\mathrm{LIS}_j : j < i,\ \mathrm{LIS}_j < \mathrm{LIS}_i\}$, and its maximum is exactly $\mathrm{LIS}_i - 1$ — because a **valid** LIS array always has some earlier position with value $\mathrm{LIS}_i - 1$ (the predecessor of $i$ on its own increasing subsequence), and by definition no earlier value can sit strictly between $\mathrm{LIS}_i - 1$ and $\mathrm{LIS}_i$. So the recurrence returns $\mathrm{LIS}_i$, as required.

Two side conditions fall out for free. Every $\mathrm{LIS}_i \geq 1$, so no digit is $0$ and there is never a leading zero; and $n \leq 9$ bounds $\mathrm{LIS}_i \leq 9$, so every value is a legal single digit. That bound on $n$ is exactly what makes the identity construction work — for $n \geq 11$ an LIS array could demand a value of $10$.

Many answers are accepted. For $[1,2,2,1,3,2,4]$ we print `1221324` where the sample prints `1730418`; both have that LIS array. For $[1,1]$ we print `11` — equal digits are correct here, since the LIS must be *strictly* increasing so the second digit cannot extend the first.

## Edge cases

- **Using the LIS value as the digit is self-consistent.** Reading the array as digits, a strictly increasing run ending at position $i$ is a strictly increasing run of integers finishing at $L_i$ and starting at $1$ or more, so it has at most $L_i$ terms; and a chain with values $1, 2, \ldots, L_i$ genuinely exists, so exactly $L_i$ is achieved.
- **No leading zero**, because every $L_i \geq 1$; and **no digit above $9$**, because $n \leq 9$ bounds any increasing subsequence.
- **$L_i$ is the LIS length *ending at* position $i$**, not of the prefix — in `1 2 2 1` the value drops back to $1$ at the last position, which a prefix reading could never do.
- **Repeated values are fine**: the two $2$s in that array both have $L = 2$, because strict increase stops the second $2$ from extending a chain through the first.
- **This answer differs from the sample's.** The sample prints `1531` where this prints `1221`; a special judge checks the resulting LIS array rather than the exact digits, so both are accepted.
- **Existence is guaranteed** by the statement, so no feasibility check is needed.

## Dry run

Last sample: $L = 1, 2, 2, 1, 3, 2, 4$, so the number is `1221324`.

| position | digit | longest strictly increasing run ending here | length |
|---:|---:|---|---:|
| 1 | 1 | $1$ | 1 |
| 2 | 2 | $1, 2$ | 2 |
| 3 | 2 | $1, 2$ | 2 |
| 4 | 1 | $1$ | 1 |
| 5 | 3 | $1, 2, 3$ | 3 |
| 6 | 2 | $1, 2$ | 2 |
| 7 | 4 | $1, 2, 3, 4$ | 4 |

The lengths reproduce the input array exactly.
