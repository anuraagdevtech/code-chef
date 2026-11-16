---
topic: Binary Search
subtopic: Binary search on the Chebyshev radius with 2D prefix sums
time: $O(N \cdot M \cdot \log \max(N, M))$ per test case
space: $O(N \cdot M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
With distance $\max(|\Delta i|, |\Delta j|)$, the rooms within distance $d$ of the mentor's room form a $(2d+1) \times (2d+1)$ square centred there, clipped to the hotel. Everybody fits within distance $d$ of a given mentor room exactly when that room has positive capacity (the mentor needs a place) and the square's total capacity is at least $K + 1$; who sleeps where inside the square does not matter.

Feasibility is monotone in $d$, so binary search the smallest radius. One check walks over all rooms with positive capacity and reads the clipped square's sum from a 2D prefix-sum table in $O(1)$.

If the capacity of the whole hotel is below $K + 1$ the answer is $-1$; otherwise the radius $\max(N, M) - 1$, which covers everything from any room, is always feasible.

## Edge cases

- The mentor counts as a person: $K + 1$ places are needed.
- A room with capacity 0 cannot be the mentor's room even if its neighbourhood is large.
- Radius 0 means everybody shares the mentor's room.
- The matrix can be a single very long row or column; the prefix table is stored flat to handle any shape.

## Dry run

`1 x 7` hotel `2 1 0 1 3 0 1`, $K = 5$, so 6 places are needed.

- radius 2: the windows around the rooms with positive capacity hold `3 4 5 5 4` places - not enough.
- radius 3: the mentor in room 2 (capacity 1) reaches rooms 1-5 with total $2 + 1 + 0 + 1 + 3 = 7 \ge 6$.

Answer 3.
