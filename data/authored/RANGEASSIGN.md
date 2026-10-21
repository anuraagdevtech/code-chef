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
