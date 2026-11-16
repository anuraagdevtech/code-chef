---
topic: Graphs
subtopic: Orient an undirected Euler tour
time: $O(N+E)$ overall
space: $O(N+E)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A directed Euler circuit requires equal indegree and outdegree at every vertex. Reorienting preserves undirected degrees, so every degree must be even. The underlying graph must also be connected, including every city.

These conditions suffice. Traverse unused undirected edges using Hierholzer's algorithm and orient each edge in its traversal direction. Every even-degree vertex has equally many arrivals and departures, so the resulting connected directed graph has an Euler circuit from any city. Store directions by edge ID to preserve the input road order; opposite-direction parallel roads remain separate edges.

## Edge cases

- Any odd degree makes the answer `NO`.
- Isolated cities prevent visiting every city when other roads exist.
- Distinguish edges by ID, not endpoint pair.
- Print roads in the same order as the input.

## Dry run

For triangle `1-2,2-3,3-1`, every degree is two. Orienting the traversal `1->2->3->1` gives the required circuit.
