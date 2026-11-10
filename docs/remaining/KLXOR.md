# Again XOR problem (KLXOR)

[Problem statement](https://www.codechef.com/problems/KLXOR) · [Python solution](../../solutions/KLXOR.py)

## Approach

Output position j is the XOR of the N-K+1 source bits beginning at j. Slide this fixed-width parity window across the K output positions and count its odd parities.

## Complexity

- Time: O(N).
- Space: O(N).
