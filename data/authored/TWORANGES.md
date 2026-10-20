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
