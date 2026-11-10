# String Reverse (STR_REVERSE)

[Problem statement](https://www.codechef.com/problems/STR_REVERSE) · [Python solution](../../solutions/STR_REVERSE.py)

## Approach

Characters never moved must retain their original order and become a prefix of the reversed target. Greedily match the longest such target prefix as a subsequence of the original string; every other character must be moved once.

## Complexity

- Time: O(length).
- Space: O(length).
