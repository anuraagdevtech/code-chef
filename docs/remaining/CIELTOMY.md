# Ciel and Tomya (CIELTOMY)

[Problem statement](https://www.codechef.com/problems/CIELTOMY) · [Python solution](../../solutions/CIELTOMY.py)

## Approach

Run Dijkstra with a path-count array. A shorter relaxation replaces the count; an equal-distance relaxation adds it. Positive edge lengths ensure all predecessors are processed before the destination state.

## Complexity

- Time: O((N+M) log N).
- Space: O(N+M).
