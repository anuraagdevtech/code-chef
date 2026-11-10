# Digit Operation (DIGITOP)

[Problem statement](https://www.codechef.com/problems/DIGITOP) · [Python solution](../../solutions/DIGITOP.py)

## Approach

Every string must preserve its length. With at least two strings, free cross-string swaps can realize any permutation of all digit positions, including internal swaps via an outside position. The minimum paid replacements equal the total deficit across digit frequencies.

## Complexity

- Time: O(total digits).
- Space: O(total digits).
