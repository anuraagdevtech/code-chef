# Number of Factors (NUMFACT)

[Problem statement](https://www.codechef.com/problems/NUMFACT) · [Python solution](../../solutions/NUMFACT.py)

## Approach

Factor each input number and add exponents of equal primes. The number of divisors of the product is the product of all combined exponents plus one.

## Complexity

- Time: O(N sqrt(max A)).
- Space: O(number of distinct prime factors).
