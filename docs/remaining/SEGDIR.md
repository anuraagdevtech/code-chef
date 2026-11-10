# Moving Segments (SEGDIR)

[Problem statement](https://www.codechef.com/problems/SEGDIR) · [Python solution](../../solutions/SEGDIR.py)

## Approach

Different speeds separate at the very large final time. For each equal speed, overlapping closed intervals need opposite directions; their interval graph is bipartite exactly when no point is covered by three intervals. A sweep checks this maximum overlap, with starts processed before ends at equal coordinates.

## Complexity

- Time: O(N log N).
- Space: O(N).
