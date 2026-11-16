---
topic: Graphs
subtopic: Connect component minima in a star
time: $O(N+M)$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Existing spaceways form connected components. Within each component, choose its cheapest nonnegative endpoint tax; negative-tax governments are forbidden. If a component has no allowed endpoint and there is more than one component, connecting the galaxy is impossible.

For component minima $c_1,\ldots,c_k$, an added edge costs the sum of its endpoint minima. Every component needs degree at least one in the connecting tree. Giving the remaining $k-2$ degrees to the globally cheapest component minimises the sum. A star attains total $\sum c_i+(k-2)\min c_i$.

## Edge cases

- An already-connected galaxy costs zero even if every tax is negative.
- A zero tax is an allowed endpoint.
- Reject an unusable component only when a connection is actually required.

## Dry run

The first sample has component minima one and two. One teleport costs `1+2=3`. In the second sample, one disconnected component has only negative taxes, so the result is `-1`.
