# Petersen Graph (PETERSEN)

[Problem statement](https://www.codechef.com/problems/PETERSEN) · [Python solution](../../solutions/PETERSEN.py)

## Approach

Each vertex has at most one neighbor with any requested letter. Try the smaller starting vertex carrying the first letter, then its larger counterpart. Every subsequent step is forced, so the first complete walk is lexicographically smallest.

## Complexity

- Time: O(length).
- Space: O(length).
