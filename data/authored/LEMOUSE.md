---
topic: Dynamic Programming
subtopic: Grid path DP that remembers the last move to avoid double counting
time: $O(N \cdot M)$ per test case
space: $O(N \cdot M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A mouse scares the elephant when its cell is on the path or adjacent to a path cell. Counting the mice near each path cell separately would count some of them several times, so the DP has to know which of them were already counted.

The plus-shaped neighbourhood of a new path cell can only overlap the neighbourhoods of the previous two path cells: anything earlier on a monotone path is at Manhattan distance at least 3. The state is therefore the current cell together with the direction of the move that entered it, which identifies the previous cell. When stepping to a new cell, add the mice in its neighbourhood that are not in the neighbourhood of the current cell or of the cell before it.

The answer is the smaller of the two states at the bottom-right corner.

## Edge cases

- The start cell has no previous cell; both direction states are initialised with the mice around $(0, 0)$.
- Neighbourhoods are clipped at the border of the board.
- A mouse on the path itself counts too - the neighbourhood includes the cell.
- Rows are strings, so cells are compared with the character `1`, not the integer.

## Dry run

Board `01 / 10`. Around the start $(0,0)$ there are two mice, at $(0,1)$ and $(1,0)$, so the initial value is 2.

Moving right to $(0,1)$: its neighbourhood is $\{(0,1), (0,0), (1,1)\}$; the only mouse there, $(0,1)$, was already counted - still 2. Moving down to $(1,1)$: its neighbourhood adds nothing new - still 2. The path that goes down first is symmetric.

Answer 2.
