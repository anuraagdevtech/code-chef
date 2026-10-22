---
topic: Conditionals & Case Work
subtopic: Fixed endpoints bound what the operation can reach
time: $O(N)$ per test case
space: $O(1)$
---
The operation only rewrites indices **strictly between** $i$ and $j$, so $A_1$ and $A_N$ can never change. Everything follows from that.

**If $A_1 = A_N$**, applying the operation to the pair $(1, N)$ overwrites the entire interior, leaving one distinct value. Always `YES`.

**If $A_1 \neq A_N$**, the final array already contains two distinct values, so *every* element must end up equal to $A_1$ or $A_N$. The best reach is:

- let $p$ be the **last** index with $A_p = A_1$; the operation $(1, p)$ makes $A_1 \ldots A_p$ all $A_1$;
- let $q$ be the **first** index with $A_q = A_N$; the operation $(q, N)$ makes $A_q \ldots A_N$ all $A_N$.

Those two sweeps are the furthest either value can spread, because an operation needs a matching pair of endpoints and no copy of $A_1$ lies beyond $p$, nor of $A_N$ before $q$. So the answer is `YES` exactly when the two ranges leave no gap:

$$q \leq p + 1$$

Anything stranded in $(p, q)$ is doomed: by definition it equals neither $A_1$ nor $A_N$, and flattening it with some inner pair would only install a *third* value.

The samples show each branch. $[5,9,5,5,5]$ has equal ends, so one operation flattens it. $[1,2,1,3]$ has $p = 3$ and $q = 4$, touching exactly, so the $2$ is absorbed. $[1,2,3,1]$ again has equal ends. And $[1,2,3]$ has $p = 1$, $q = 3$, leaving the $2$ unreachable — there is no matching pair anywhere, so nothing can be done at all.

## Edge cases

- **The first and last elements can never change.** An operation only rewrites indices strictly between $i$ and $j$, so $A_1$ and $A_N$ survive everything — which both bounds the answer and drives the whole case split.
- **If $A_1 = A_N$ one operation flattens the array** to a single value, so the answer is `YES` regardless of what lies between (the first and fourth rows).
- **Otherwise both $A_1$ and $A_N$ must remain, so the target is exactly two values** — and each can spread only as far as its own outermost copy: $A_1$ rightward to its last occurrence, $A_N$ leftward to its first.
- **The two spreads must meet or touch**, hence $\text{first occurrence of } A_N \leq \text{last occurrence of } A_1 + 1$. A gap between them leaves a third value stranded.
- **No equal pair at all** means no operation is possible (the second row, $1,2,3$), and three distinct values remain.
- **Touching exactly** (the third row, where the spreads are adjacent at indices $2$ and $3$) is enough, which is why the bound is non-strict with the $+1$.
- **Values are compared as raw byte tokens**, safe since the input has no leading zeros.

## Dry run

Third sample: $A = 1, 2, 1, 3$.

| quantity | value |
|---|---:|
| last index holding $A_1 = 1$ | 3 (1-based) |
| first index holding $A_N = 3$ | 4 |
| is $4 \leq 3 + 1$? | yes |

Output `YES`: one operation on the two $1$s at indices $1$ and $3$ gives $1, 1, 1, 3$ — two distinct values.
