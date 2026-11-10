# Chef and Reversing (REVERSE)

[Problem statement](https://www.codechef.com/problems/REVERSE) · [Python solution](../../solutions/REVERSE.py)

## Approach

Give every original directed edge cost zero and its reverse cost one. A deque-based 0-1 BFS finds the minimum reversal count from vertex one to vertex N, or detects disconnection.

## Complexity

- Time: O(N+M).
- Space: O(N+M).
