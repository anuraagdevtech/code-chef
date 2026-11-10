# Per Capita Income (PERCAPTA)

[Problem statement](https://www.codechef.com/problems/PERCAPTA) · [Python solution](../../solutions/PERCAPTA.py)

## Approach

A weighted average cannot exceed the largest individual income-to-population ratio. Therefore keep only provinces attaining that ratio and choose their largest connected component. Compare ratios using cross multiplication.

## Complexity

- Time: O(N+M).
- Space: O(N+M).
