---
topic: Trees
subtopic: Follow one burning branch while shielding its sibling
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Root the fire's component at the initial burning bush. The degree bounds give every vertex at most two children. An initial shield anywhere below a child can be moved up to that child without saving fewer marked bushes, so an optimal first shield may protect an entire child subtree. That subtree remains safe after its parent burns out; only the other child can continue burning.

A marked burning vertex is failure. An unmarked vertex with zero or one child is success because its only possible continuation can be shielded. With two children, choose which child to shield and recurse into the other. A reverse-order boolean DP therefore uses `safe[u] = not marked[u] and (child_count < 2 or any(safe[child]))`.

## Edge cases

- The initially burning bush cannot be saved.
- Unmarked bushes may be sacrificed.
- Disconnected components never reached by the fire are already safe.
- Input contains blank lines, handled by tokenisation.

## Dry run

In sample three, shield subtree 2 while bush 1 burns. Fire reaches 3; then shield marked bush 7 and allow unmarked leaf 6 to burn. All marked bushes are saved.
