---
topic: Arrays
subtopic: 2D sliding-window maximum with monotone deques plus 2D prefix sums
time: $O(Q \cdot N \cdot M)$, with repeated query sizes answered from a cache
space: $O(N \cdot M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Elements can only be increased, so the cheapest way to equalise an $a \times b$ block is to raise everything to the block maximum. Its cost is $a \cdot b \cdot \max - \text{sum}$, and the answer to a query is the minimum of that over all positions of the block.

The block sum comes from a 2D prefix-sum table in $O(1)$. The block maximum is computed in two passes of the monotone-deque sliding-window maximum: first along every row with window width $b$, then down every column of those row maxima with window height $a$. Each pass is linear in the size of the matrix, so one query costs $O(N \cdot M)$. Queries with the same dimensions are answered from a dictionary.

## Edge cases

- A $1 \times 1$ query always costs 0.
- The block may be the whole matrix; then there is a single position.
- The deque comparison uses `<=` so equal values keep only the most recent index, which is safe for a maximum.
- Costs can exceed 32 bits when the block is large and values are spread out.

## Dry run

Sample matrix `1 8 3 4 / 5 2 3 1 / 3 6 2 2`, query `2 2`.

Row maxima for width 2: `8 8 4`, `5 3 3`, `6 6 2`. Column windows of height 2 over them give the block maxima `8 8 4` (rows 1-2) and `6 6 3` (rows 2-3).

The bottom-right block `3 1 / 2 2` has maximum 3 and sum 8, cost $4 \cdot 3 - 8 = 4$; every other block costs more. Answer 4.
