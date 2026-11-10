# FCAR (INSQ15_F)

[Problem statement](https://www.codechef.com/problems/INSQ15_F) · [Python solution](../../solutions/INSQ15_F.py)

## Approach

Dijkstra's states are (city, uphill/downhill mode). Changing mode costs the current city's fee; traversing a compatible road costs zero. Both initial modes cost the first city's fee, and equal-height roads accept either mode.

## Complexity

- Time: O((N+M) log N).
- Space: O(N+M).
