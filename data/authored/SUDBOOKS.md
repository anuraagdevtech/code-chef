---
topic: Simulation
subtopic: A stack, with an empty-pop guard
time: $O(1)$ per query
space: $O(Q)$
---
Books are inserted and removed only from the top, which is the definition of a **stack** (last in, first out). Python's `list` is exactly that: `append` pushes and `pop` removes the most recent element, both in amortised $O(1)$.

So the whole problem is two cases:

- `1 N` → `append(N)`, printing nothing;
- `-1` → `pop()` and print the value, or print `kuchbhi?` when the shelf is empty.

The empty check is the only real requirement — calling `pop` on an empty list raises `IndexError`, so the guard is not defensive padding but necessary for correctness on valid input.

The sample exercises it: two books go on, both come off in reverse order (`45` then `2`), and the third removal finds nothing left.

With $Q$ up to $10^6$, the dominant cost is **I/O**, not the stack. Reading the whole stream at once and collecting the outputs into a list for a single joined write avoids a million separate `input()` and `print()` calls, which would otherwise dominate the runtime by an order of magnitude.

Note the input is not uniformly shaped — a type-1 query occupies two tokens and a type-2 query only one — so the parser advances a cursor by a variable amount rather than reading fixed-size records.
