---
topic: Graphs
subtopic: 0-1 BFS where only unit-length added edges are ever needed
time: $O(N + M)$ per test case
space: $O(N + M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
An added edge between $a$ and $b$ costs $(a - b)^2$. Replacing it by the chain $a, a \pm 1, \dots, b$ of $|a - b|$ unit edges costs only $|a - b|$ and connects at least as much. So an optimal solution only buys edges between consecutive labels, each for cost 1.

That turns the task into a shortest path from 1 to $N$ in a graph with the original edges at weight 0 and an edge of weight 1 between every $i$ and $i + 1$. A 0-1 BFS with a deque - weight-0 relaxations go to the front, weight-1 relaxations to the back - computes it in linear time.

## Edge cases

- Vertices 1 and $N$ already connected: answer 0.
- No edges at all: the answer is $N - 1$.
- A path may walk "backwards" along the labels to reach a useful component.
- Buying the same unit edge twice never helps; the shortest path uses each at most once.

## Dry run

`N = 6`, edges `1-2, 3-2, 1-3`.

Vertices 1, 2, 3 are at distance 0. From 3, the unit edges to 4, 5, 6 cost 1 each: distances 1, 2, 3.

Answer 3.
