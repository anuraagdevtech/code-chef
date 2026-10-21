---
topic: Binary Search
subtopic: Searching the answer on a monotonic predicate
time: $O(N \log \max A)$ per test case
space: $O(1)$
---
At speed $K$, a pile of $A_i$ bananas takes $\lceil A_i / K \rceil$ hours, because Chef commits a whole hour to one pile even when the remainder is small. So the total time is

$$f(K) = \sum_{i} \left\lceil \frac{A_i}{K} \right\rceil$$

The key structural fact is that $f$ is **non-increasing** in $K$: eating faster never takes longer. So the predicate "$f(K) \leq H$" is false for small $K$ and true for all $K$ beyond some threshold — exactly the monotone shape that **binary search on the answer** needs.

Search $K$ over $[1, \max A]$; the upper end suffices because at that speed every pile falls in one hour, needing $N \leq H$ hours, which the constraints guarantee.

Each evaluation of $f$ costs one pass, so the whole thing is $O(N \log \max A)$ — about $30$ passes rather than the $10^9$ a linear scan over $K$ would need.

The ceiling must be computed in integers as `(a + k - 1) // k`; a float division would drift at $A_i$ up to $10^9$.

The samples show the threshold moving with the budget. With piles $[1,2,3]$ and $H = 3$ — exactly the number of piles — Chef has one hour per pile, so $K$ must cover the largest pile outright: $K = 3$. Give her one extra hour ($H = 4$) and $K = 2$ suffices, since the $3$-pile may then take two hours.

Sample case 3 lands exactly on the budget: $K = 4$ costs $1+1+1+2 = 5 = H$, and $K = 3$ costs $7$.
