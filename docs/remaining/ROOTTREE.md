# Root the Tree (ROOTTREE)

[Problem statement](https://www.codechef.com/problems/ROOTTREE) · [Python solution](../../solutions/ROOTTREE.py)

## Approach

A rooted outward tree needs a single indegree-zero vertex and indegree one elsewhere. Each extra source requires one edge replacement to join it to the chosen root's component. Thus the optimum is the number of original sources minus one.

## Complexity

- Time: O(N).
- Space: O(N).
