---
topic: Trees
subtopic: Reroot distance sums using subtree sizes
time: $O(N)$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Root the tree at vertex zero. One traversal computes depths and a parent-first order. The sum of depths is the distance sum for root zero; a reverse traversal gives subtree sizes.

When moving the root across edge $u-v$ to child $v$, distances to the $size[v]$ vertices inside that subtree decrease by one, while all others increase by one. Therefore $answer[v]=answer[u]+N-2size[v]$. Evaluate this in parent-first order.

The adjacency representation uses compact integer arrays because the bound reaches one million vertices. Iterative traversal avoids recursion depth limits.

## Edge cases

- Vertices are zero-based in this problem.
- One vertex has distance sum zero.
- Large chains require integer sums beyond 32 bits.
- The published sample is embedded in the statement rather than the API sample list.

## Dry run

For sample edges `0-2,0-3,1-3,3-4`, root-zero depths sum to 6. Subtree 3 has size 3, so its answer is `6+5-6=5`. Its leaf children have answer `5+5-2=8`.
