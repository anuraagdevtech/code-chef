# 01 Subsequence (ZEROONE)

[Problem statement](https://www.codechef.com/problems/ZEROONE) · [Python solution](../../solutions/ZEROONE.py)

## Approach

Put zero-block lengths in decreasing order and one-block lengths in increasing order. Exchanging two out-of-order zero blocks moves more zeros before all intervening ones; the symmetric exchange moves larger one blocks after more zeros. Count subsequences with a running zero total.

## Complexity

- Time: O(N log N).
- Space: O(N).
