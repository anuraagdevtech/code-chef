---
topic: Greedy
subtopic: Earliest cut maximises the number of GCD-$G$ pieces
time: $O(N \log A)$ per test case
space: $O(1)$
---
$G$ divides every element, so the GCD of **any** subarray is a multiple of $G$ and hence at least $G$. An average of values each $\geq G$ equals $G$ only if they are *all* exactly $G$. So the arithmetic-mean condition is not an averaging problem at all — it demands

$$g_1 = g_2 = \cdots = g_K = G$$

and the question becomes: can we find $K$ disjoint subarrays each with GCD exactly $G$? Equivalently, is the maximum number of such disjoint subarrays at least $K$?

That maximum comes from a greedy sweep: run a running GCD from left to right and **cut as soon as it reaches $G$**, then reset. Cutting at the earliest possible point is optimal because a GCD only shrinks as a subarray grows, so any solution's first piece can be shortened to the greedy's first piece without affecting the rest — the classic exchange argument for interval packing.

Leftover elements at the end are simply discarded; the subarrays need not cover the array.

The samples separate the two outcomes. $[1,2,3,4,5]$ has $G = 1$ and the greedy cuts at $[1]$, $[2,3]$, $[4,5]$ — three pieces, enough for $K = 3$. But $[2,2,3,3,2,2]$ also has $G = 1$ and yields only two pieces, $[2,2,3]$ and $[3,2]$, falling short of $K = 4$: the twos cannot reach GCD $1$ on their own.

The last sample shows the same with a larger $G$: $[6,12,18,24]$ has $G = 6$, and only $[6]$ and $[12,18]$ qualify before the trailing $24$ is stranded, so $K = 3$ is impossible.
