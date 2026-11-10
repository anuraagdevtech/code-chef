# Even Edges (EVEDG)

[Problem statement](https://www.codechef.com/problems/EVEDG) · [Python solution](../../solutions/EVEDG.py)

## Approach

If M is even, use one part. Otherwise isolate an odd-degree vertex to get two even-edge parts. If every degree is even, separate the two endpoints of any edge into distinct singleton parts; their removal leaves an even number of edges and three parts are necessary.

## Complexity

- Time: O(N+M).
- Space: O(N).
