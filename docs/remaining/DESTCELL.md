# Destroy Cells (DESTCELL)

[Problem statement](https://www.codechef.com/problems/DESTCELL) · [Python solution](../../solutions/DESTCELL.py)

## Approach

For step K+1 each hero destroys ceil(NM/step) cells. Iterate the first hero's destroyed indices and test whether their column-major indices are also divisible by step. Subtract this intersection from twice the individual count; harmonic iteration gives the stated bound.

## Complexity

- Time: O(NM log(NM)).
- Space: O(NM).
