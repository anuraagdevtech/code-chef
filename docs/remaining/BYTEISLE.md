# Byteknights and Byteknaves (BYTEISLE)

[Problem statement](https://www.codechef.com/problems/BYTEISLE) · [Python solution](../../solutions/BYTEISLE.py)

## Approach

For each possible knight count k, count intervals containing k; feasibility requires this count to equal k. To choose the lexicographically smallest feasible indicator vector, process people in order and retain candidates outside their interval whenever any exist. A Fenwick tree counts remaining candidates and a successor DSU deletes each candidate at most once.

## Complexity

- Time: O(N log N).
- Space: O(N).
