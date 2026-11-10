# Treeversion (TREEVERS)

[Problem statement](https://www.codechef.com/problems/TREEVERS) · [Python solution](../../solutions/TREEVERS.py)

## Approach

For child subtrees A,B, placing A first creates ones(A)*zeros(B) cross inversions. Sort children by that exact pairwise comparison, then accumulate internal and cross inversions in postorder. Integer cross products avoid floating-point ordering errors.

## Complexity

- Time: O(N log N).
- Space: O(N).
