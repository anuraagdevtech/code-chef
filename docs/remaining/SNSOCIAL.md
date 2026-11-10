# Snakes and transition from Capitalism to Socialism (SNSOCIAL)

[Problem statement](https://www.codechef.com/problems/SNSOCIAL) · [Python solution](../../solutions/SNSOCIAL.py)

## Approach

All globally richest cells are simultaneous sources. Their value propagates one king move per hour, so an eight-neighbor multi-source BFS gives the time at which the last cell receives that wealth.

## Complexity

- Time: O(NM).
- Space: O(NM).
