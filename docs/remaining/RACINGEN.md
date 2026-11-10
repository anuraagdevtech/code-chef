# Racing (RACINGEN)

[Problem statement](https://www.codechef.com/problems/RACINGEN) · [Python solution](../../solutions/RACINGEN.py)

## Approach

Convert minutes to seconds. Running requires 60R energy units. The first X units are free; every additional unit needs one second of rest. Thus the minimum elapsed time is 60R+max(0,60R-X), attainable by alternating rest and running once energy is exhausted.

## Complexity

- Time: O(1).
- Space: O(1).
