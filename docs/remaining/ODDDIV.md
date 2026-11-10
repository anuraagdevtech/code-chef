# Odd Divisors (ODDDIV)

[Problem statement](https://www.codechef.com/problems/ODDDIV) · [Python solution](../../solutions/ODDDIV.py)

## Approach

For every odd divisor d up to V=100000, add d to each of its multiples. Prefix-sum these odd-divisor sums so a range query is a subtraction.

## Complexity

- Time: O(V log V+T).
- Space: O(V).
