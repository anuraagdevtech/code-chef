---
topic: Greedy
subtopic: Bounded by the widest gap
time: $O(N)$ per test case
space: $O(1)$
---
A move raises any chosen subset of elements by $1$ — so in a single move, **every** element that still needs raising can be raised at once. There is no cost to touching more indices.

That makes the answer easy. Since values only increase, the common target must be at least $\max(A)$, and choosing exactly $\max(A)$ is optimal. The element needing the most work is the smallest one, requiring $\max(A) - \min(A)$ increments. Every other element needs fewer, so it can simply sit out the final moves. Hence

$$\text{moves} = \max(A) - \min(A)$$

The lower bound is clear — the minimum element gains at most $1$ per move — and the construction matches it, so the bound is tight.

The trap is treating this as a sum. Totalling $\sum (\max - A_i)$ counts individual increments, not moves, and would answer $4$ on sample case 1 instead of $2$. The freedom to choose $K$ and update many indices simultaneously is precisely what collapses the sum into a maximum.

Sample case 1 has $\max = 3$ and $\min = 1$, so $2$ moves: raise both $1$s together, twice. Sample case 2 is already uniform and needs none.

Aiming above $\max(A)$ would only add moves, so there is no reason to consider a higher target.

One pass computes both extremes, giving $O(N)$ time and $O(1)$ space — appropriate given the sum of $N$ reaches $10^5$.

## Edge cases

- **One move raises every lagging element at once**, so the cost is the single widest gap, not the total shortfall. The first row needs $2$; summing the per-element deficits ($2 + 0 + 2$) gives $4$.
- **Already equal** (the second row) → $0$, which $\max - \min$ gives with no special case.
- **$N = 1$**: maximum and minimum coincide, so the answer is $0$.
- **The target is forced to be $\max(A)$** — raising elements only, so nothing below the maximum can be the common value, and every element must climb to it.
- **Sum of $N$ bounded by $10^5$** across up to $10^4$ cases, so one pass per case with no sorting.

## Dry run

| input | max | min | gap | output |
|---|---:|---:|---:|---|
| $1, 3, 1$ | 3 | 1 | 2 | `2` |
| $2, 2, 2$ | 2 | 2 | 0 | `0` |

In the first row both $1$s rise together on each of the two moves.
