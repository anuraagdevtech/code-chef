# Subtree Removal (SUBREM)

[Problem statement](https://www.codechef.com/problems/SUBREM) · [Python solution](../../solutions/SUBREM.py)

## Approach

For each subtree, either delete it for profit -X or retain its root plus the optimal profits of all child subtrees. Compute these alternatives in reverse iterative traversal order; the root's value is the answer.

## Complexity

- Time: O(N).
- Space: O(N).
