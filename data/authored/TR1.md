---
topic: Trees
subtopic: Count ordered pairs by their lowest common ancestor
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The city where two agents first meet is the lowest common ancestor of their assigned cities. There are $size[u]^2$ ordered pairs entirely inside $u$'s subtree. Pairs lying entirely in a single child's subtree have their LCA below $u$ and must be subtracted.

Thus $Im(u)=size[u]^2-\sum size[v]^2$ over children. Compute subtree sizes in reverse traversal order, multiply each importance by its one-based city label, and sum modulo $10^9+7$.

## Edge cases

- Pairs are ordered, so `(A,B)` and `(B,A)` both count.
- Include diagonal pairs `(u,u)`.
- A one-city tree returns one.

## Dry run

In the five-city sample tree, subtree sizes are `[5,3,1,1,1]`. Importance at city 1 is `25-9-1=15`; at city 2 it is `9-1-1=7`; leaves contribute one each. The weighted sum is 41.
