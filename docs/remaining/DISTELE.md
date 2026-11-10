# Distinct Elements (DISTELE)

[Problem statement](https://www.codechef.com/problems/DISTELE) · [Python solution](../../solutions/DISTELE.py)

## Approach

For a value occurring f times, a distinct-valued subsequence chooses either no occurrence or one of its f indices. Multiply all f+1 choices modulo 1000000007 and remove the empty subsequence.

## Complexity

- Time: O(N) expected.
- Space: O(N).
