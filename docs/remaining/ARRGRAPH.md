# Graph on an Array (ARRGRAPH)

[Problem statement](https://www.codechef.com/problems/ARRGRAPH) · [Python solution](../../solutions/ARRGRAPH.py)

## Approach

Check connectivity in the coprimality graph. If disconnected, one change suffices: insert 47 unless it already occurs, otherwise insert 43. A present 47 can only lie in a disconnected component when all entries are 47, so 43 handles that case.

## Complexity

- Time: O(N squared log 50).
- Space: O(N).
