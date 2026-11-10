# K-Concatenation (KCON)

[Problem statement](https://www.codechef.com/problems/KCON) · [Python solution](../../solutions/KCON.py)

## Approach

For one copy use nonempty Kadane. For at least two copies, run Kadane over two copies to cover all boundary shapes. If the original total is positive, every additional complete middle copy improves that optimum by the total; otherwise it adds nothing.

## Complexity

- Time: O(N).
- Space: O(N).
