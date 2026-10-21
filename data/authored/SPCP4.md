---
topic: Basic Math
subtopic: Remainders paired off
time: $O(1)$ per test case
space: $O(1)$
---
There are $X$ boys and $N - X$ girls. Each gender forms as many full groups of $K$ as possible, so the students left over are the remainders:

$$r_b = X \bmod K, \qquad r_g = (N - X) \bmod K$$

Those leftovers can dance, but only in mixed pairs — one boy with one girl. So $\min(r_b, r_g)$ pairs form, consuming $2\min(r_b, r_g)$ students, and the rest must read:

$$r_b + r_g - 2\min(r_b, r_g) = |r_b - r_g|$$

The absolute difference is the whole answer, and it says something clean: dancing cancels the leftovers against each other, and only the **imbalance** is stranded.

Note that the group-forming is not a choice — the statement says both genders form as many groups as possible — so there is no optimisation deciding whether to leave more students out for dancing. If it were a choice, holding back students to form more dancing pairs could sometimes beat this, and the problem would be considerably harder.

Sample case 3 is the one-sided case: $8$ boys and no girls leave $r_b = 2$ and $r_g = 0$, so both leftover boys read. Sample case 2 divides evenly on both sides, leaving nobody. Sample case 1 has $r_b = 1$ and $r_g = 2$, so one pair dances and a single girl reads.

With $N$ and $K$ up to $10^9$ only the closed form is viable, but the arithmetic is trivial.

## Edge cases

- **Both remainders zero** (the second row, $15\,10\,5$): nothing is left over on either side, so $0$.
- **Everyone on one side** (the third row, where $X = N$): the other group is empty, so its remainder is $0$ and the answer is the first remainder alone.
- **The remainders cancel rather than add.** Leftover members of the two groups pair off with each other, so only the imbalance shows — taking the sum instead of the absolute difference would report $3$ on the first row instead of $1$.
- **$K = 1$**: every remainder is $0$, so the answer is always $0$.

## Dry run

The three values are $N$, then $X$, then $K$.

| $N$ | $X$ | $K$ | $X \bmod K$ | $(N{-}X) \bmod K$ | difference | output |
|---:|---:|---:|---:|---:|---:|---|
| 12 | 4 | 3 | 1 | 2 | 1 | `1` |
| 15 | 10 | 5 | 0 | 0 | 0 | `0` |
| 8 | 8 | 3 | 2 | 0 | 2 | `2` |

Row 3 has an empty second group.
