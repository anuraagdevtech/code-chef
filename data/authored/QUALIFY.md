---
topic: Basic Math
subtopic: Weighted sum against a threshold
time: $O(1)$ per test case
space: $O(1)$
---
Easy problems are worth $1$ point and hard ones $2$, so solving $A$ easy and $B$ hard problems scores

$$A + 2B$$

Chef qualifies when that total reaches the threshold $X$. Because the bar is "**at least** $X$ points", the comparison is `>=` and scoring exactly $X$ qualifies.

The only way to go wrong is to mix up which count carries the weight. The input order is $X, A, B$ — threshold first, then easy, then hard — which is deliberately not the order the quantities are introduced in the prose. Reading the three integers into the wrong names gives a plausible-looking program that fails immediately; sample case 3 ($X=6, A=2, B=8$) would score $2 + 16 = 18$ correctly but $8 + 4 = 12$ if $A$ and $B$ were swapped, and both pass the threshold, so the first sample is the one that actually exposes the error.

Note that $A$ and $B$ may be zero — Chef need not have attempted both kinds — so no positivity assumption is safe. Case 2 has $B = 0$ and falls short with $3 < 5$.
