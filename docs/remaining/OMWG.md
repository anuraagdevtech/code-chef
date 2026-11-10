# One more weird game (OMWG)

[Problem statement](https://www.codechef.com/problems/OMWG) · [Python solution](../../solutions/OMWG.py)

## Approach

Every grid edge contributes exactly once, when its second endpoint is colored. The order cannot change the score, which is N*(M-1)+M*(N-1).

## Complexity

- Time: O(1).
- Space: O(1).
