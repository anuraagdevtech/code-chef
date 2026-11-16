---
topic: Graphs
subtopic: BFS with each equal-digit group expanded once
time: $O(N)$ overall
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Positions are vertices. Adjacent positions and positions with the same digit are connected by unit-cost jumps. Ordinary BFS yields the shortest route, but explicitly adding every equal-digit edge could be quadratic.

Store the positions of each of the ten digits. The first time BFS visits a digit, enqueue every still-unvisited position in its group and clear that group. Later expansions cannot improve those distances, so each position participates in one group expansion and at most two adjacency checks.

## Edge cases

- A one-character string requires zero jumps.
- Equal first and last digits allow a direct one-jump route.
- Clear each digit group after its first expansion.

## Dry run

For `01234567890`, positions zero and ten both contain zero. Expanding the initial digit group immediately reaches the last position at distance one.
