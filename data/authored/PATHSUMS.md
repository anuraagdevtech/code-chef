---
topic: Constructive
subtopic: Assign one and two to the two tree colour classes
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Two-colour the tree and assign value one to one class and value two to the other. Every path containing at least two vertices includes an edge, hence includes both values. Its average is strictly between one and two, so it cannot be an integer. Therefore the path sum is not divisible by its vertex count.

## Edge cases

- Single-vertex paths are excluded by the condition.
- Either colour may receive value one.
- Values one and two satisfy the output bound.

## Dry run

For path `1-2-3`, assign `[1,2,1]`. Its two-edge subpaths have sums 3 over two vertices, and the full path has sum 4 over three vertices; none is divisible by its length.
