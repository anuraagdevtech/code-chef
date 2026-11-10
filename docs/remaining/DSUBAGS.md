# Queries with Bags (DSUBAGS)

[Problem statement](https://www.codechef.com/problems/DSUBAGS) · [Python solution](../../solutions/DSUBAGS.py)

## Approach

Use a disjoint-set union structure with path compression and union by size. Equality queries compare representatives; successful unions decrement a separately maintained bag count.

## Complexity

- Time: O((N+Q) alpha(N)).
- Space: O(N).
