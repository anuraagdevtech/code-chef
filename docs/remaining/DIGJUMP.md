# Chef and Digit Jumps (DIGJUMP)

[Problem statement](https://www.codechef.com/problems/DIGJUMP) · [Python solution](../../solutions/DIGJUMP.py)

## Approach

BFS over positions using adjacent jumps and equal-digit jumps. Expand each digit's complete position list only once, then clear it; otherwise repeated equal-digit expansions would be quadratic.

## Complexity

- Time: O(length).
- Space: O(length).
