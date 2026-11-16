---
topic: Disjoint Set Union
subtopic: Path compression and union by size
time: $O((N+Q)\alpha(N))$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A DSU component represents one bag of merged cards. Store parent pointers and component sizes. Find representatives with path compression and attach the smaller component to the larger during a merge.

Maintain the number of components, decreasing it only for merges between distinct representatives. Connectivity queries compare representatives; type-three queries read the maintained count.

## Edge cases

- Repeating a merge does not decrease the bag count.
- The input has one case, without a test-count prefix.
- A card is always connected to itself.

## Dry run

The sample starts with three components. Merging 1 and 2 changes the count to two; merging 2 and 3 changes it to one. Connectivity of 1 and 3 then returns `YES`.
