# Rendezvous (TR1)

[Problem statement](https://www.codechef.com/problems/TR1) · [Python solution](../../solutions/TR1.py)

## Approach

For a vertex v, ordered endpoint pairs whose LCA is v number size(v)^2 minus the sum of squared child-subtree sizes. Weight this count by the vertex label and sum modulo 1000000007.

## Complexity

- Time: O(N).
- Space: O(N).
