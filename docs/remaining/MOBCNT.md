# Counting Mobiles (MOBCNT)

[Problem statement](https://www.codechef.com/problems/MOBCNT) · [Python solution](../../solutions/MOBCNT.py)

## Approach

At depth d every mobile leaf has weight total/2^d. Starting with one root slot, choose which available ordered slots are leaves of the current weight, then double the unused slots for the next depth. Multiply binomial choices; impossible weights, excessive slots or leftover leaves yield zero.

## Complexity

- Time: O(N+log(sum A)).
- Space: O(N).
