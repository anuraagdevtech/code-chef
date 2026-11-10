# Special Triplets (SPCTRIPS)

[Problem statement](https://www.codechef.com/problems/SPCTRIPS) · [Python solution](../../solutions/SPCTRIPS.py)

## Approach

Write B=k*C with k>=2. The permitted A values are C,C+B,C+2B,... up to N, so this (B,C) contributes floor((N-C)/B)+1. Enumerate C and its eligible multiples B.

## Complexity

- Time: O(N log N).
- Space: O(1).
