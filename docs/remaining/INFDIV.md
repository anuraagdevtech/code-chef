# E - Make it Zero (INFDIV)

[Problem statement](https://www.codechef.com/problems/INFDIV) · [Python solution](../../solutions/INFDIV.py)

## Approach

Scale expectations by n. For x<n, D[x]=(1+sum_(r<=x)D[x mod r])/x. Split divisors at sqrt(x); large divisors share a quotient and their remainders form an arithmetic progression. Store progression-prefix sums only up to floor(limit/(quotient+1)), bounding total storage. For initial m>=n the answer is 1+sum D[m mod r]. PyPy is recommended for the largest inputs.

## Complexity

- Time: O(N sqrt N).
- Space: O(N log N).
