# Doubly Increasing Path (DINCPATH)

[Problem statement](https://www.codechef.com/problems/DINCPATH) · [Python solution](../../solutions/DINCPATH.py)

## Approach

Orient each unequal-value edge upwards and sort by its positive difference. DP stores the longest path ending at each vertex. Process equal-difference edges in a batch so no transition can use another edge of the same difference.

## Complexity

- Time: O(M log M+N).
- Space: O(N+M).
