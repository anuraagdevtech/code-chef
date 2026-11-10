# Cosmic Temple (COSTEMP)

[Problem statement](https://www.codechef.com/problems/COSTEMP) · [Python solution](../../solutions/COSTEMP.py)

## Approach

A bottom-up pass computes subtree sizes and root distance sum. Rerooting across an edge into a subtree of size s decreases s distances and increases N-s distances, hence answer[child]=answer[parent]+N-2s. City labels are zero-based.

## Complexity

- Time: O(N).
- Space: O(N).
