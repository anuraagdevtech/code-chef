# Cool Guys (COOLGUYS)

[Problem statement](https://www.codechef.com/problems/COOLGUYS) · [Python solution](../../solutions/COOLGUYS.py)

## Approach

The event gcd(A,B)=B means B divides A, giving sum floor(N/B) favorable ordered pairs out of N squared. The divisor hyperbola identity evaluates the sum as 2*sum_(i<=sqrt N)floor(N/i)-floor(sqrt N)^2. Reduce the resulting fraction exactly.

## Complexity

- Time: O(sqrt N).
- Space: O(1).
