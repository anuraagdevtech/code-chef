# Rectangles Counting (RECTCNT)

[Problem statement](https://www.codechef.com/problems/RECTCNT) · [Python solution](../../solutions/RECTCNT.py)

## Approach

At most two points share an x coordinate, so each column supplies at most one vertical side. Group these sides by their sorted y pair. A newly completed side makes one rectangle with every earlier side in its group. Input ends with N=0 and has no test count.

## Complexity

- Time: O(N) expected.
- Space: O(N).
