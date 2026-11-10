# Little Elephant and Bamboo (LEBAMBOO)

[Problem statement](https://www.codechef.com/problems/LEBAMBOO) · [Python solution](../../solutions/LEBAMBOO.py)

## Approach

After t operations, a stem selected x_i times changes by t-2x_i. For N>2 the sum of desired changes forces t=sum(D-H)/(N-2). Check integrality, nonnegativity and parity of every x_i. For N=2 the sum is invariant; for N=1 only decreases are possible.

## Complexity

- Time: O(N).
- Space: O(N).
