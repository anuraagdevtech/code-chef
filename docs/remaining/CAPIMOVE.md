# Capital Movement (CAPIMOVE)

[Problem statement](https://www.codechef.com/problems/CAPIMOVE) · [Python solution](../../solutions/CAPIMOVE.py)

## Approach

Sort planets by decreasing population. For each vertex mark itself and its neighbors, then take the first unmarked planet. At most degree(v)+1 rejected candidates are scanned, so all scans together are linear after sorting.

## Complexity

- Time: O(N log N).
- Space: O(N).
