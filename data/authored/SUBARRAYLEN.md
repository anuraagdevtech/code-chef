---
topic: Arrays
subtopic: Grouping by length, then a union of intervals
time: $O(N)$ per test case
space: $O(N)$
---
Counting per subarray invites double counting, since a window may contain several elements equal to its own length. Group by **length** instead.

Fix a length $\ell$ and let $p_1 < \cdots < p_m$ be the positions holding the value $\ell$. A window of length $\ell$ is determined by its left end $L \in [1, N-\ell+1]$, and it contains position $p$ exactly when

$$L \in [\,p - \ell + 1,\ p\,]$$

So the valid left ends form a **union of $m$ intervals**, each clipped to the legal range, and the count for this length is the size of that union. Because the $p_j$ are increasing, so are the intervals, and merging them is a single sweep that tracks the furthest left end already used.

Summing over all $\ell$ costs $O(N)$ in total — each position appears in exactly one length's list — and the union handles overlaps exactly once, which is what the direct per-element count gets wrong.

$$\text{answer} = \sum_{\ell=1}^{N} \left|\ \bigcup_{j} \bigl[\max(1, p_j - \ell + 1),\ \min(p_j, N-\ell+1)\bigr]\ \right|$$

Lengths with no matching value contribute nothing, and an interval can come out empty after clipping — for instance a value $\ell$ sitting too near the array's start to anchor a window of that length.

The second sample, $[2,3,1,3,5]$, totals $6$: length $3$ alone contributes $3$, because the two threes at positions $2$ and $4$ give the overlapping ranges $[1,2]$ and $[2,3]$, whose union is $[1,3]$ — counting them separately would give $4$ and overcount the window starting at $2$.
