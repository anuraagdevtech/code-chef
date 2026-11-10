# Gravel (SPREAD)

[Problem statement](https://www.codechef.com/problems/SPREAD) · [Python solution](../../solutions/SPREAD.py)

## Approach

Maintain the difference array in a Fenwick tree. Adding k to [l,r] changes differences at l and r+1; a point query is its prefix sum plus the common initial value.

## Complexity

- Time: O((N+M) log N).
- Space: O(N).
