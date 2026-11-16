---
topic: Dynamic Programming
subtopic: Sliding reachability window and shortest-level prefix counts
time: $O(N)$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $dist[j]$ be the least number of drives to station $j$. Reachable predecessor stations form a sliding suffix interval of earlier stations. Distances are nondecreasing with station position, so its leftmost predecessor has the smallest distance. All predecessors with that distance give shortest routes to $j$.

Maintain the last processed index at each distance level and a prefix sum of route counts. This gives the sum of ways over the optimal predecessor interval in constant time. Advance the left boundary while stations fall out of fuel range. Subtract one from the final number of drives to obtain the number of intermediate stops.

## Edge cases

- Starting and destination stations are not intermediate stops.
- A direct drive gives zero stops and one route.
- Stations are already strictly increasing.
- The input guarantees every necessary gap is traversable.

## Dry run

In the sample, routes `0->1->4->7->10` and `0->3->4->7->10` both use four drives, hence three intermediate stops and two optimal plans.
