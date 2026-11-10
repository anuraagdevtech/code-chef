# Cybalphabit (CAB)

[Problem statement](https://www.codechef.com/problems/CAB) · [Python solution](../../solutions/CAB.py)

## Approach

Represent K as powers of two. The initial set-bit decomposition uses the fewest characters; splitting a power into two equal smaller powers increases the character count by one without changing the score. Split until there are N characters, rejecting counts outside the feasible range.

## Complexity

- Time: O(N+26).
- Space: O(N).
