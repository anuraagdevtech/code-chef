# Chef and Polygon Cakes (PCJ18C)

[Problem statement](https://www.codechef.com/problems/PCJ18C) · [Python solution](../../solutions/PCJ18C.py)

## Approach

The interior-angle sum is 180(N-2). Solve the arithmetic-progression sum for the common difference, substitute into A+(K-1)d, and reduce the exact numerator and denominator by their GCD. Integer arithmetic avoids rounding.

## Complexity

- Time: O(log(N A)).
- Space: O(1).
