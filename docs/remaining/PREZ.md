# Prefix Zeros (PREZ)

[Problem statement](https://www.codechef.com/problems/PREZ) · [Python solution](../../solutions/PREZ.py)

## Approach

For prefix ending at r, its minimum cost is (-S_r mod 10) plus the sum of (S_(i+1)-S_i mod 10) over earlier adjacent pairs. Extending the prefix updates this cost in constant time; it never decreases, so stop when the budget is exceeded.

## Complexity

- Time: O(N).
- Space: O(N).
