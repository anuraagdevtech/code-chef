# Optimal Denomination (MINNOTES)

[Problem statement](https://www.codechef.com/problems/MINNOTES) · [Python solution](../../solutions/MINNOTES.py)

## Approach

If employee i is changed, choose the denomination as the GCD of all other salaries and give i exactly one note. Prefix and suffix GCDs evaluate every excluded employee in linear many GCD operations. A single employee always needs one note.

## Complexity

- Time: O(N log max A).
- Space: O(N).
