# Fence - INOI 2017 (TINOI17A)

[Problem statement](https://www.codechef.com/problems/TINOI17A) · [Python solution](../../solutions/TINOI17A.py)

## Approach

Flood-fill only cultivated coordinates stored in a hash set. Each missing orthogonal neighbor contributes one fence unit. Sum each component's exposed sides and take the largest, including boundaries around holes.

## Complexity

- Time: O(number of cultivated cells) expected.
- Space: O(number of cultivated cells).
