# Flip the Prefix (PREFIXFLIP)

[Problem statement](https://www.codechef.com/problems/PREFIXFLIP) · [Python solution](../../solutions/PREFIXFLIP.py)

## Approach

Inside a chosen length-K window, every adjacent change requires a prefix flip ending at that boundary. One additional flip is needed exactly when the window's rightmost bit is zero. Slide the window while maintaining its number of changes and take the minimum cost.

## Complexity

- Time: O(N).
- Space: O(N).
