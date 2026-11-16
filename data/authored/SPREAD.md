---
topic: Fenwick Tree
subtopic: Range additions become two difference-array point updates
time: $O((N+M)\log N)$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Use a Fenwick tree for differences from the common initial amount $C$. Adding $K$ to inclusive range $[u,v]$ changes only two differences: add $K$ at $u$ and subtract $K$ at $v+1$. A prefix sum at position $p$ is its total added amount, so the query answer is that prefix sum plus $C$.

## Edge cases

- Skip the second difference update when $v=N$.
- Amounts can exceed 32-bit integers after many updates.
- There is one input case, without a test-count prefix.

## Dry run

The sample starts at zero. Adding one to `[1,7]` makes position 3 equal one; another addition to `[1,3]` makes it two.
