# India Fights Corona (CORONA)

[Problem statement](https://www.codechef.com/problems/CORONA) · [Python solution](../../solutions/CORONA.py)

## Approach

Initialize Dijkstra with every hospital, using its test fee as its initial distance. The minimum propagated value at each city combines the best hospital fee and the shortest transportation cost.

## Complexity

- Time: O((N+M) log N).
- Space: O(N+M).
