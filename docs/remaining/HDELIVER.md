# Home Delivery (HDELIVER)

[Problem statement](https://www.codechef.com/problems/HDELIVER) · [Python solution](../../solutions/HDELIVER.py)

## Approach

Union endpoints of fast roads. Delivery queries return YO exactly when both locations have the same representative. Locations are zero-based.

## Complexity

- Time: O((N+M+Q) alpha(N)).
- Space: O(N).
