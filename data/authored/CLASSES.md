---
topic: Graphs
subtopic: BFS distances from the hostel, then the K nearest subjects
time: $O(N + M + S \log S)$ per test case
space: $O(N + M + S)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Chef returns to the hostel after every subject, so attending a subject taught in building $b$ costs exactly $2 \cdot \text{dist}(0, b)$, independently of the other subjects he attends and of their order.

All paths have length 1, so one breadth-first search from building 0 gives every distance. Map each subject to the distance of its building, sort, and take the $K$ smallest; the answer is twice their sum.

## Edge cases

- Several subjects may be taught in the same building; each still costs a full round trip.
- A subject taught in the hostel building itself costs 0.
- The graph is connected for the given inputs, so every subject is reachable.
- $K \le S$, so there are always enough subjects to choose from.

## Dry run

Third sample: edges `0-1, 0-2, 0-4, 1-3, 1-4, 2-5, 2-6`; subjects in buildings `1 2 3 5 6`; $K = 3$.

Distances from 0: buildings 1, 2, 4 at distance 1; buildings 3, 5, 6 at distance 2.

Subject distances sorted: `1 1 2 2 2`. The three smallest sum to 4, so the answer is 8.
