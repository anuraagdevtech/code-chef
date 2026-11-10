# Chefland and Electricity (CHEFELEC)

[Problem statement](https://www.codechef.com/problems/CHEFELEC) · [Python solution](../../solutions/CHEFELEC.py)

## Approach

Start with the entire coordinate span connected. Between consecutive powered villages, remove the largest gap: both sides retain power and no other gap can save more wire. The unpowered prefix and suffix must remain connected to the nearest powered village.

## Complexity

- Time: O(N).
- Space: O(N).
