---
topic: Sets
subtopic: Inclusion-exclusion on intervals
time: $O(1)$ per test case
space: $O(1)$
---
Count the integers lying in $[A,B] \cup [C,D]$. By inclusion–exclusion:

$$|[A,B]| + |[C,D]| - |[A,B] \cap [C,D]|$$

An inclusive integer range $[P,Q]$ holds $Q - P + 1$ values — the $+1$ is the usual fencepost, easy to drop.

The intersection of two intervals is $[\max(A,C),\ \min(B,D)]$, whose size is

$$\max\bigl(0,\ \min(B,D) - \max(A,C) + 1\bigr)$$

The clamp at zero is essential: when the ranges are disjoint the computed length goes negative, and subtracting a negative would *inflate* the answer. Sample case 1 is exactly that — $[1,3]$ and $[5,5]$ give $\min(3,5) - \max(1,5) + 1 = -1$, which must be treated as $0$, yielding $3 + 1 = 4$.

Sample case 3 shows full containment: $[4,6]$ sits inside $[1,8]$, so the overlap is the whole of the smaller range and the union is just $8$. Sample case 4 has both ranges identical, where the overlap cancels one copy exactly to give $1$.

Because the bounds here are tiny ($1$ to $8$), building actual Python sets and taking `len(set(range(a, b+1)) | set(range(c, d+1)))` would be perfectly fine and arguably clearer. The inclusion–exclusion form is worth knowing because it stays $O(1)$ when the bounds reach $10^{18}$, where enumeration is impossible.

## Edge cases

- **Disjoint ranges** ($1..3$ and $5..5$): the overlap expression evaluates to $-1$ and **must clamp to zero**. Without the clamp the answer comes out as $5$ instead of $4$, and the sample's first row is exactly this.
- **Ranges that touch without overlapping** ($1..3$ and $4..6$): the expression gives exactly $0$, so the clamp is not needed but does no harm — the boundary between the two behaviours.
- **One range inside the other** ($1..8$ and $4..6$): the union is just the outer range, $8$.
- **Identical single points** ($5..5$ twice): the union is $1$, not $2$.
- **Inclusive counts throughout**: a range $A..B$ holds $B - A + 1$ values, so each $+1$ matters — dropping them understates every answer.

## Dry run

| $A..B$ | $C..D$ | sizes | overlap $\min(B,D) - \max(A,C) + 1$ | union | output |
|---|---|---|---:|---:|---|
| $1..3$ | $5..5$ | $3 + 1$ | $3 - 5 + 1 = -1 \to 0$ | 4 | `4` |
| $3..8$ | $2..5$ | $6 + 4$ | $5 - 3 + 1 = 3$ | 7 | `7` |
| $1..8$ | $4..6$ | $8 + 3$ | $6 - 4 + 1 = 3$ | 8 | `8` |
| $5..5$ | $5..5$ | $1 + 1$ | $5 - 5 + 1 = 1$ | 1 | `1` |

Row 1 is the clamp; row 3 is full containment.
