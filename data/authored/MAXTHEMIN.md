---
topic: Sorting
subtopic: The (K+1)-th smallest survives
time: $O(N \log N)$ per test case
space: $O(N)$
---
Each operation overwrites one element with a neighbour's value, so **at most $K$ positions can be changed**. Whatever is not overwritten keeps its original value, and the final minimum is at most the smallest surviving original.

That gives an upper bound: however the $K$ operations are spent, at least $N - K$ originals remain, so the minimum cannot exceed the $(K+1)$-th smallest value — overwriting the $K$ smallest is the best one could hope for.

The bound is achievable. Values propagate along neighbours, so each of the $K$ smallest elements can be overwritten by a larger adjacent value, one operation apiece. Hence

$$\text{answer} = A_{(K)} \text{ in sorted order, i.e. } \mathrm{sorted}(A)[\min(K,\, N-1)]$$

The clamp handles the case $K \geq N - 1$, where enough operations exist to flood the whole array with its maximum. Sample cases 1 and 4 are both this: case 1 has exactly $K = N - 1 = 4$, and case 4 has $K$ far beyond it, both answering $\max(A) = 5$.

Without the clamp, `sorted(a)[k]` would index out of range on case 4.

Sample case 2 is the plain case: one operation removes the single smallest element $2$, leaving $3$ as the new minimum — the second smallest, which is `sorted(a)[1]`.

Sample case 3 removes both $3$s with two operations, promoting the minimum to $4$.

Sorting costs $O(N \log N)$; `heapq.nsmallest` or a partial selection would shave that to $O(N \log K)$, immaterial at these bounds.
