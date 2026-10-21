---
topic: Sorting
subtopic: Sliding a fixed-size window
time: $O(N \log N)$ per test case
space: $O(N)$
---
The spread of a chosen set depends only on its largest and smallest members, so the middle elements are free. That means an optimal choice of $K$ elements can always be taken **contiguous in sorted order**: if two chosen values have an unchosen value between them, swapping it in never widens the spread.

So sort the array and slide a window of width $K$, taking the best:

$$\min_{0 \leq i \leq N-K} \bigl(A_{i+K-1} - A_i\bigr)$$

Sorting dominates at $O(N \log N)$; the sweep itself is linear with no extra storage.

The contiguity argument is what makes this cheap. Without it one might consider $\binom{N}{K}$ subsets, which is hopeless at $N = 10^5$.

Sample case 1, $[1,2,4,7]$ with $K = 3$, has windows $[1,2,4]$ spanning $3$ and $[2,4,7]$ spanning $5$ — so $3$. Note the best window is **not** the one containing the two closest elements in isolation; it is the tightest run of three.

Sample case 3, $[1,5,44,20,40]$ with $K = 4$, sorts to $[1,5,20,40,44]$ with both windows spanning $39$ — a tie, which needs no special handling.

Duplicates give a span of $0$ and are handled naturally. When $K = N$ there is a single window, the whole array, and when $K = 1$ every window has width $0$.
