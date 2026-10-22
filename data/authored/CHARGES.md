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

## Edge cases

- **The total length is $2(N-1) - (\text{opposite pairs})$.** Each of the $N-1$ gaps costs $2$ for a matching pair and $1$ for an opposite one, so counting the opposite pairs and subtracting is enough.
- **A flip touches only two gaps** — the ones on either side of the flipped particle — and both invert, which is what makes each query $O(1)$ instead of a rescan.
- **The flips are cumulative.** Query $2$ then $1$ then $3$ in the sample operate on a string that keeps changing, so the state must be mutated rather than recomputed from the original.
- **The ends have only one adjacent gap**, which the `0 <= j < n - 1` guard handles for $Q = 1$ and $Q = N$.
- **The old contributions must be removed before the flip and the new ones added after**, or the delta is computed against a stale character.
- **$N = 1$** has no gaps at all, so the length is $0$ for every query.
- **Sum of $K \leq 2 \cdot 10^5$**: a `bytearray` for in-place flips and XOR with $1$ to toggle between the byte codes for `0` and `1`.

## Dry run

$N = 3$, $S = $ `010`, so $2(N-1) = 4$.

| query | string after | opposite pairs | length |
|---:|---|---:|---:|
| flip 2 | `000` | 0 | `4` |
| flip 1 | `100` | 1 | `3` |
| flip 3 | `101` | 2 | `2` |

The last state has both gaps opposite, so each costs $1$.
