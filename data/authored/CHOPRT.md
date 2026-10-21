---
topic: Conditionals & Case Work
subtopic: Three-way comparison
time: $O(1)$ per test case
space: $O(1)$
---
Print the relational operator describing how $A$ stands to $B$: `<` if $A$ is smaller, `>` if larger, `=` if equal. A three-branch comparison, with each outcome mapped to its symbol.

The three cases are mutually exclusive and exhaustive, so an `if / elif / else` covers the space exactly and the branch order carries no meaning. What *is* required is that the equality case get its own branch — collapsing it into one of the inequalities silently reports a strict relation for equal values.

Two practical notes for this particular problem. $A$ and $B$ reach $1000000001$, which is just past $2^{30}$ and over the $2{,}147{,}483{,}647$ ceiling of a signed 32-bit `int` only when summed — comparison itself is safe, but the bound is a hint that a C solution should use a wider type if it does any arithmetic. Python has no such concern.

With $T$ up to $10^4$, reading the whole stream at once and joining the output into a single write is worth doing; per-line `input()` and `print()` calls dominate the runtime in Python at this volume, even though the comparison itself is free.

The symbols must be printed bare, with no surrounding quotes — the problem statement quotes them only for clarity.

## Edge cases

- **$A = B$**: must print `=`, so the chain needs all three branches and not just a two-way test. Sample case 3 covers it.
- **Both at the bound** $A = B = 10^9 + 1$: equal, so `=`. Note the limit is $10^9 + 1$, one past the usual $10^9$ — still inside 32-bit range, but it is a deliberate nudge past the round number.
- **Both minimal** ($A = B = 1$): `=`.
- Only the *sign* of $A - B$ matters, so no subtraction overflow is possible even in a fixed-width language; comparing directly avoids the question entirely.

## Dry run

| $A$ | $B$ | relation | output |
|---:|---:|---|---|
| 10 | 20 | $A < B$ | `<` |
| 20 | 10 | $A > B$ | `>` |
| 10 | 10 | equal | `=` |

The three sample rows exercise all three branches in turn.
