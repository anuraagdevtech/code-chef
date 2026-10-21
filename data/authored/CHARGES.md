---
topic: Arrays
subtopic: Local update of an adjacency count
time: $O(N + K)$ per test case
space: $O(N)$
---
The total length is a sum over the $N-1$ adjacent pairs, each worth $1$ or $2$. Writing $m$ for the number of pairs with **opposite** charges,

$$\text{distance} = 2(N-1) - m$$

so the whole state collapses to a single counter, and each query needs only the change in $m$.

Flipping particle $q$ changes nothing except the two pairs it belongs to, $(q-1, q)$ and $(q, q+1)$ — both of which **invert**: a matching pair becomes opposite and vice versa. So remove those pairs' contributions from $m$, flip the character, and add them back. That is $O(1)$ per update, with the ends handled by simply having fewer pairs.

Recomputing the whole string after each query would be $O(NK) = 10^{10}$; the local update makes it $O(N + K)$. No segment tree or difference array is needed, because a point flip touches a bounded number of pairs.

Updates are **persistent**, so the string must be mutated in place rather than re-read from the input each time — which also means the same position may be flipped twice and return to its original charge.

The sample runs all three cases. `010` starts with both pairs opposite, so $m = 2$ and the distance is $2 \cdot 2 - 2 = 2$. Flipping position $2$ gives `000` with $m = 0$ and distance $4$ — the maximum, since same-charge neighbours repel further. Flipping position $1$ makes `100`, with one opposite pair, giving $3$. Flipping position $3$ makes `101`, both pairs opposite again, back to $2$.
