# Cricket Match (CRIMCH)

[Problem statement](https://www.codechef.com/problems/CRIMCH) · [Python solution](../../solutions/CRIMCH.py)

## Approach

Conflicting people must receive different teams, exactly the bipartite-coloring condition. Color every connected component iteratively and reject any edge whose endpoints receive the same color.

## Complexity

- Time: O(N+M).
- Space: O(N+M).
