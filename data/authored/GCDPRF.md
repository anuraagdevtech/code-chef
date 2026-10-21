---
topic: Constructive
subtopic: Divisibility chain, realised by the array itself
time: $O(N \log A)$ per test case
space: $O(N)$
---
Prefix GCDs only ever shrink, and they shrink by division: $B_{i} = \gcd(B_{i-1}, A_i)$, so

$$B_i \mid B_{i-1}$$

is necessary. If that chain ever breaks — as in the sample's $B = [1, 3]$, where $3 \nmid 1$ — no array exists and the answer is $-1$.

When the chain holds, the construction is as short as it gets: take $A = B$. The divisibility chain means $B_i$ divides every earlier $B_j$, so

$$\gcd(B_1, B_2, \ldots, B_i) = B_i$$

and the prefix GCDs of $A$ reproduce $B$ exactly. The range condition is free as well, since $B_i \leq 10^9$ is given.

It is worth seeing why nothing cleverer is needed. One might try to make $A_i$ a multiple of $B_i$ that avoids extra common factors — the sample's `4 26` does this, with $26 = 2 \cdot 13$ — but the earlier prefix already caps the GCD at $B_{i-1}$, so any extra factors in $A_i$ beyond $B_i$ are harmless *and* unnecessary. Echoing $B$ is both valid and simplest.

Note the chain condition is only about consecutive terms: $B_i \mid B_{i-1}$ for every $i$ implies $B_i \mid B_j$ for all $j < i$ by transitivity, so one pass suffices.

Our output for the first sample is `4 2` where the sample prints `4 26`; both have prefix GCDs $4, 2$, and the problem accepts any valid array.
