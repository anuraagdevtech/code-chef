---
topic: Trees
subtopic: Carry the minimum and maximum ancestor wealth during DFS
time: $O(N)$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a fixed descendant, the greatest absolute wealth difference against an ancestor is attained by either the poorest or the richest ancestor. Carry both extremes along the root path during iterative DFS. Evaluate `max(highest - current, current - lowest)` before updating the extremes, so the pair contains two distinct vertices.

Every valid ancestor pair is covered by these two extremes at its descendant. This differs from INOI1601, which specifically asks for ancestor wealth minus descendant wealth. See the [CodeChef editorial](https://discuss.codechef.com/t/famtree-editorial/18864) for the absolute-difference interpretation.

## Edge cases

- The root is identified by parent `-1`, not by its index.
- Wealth may be negative.
- Check both directions of the wealth difference; wealth increasing down the tree can determine the answer.

## Dry run

The sample has root 2 with wealth 10, and descendant 3 under vertex 4 of wealth 12. At vertex 3, highest ancestor wealth is 12 and its wealth is 6, giving the maximum difference 6.
