# Galactik Football (GALACTIK)

[Problem statement](https://www.codechef.com/problems/GALACTIK) · [Python solution](../../solutions/GALACTIK.py)

## Approach

Find connected components and the cheapest nonnegative-tax planet in each. Every component needs a teleport endpoint. Join all components in a star centered at the globally cheapest endpoint, costing sum(component minima)+(components-2)*globalMinimum. A component with no allowed endpoint makes reconnection impossible.

## Complexity

- Time: O((N+M) alpha(N)).
- Space: O(N).
