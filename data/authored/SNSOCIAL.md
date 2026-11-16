---
topic: Graphs
subtopic: Multi-source BFS from all maximum-wealth cells
time: $O(NM)$ per test case
space: $O(NM)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The global maximum wealth cannot be exceeded. After one hour it spreads to all eight neighbours of every cell already holding it. Consequently, a cell reaches the maximum after its shortest eight-neighbour distance from any initially maximal cell.

Start a BFS with all maximum cells at distance zero. Its largest assigned distance is the first hour at which the entire grid has the maximum. Each cell is enqueued once.

## Edge cases

- Already-equal grids need zero hours.
- Diagonal neighbours count.
- Start from every maximum, not just the first one.

## Dry run

For a two-by-two grid with only its bottom-right cell maximal, every other cell is a side or diagonal neighbour. BFS gives maximum distance one.
