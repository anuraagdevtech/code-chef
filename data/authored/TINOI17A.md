---
topic: Graphs
subtopic: Sparse flood fill with exposed-side counting
time: $O(N)$ expected overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Store cultivated cells in a set rather than allocate the possibly enormous farm grid. Flood-fill each four-neighbour component. For every visited cell, count one fence unit for each of its four neighbours absent from the cultivated set.

Sum these exposed sides within each component and return the largest component perimeter. Keep membership and visited status separate, so already-visited cultivated neighbours never get counted as exposed.

## Edge cases

- No cultivated fields gives perimeter zero.
- Diagonal contact does not connect patches.
- Boundaries around internal uncultivated holes also need fencing.

## Dry run

The sample has an isolated cell of perimeter 4 and a connected eight-cell ring. The ring has outer perimeter 12 and inner perimeter 4, giving maximum 16.
