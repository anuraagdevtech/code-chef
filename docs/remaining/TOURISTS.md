# Tourists in Mancunia (TOURISTS)

[Problem statement](https://www.codechef.com/problems/TOURISTS) · [Python solution](../../solutions/TOURISTS.py)

## Approach

A connected undirected graph admits a balanced Eulerian orientation exactly when every degree is even. Iteratively traverse unused edges and orient them in traversal order. Check connectivity and final indegree/outdegree balance; preserve original edge order in the output.

## Complexity

- Time: O(N+M).
- Space: O(N+M).
