---
topic: Number Theory
subtopic: Cyclic state via modulo
time: $O(1)$ per test case
space: $O(1)$
---
The three sizes form a closed cycle: `normal` → `huge` → `small` → `normal`. Because the cycle has length $3$, eating three mushrooms returns Mario to exactly where he started, so only $X \bmod 3$ matters.

Starting from `normal`, the mapping is

| $X \bmod 3$ | size |
|---|---|
| $0$ | `NORMAL` |
| $1$ | `HUGE` |
| $2$ | `SMALL` |

so the answer is a lookup into the list `["NORMAL", "HUGE", "SMALL"]` at index `x % 3`.

Simulating the $X$ steps in a loop would also pass at these bounds, but the modulo is both $O(1)$ and the idea that transfers: whenever a process returns to its initial state after a fixed number of steps, the step count collapses modulo the cycle length. With $X$ up to $10^9$ the loop would be hopeless and the modulo unchanged.

The ordering of the lookup table encodes the starting point. Mario begins `normal`, so index $0$ must be `NORMAL`; had he started `small` the same cycle would need its table rotated. Writing the table in cycle order starting from the initial state is what keeps this correct.

Check $X = 4$: $4 \bmod 3 = 1$, giving `HUGE` — one full cycle plus one step.
