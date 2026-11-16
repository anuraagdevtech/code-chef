---
topic: Dynamic Programming
subtopic: Subset sum of inversion-graph degrees
time: $O(N^2+NI/w)$ word operations per test case for $I$ total inversions
space: $O(N+I/w)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Form the inversion graph: each permutation position is a vertex, and each inversion is an undirected edge. Let $I$ be the total edge count. If positions are partitioned into $S$ and its complement, then `sum(degree[u] for u in S) - I` equals the number of internal inversions in $S$ minus the number in the complement; crossing edges cancel.

Therefore equal inversion counts are possible exactly when some subset of vertex degrees sums to $I$. Compute degrees by testing all pairs, then solve this subset-sum question with an integer bitset capped at $I$. Empty subsequences are naturally included.

## Edge cases

- With no inversions, the empty subset already reaches target zero.
- Degrees count inversion partners on both sides of a position.
- Merely checking that the total inversion count is even is insufficient.

## Dry run

For `[3,2,1]`, every vertex has degree two, but the target is three inversions, which no subset of degrees reaches. For `[4,3,2,1]`, target six is reached by choosing two vertices of degree three.
