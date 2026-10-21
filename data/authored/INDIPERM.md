---
topic: Constructive
subtopic: A single cyclic shift
time: $O(N)$ per test case
space: $O(N)$
---
The requirement is that $i \nmid P_i$ for every $i \geq 2$. Index $1$ is deliberately excluded, because $1$ divides everything and no permutation could satisfy it there.

The simplest construction is a **cyclic shift by one**:

$$P = [N, 1, 2, 3, \ldots, N-1]$$

so that $P_i = i - 1$ for every $i \geq 2$.

Why it works: for $i \geq 2$ we have $0 < i - 1 < i$, and a positive integer strictly smaller than $i$ can never be a multiple of $i$. So $i \nmid P_i$ holds for every index at once, with no case analysis.

The wrapped value $N$ lands at index $1$, which is exactly the index with no constraint — the shift puts the one problematic value in the one position where nothing is required.

Contrast this with the identity permutation, which fails at **every** index since $i \mid i$ always. Shifting by one is the minimal perturbation that fixes all of them simultaneously.

For $N = 2$ this gives `2 1`, matching the sample exactly. For $N = 3$ it gives `3 1 2` where the sample prints `1 3 2` — both satisfy the condition ($2 \nmid 3$ and $3 \nmid 2$), so **any indivisible permutation is accepted** and this is judged by a checker.

The guarantee $N \geq 2$ means the shift always has somewhere to wrap to.

## Edge cases

- **Index $1$ is exempt by the statement** ($i \nmid P_i$ is required only for $2 \leq i \leq N$), which is what makes the problem solvable at all — every integer is divisible by $1$.
- **The wrapped $N$ lands at index $1$**, precisely the unconstrained slot, so the single cyclic shift is enough.
- **Every other index is safe for the same reason**: $P_i = i - 1$ satisfies $0 < i - 1 < i$, and no multiple of $i$ lies strictly between $0$ and $i$.
- **$N = 2$** (the smallest case): $[2, 1]$, where $P_2 = 1$ is not divisible by $2$.
- **This answer differs from the sample's** at $N \geq 3$ — it prints `3 1 2` where the sample shows `1 3 2`. The statement allows any valid permutation, so a special judge checks the divisibility rather than the exact output.
- **Sum of $N \leq 2 \cdot 10^5$**, so each line is built once and all output is joined at the end.

## Dry run

$N = 5$ gives $P = 5, 1, 2, 3, 4$.

| $i$ | $P_i$ | $P_i \bmod i$ | required? |
|---:|---:|---:|---|
| 1 | 5 | 0 | exempt |
| 2 | 1 | 1 | ✓ |
| 3 | 2 | 2 | ✓ |
| 4 | 3 | 3 | ✓ |
| 5 | 4 | 4 | ✓ |

For $i \geq 2$ the remainder is always $i - 1$, never zero.
