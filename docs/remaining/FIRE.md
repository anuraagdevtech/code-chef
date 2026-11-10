# Brush Fire (FIRE)

[Problem statement](https://www.codechef.com/problems/FIRE) · [Python solution](../../solutions/FIRE.py)

## Approach

Root the threatened forest component at the initial fire. Ignore branches with no target. With one target-containing child, protect it immediately. With two, protect one and continue fire down the other, which must itself be feasible. A burning target is infeasible. The binary branching condition makes this postorder DP sufficient.

## Complexity

- Time: O(N).
- Space: O(N).
