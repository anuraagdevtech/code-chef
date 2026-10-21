---
topic: Greedy
subtopic: Leftmost-feasible placement
time: $O(N)$ per test case
space: $O(N)$
---
Scan left to right and occupy a tower the moment it is legal — empty, with both neighbours empty. This leftmost-feasible greedy is optimal, and the exchange argument is short: if an optimal solution skips the first legal position $i$, it must leave $i$ free, and it can hold at most one occupant among $\{i, i+1\}$. Replacing that occupant (if any) with $i$ keeps the arrangement valid, since $i-1$ was already free, and does not reduce the count. Repeating pushes any optimum into the greedy's shape.

Placing as early as possible is what matters: a person at $i$ blocks only $i+1$ going forward, whereas a person at $i+1$ blocks $i+2$ as well, so the greedy never costs a later opportunity.

The implementation detail that matters is checking the **already-updated** left neighbour and the **original** right neighbour. Since the greedy writes its placements back into the string as it goes, a single array read handles both — but it means the string must be mutable, so the input is copied into a `bytearray`.

The guarantee that no two towers are initially adjacent means the starting configuration is already valid, so the greedy never has to repair anything.

In `010001` only index $3$ (0-based) qualifies: index $0$ is blocked by the occupant at $1$, and index $4$ is blocked by the occupant at $5$ — and after placing at $3$, index $4$ is doubly blocked. Hence $1$.

In `00101010000` the answer is $3$: index $0$ (its right neighbour being free), then the long tail `0000` at the end, which admits indices $8$ and $10$ — placing at $8$ rather than $9$ is exactly what leaves room for $10$.

## Edge cases

- **Placing as early as legal is optimal.** Any valid set of new towers can be shifted leftward one tower at a time without losing any, so the leftmost-feasible greedy matches the maximum — no lookahead is needed.
- **The ends have only one neighbour**, which the `j == 0` and `j == n - 1` guards cover; the second row places towers at both index $0$ and the final index $10$.
- **The string must be mutated as the scan proceeds**, or later positions will not see the towers just placed. In the second row, index $9$ is blocked solely by the tower placed at index $8$ a moment earlier.
- **The input is guaranteed to start valid** — no two consecutive towers are occupied — so no pre-check is needed and the greedy can begin immediately.
- **A `bytearray` keeps the mutation in place**, and comparing against the byte literals `0x30`/`0x31` avoids decoding up to a megabyte of input.
- **Sum of $N \leq 10^6$**: a single pass with no per-character object creation.

## Dry run

Second sample: `00101010000`, $N = 11$.

| index | char | left free | right free | place? | string becomes |
|---:|---|:---:|:---:|:---:|---|
| 0 | `0` | edge | yes | **yes** | `10101010000` |
| 1–7 | — | blocked by a neighbour | | no | — |
| 8 | `0` | yes | yes | **yes** | `10101010100` |
| 9 | `0` | **no** (just placed) | | no | — |
| 10 | `0` | yes | edge | **yes** | `10101010101` |

Output `3`.
