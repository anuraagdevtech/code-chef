# Path-etic Sums (PATHSUMS)

[Problem statement](https://www.codechef.com/problems/PATHSUMS) · [Python solution](../../solutions/PATHSUMS.py)

## Approach

Bipartition the tree and assign values one and two to opposite colors. Along every path the values alternate. An even path has average 1.5; an odd path of length at least three has a noninteger average strictly between one and two. Thus no allowed path sum is divisible by its length.

## Complexity

- Time: O(N).
- Space: O(N).
