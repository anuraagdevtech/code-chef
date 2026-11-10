# Art of Balance (ARTBALAN)

[Problem statement](https://www.codechef.com/problems/ARTBALAN) · [Python solution](../../solutions/ARTBALAN.py)

## Approach

Try each possible number d of distinct final letters dividing the length. Every selected letter then needs length/d occurrences. Keep as many characters as possible from the d largest original counts; all remaining positions require replacement.

## Complexity

- Time: O(length+26 squared).
- Space: O(26).
