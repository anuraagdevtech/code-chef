# Server Trouble (SVRT)

[Problem statement](https://www.codechef.com/problems/SVRT) · [Python solution](../../solutions/SVRT.py)

## Approach

Use clockwise gaps, as clarified by the official editorial. K positive gaps sum to N, so their smallest possible maximum is ceil(N/K). Exactly N-K*(ceil(N/K)-1) gaps must have that maximum.

## Complexity

- Time: O(1).
- Space: O(1).

[Official clarification of clockwise gaps](https://discuss.codechef.com/t/svrt-editorial/87249).
