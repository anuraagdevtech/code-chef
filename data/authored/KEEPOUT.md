---
topic: Arrays
subtopic: Undo the insertions on a linked list of sorted posts
time: $O(N \log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Inserting a post splits a gap, and tracking the maximum gap under splits needs a heap or a sorted structure. Removing a post is much easier: it merges its two neighbouring gaps into one, so the maximum can only grow and is updated with a single comparison.

So start from the final picture: sort all posts together with the endpoints 0 and $M$, link them into a doubly linked list by sorted index and compute the largest gap. Then walk through the posts in reverse order of insertion: first record the current maximum as the answer for that prefix, then remove the post - its neighbours are read from the list in $O(1)$, the merged gap is compared with the maximum, and the two neighbours are linked to each other.

Reverse the recorded answers before printing.

## Edge cases

- The answer for the first $i$ posts is recorded before post $i$ is removed.
- The endpoints 0 and $M$ are never removed.
- Positions are distinct, so the position-to-index map is well defined.
- The only superlinear step is the initial sort.

## Dry run

`M = 25`, posts in order `10, 12, 5, 19`. Sorted points `0 5 10 12 19 25`, gaps `5 5 2 7 6`, maximum 7.

- record 7; remove 19: gap $25 - 12 = 13$, maximum 13
- record 13; remove 5: gap $10 - 0 = 10$, maximum 13
- record 13; remove 12: gap $25 - 10 = 15$, maximum 15
- record 15; remove 10

Reversed: `15 13 13 7`.
