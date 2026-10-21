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

## Edge cases

- **Popping an empty shelf prints `kuchbhi?`** rather than raising `IndexError` — the third `-1` in the sample, after both books have been taken.
- **The two query types have different token counts** (type $1$ takes two tokens, type $-1$ one), so the stream must be consumed by type; a fixed stride of two desynchronises the whole input.
- **Last in, first out**: $45$ was pushed second and comes out first.
- **$Q$ up to $10^6$** — the output is joined once at the end rather than printed per query, and the whole input is read in a single buffered call.
- **$N$ up to $10^9$**: the values are only stored and echoed, so they are kept as raw byte tokens and never parsed into integers.
- **A run of pushes with no pops** produces no output at all; the output line count equals the number of $-1$ queries, not $Q$.

## Dry run

| query | shelf after (bottom → top) | output |
|---|---|---|
| `1 2` | $2$ | — |
| `1 45` | $2, 45$ | — |
| `-1` | $2$ | `45` |
| `-1` | empty | `2` |
| `-1` | empty | `kuchbhi?` |
