# The Great Wall of Byteland (BWALL)

[Problem statement](https://www.codechef.com/problems/BWALL) · [Python solution](../../solutions/BWALL.py)

## Approach

Use a two-bit occupancy mask for the next column. Enumerate placements of the one-cell tile and all rotations of the L tromino to form a four-state transfer matrix. Binary exponentiation counts width-N tilings modulo 1000000007.

## Complexity

- Time: O(log N).
- Space: O(log N).
