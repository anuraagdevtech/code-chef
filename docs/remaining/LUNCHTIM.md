# Lunchtime (LUNCHTIM)

[Problem statement](https://www.codechef.com/problems/LUNCHTIM) · [Python solution](../../solutions/LUNCHTIM.py)

## Approach

Run a decreasing monotonic stack from each side. Shorter groups are popped; an equal-height top group contributes all its members, whereas a taller group blocks everything behind it. Add contributions from both directions.

## Complexity

- Time: O(N).
- Space: O(N).
