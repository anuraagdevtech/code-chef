# Monks (MONKS)

[Problem statement](https://www.codechef.com/problems/MONKS) · [Python solution](../../solutions/MONKS.py)

## Approach

The total number of coins is an upper bound on what the remaining people can hold. To keep m people, choose the m smallest initial fortunes and raise them to their maximum; feasibility is m*maximum<=total. Departing people can supply any needed difference, so this condition is also sufficient.

## Complexity

- Time: O(N log N).
- Space: O(N).
