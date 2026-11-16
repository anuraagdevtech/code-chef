---
topic: Graphs
subtopic: Scan population order while marking each closed neighbourhood
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Sort vertices by descending population. For each possible infected vertex, temporarily mark itself and all its neighbours. The first unmarked vertex in population order is the best surviving capital; return zero if none remains.

If a scan skips $k$ vertices, all of them belong to that vertex's closed neighbourhood. Thus its scan is bounded by degree plus two. Summing tree degrees gives $2(N-1)$, so all scans together are linear after sorting. Timestamp marks avoid clearing a full array per vertex.

## Edge cases

- The infected vertex itself cannot be the capital.
- A star centre leaves no survivor.
- A one-vertex tree returns zero.

## Dry run

In the sample, infection at vertex 4 excludes vertices `3,4,5,6`. Among survivors `1,2`, vertex 2 has larger population, so its answer is 2.
