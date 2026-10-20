---
topic: Sorting
subtopic: Adjacent gaps in sorted order
time: $O(N \log N)$ per test case
space: $O(N)$
---
A rearrangement with every adjacent pair differing by at most $1$ exists **if and only if the sorted array already has that property**.

One direction is immediate: if sorting works, a valid arrangement exists. The other is the interesting one. Suppose the sorted values have a gap larger than $1$ between some $a$ and the next distinct value $b$. Then the multiset splits into two groups — values $\leq a$ and values $\geq b$ — with no value in between. Any arrangement must at some point step from one group to the other, and that step is a jump of at least $b - a > 1$. So no arrangement can work.

Hence the test is simply: sort, then check every consecutive difference.

That argument is what makes the problem a two-liner rather than a search over permutations. It also shows the sorted order is *canonical* here: if any arrangement works, the sorted one does.

Sample case 1, $[3,2,2,3]$, sorts to $[2,2,3,3]$ with gaps $0, 1, 0$ — all within bounds, so `YES`. Sample case 2, $[1,5]$, has a single gap of $4$ and fails.

Note that duplicates are harmless, contributing gaps of $0$, and that $N = 1$ is vacuously fine with no adjacent pairs at all.

With the sum of $N$ reaching $2 \times 10^5$, the sort dominates and bulk input reading is worth having; `all(...)` over the consecutive pairs short-circuits on the first violation.
