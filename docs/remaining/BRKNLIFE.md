# Broken Life (BRKNLIFE)

[Problem statement](https://www.codechef.com/problems/BRKNLIFE) · [Python solution](../../solutions/BRKNLIFE.py)

## Approach

Scan the fixed characters while greedily matching A. Replace every question mark with a letter different from the next unmatched character of A, so it cannot advance that match. If even the fixed characters complete A, no replacement can avoid the forbidden subsequence.

## Complexity

- Time: O(N+M).
- Space: O(N+M).
