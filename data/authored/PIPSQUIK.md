---
topic: Simulation
subtopic: Walking a sequence with a consumable resource
time: $O(N)$ per test case
space: $O(1)$
---
Each barrier is passed in one of three ways, tested in order.

- **Type 2** (ground up to height $X$): Edward jumps over it if $X \leq Y_2$.
- **Type 1** (height $X$ up to the sky): Edward ducks under it if $H - Y_1 \leq X$ — ducking lowers his effective height to $H - Y_1$.
- Otherwise he breaks it, spending one unit of life force.

The rule that decides this problem is the exhaustion clause: **if breaking a barrier leaves zero life force, he does not pass that barrier**. So the check is to decrement first and then test for zero, counting the barrier only if something remains.

Sample case 1 traces it exactly. The first three barriers are cleared by jumping, jumping and ducking. The fourth ($X=8$, too tall to jump) and fifth ($X=4$) are broken, dropping $L$ from $3$ to $1$. The sixth is a type-1 barrier at height $2$, below his ducked height of $4$, so he breaks it — and that takes $L$ to $0$, so he collapses on it. The answer is $5$, not $6$.

Sample case 3 is the same input with the last barrier raised to $X = 6$, which he can now duck under for free, so all $6$ are cleared. Sample case 2 is the minimal exhaustion case: one barrier, one life force, broken and he stops at $0$.

Note the "touching counts as passing" wording makes both comparisons **inclusive** — $X \leq Y_2$ and $H - Y_1 \leq X$. Using strict inequalities would fail sample case 1 on the very first barrier, where $X = 2$ equals $Y_2 = 2$.

## Edge cases

- **Touching counts as passing**, so both tests are inclusive. The first case's opening barrier is type $2$ at height $2$ with a jump of exactly $2$, and it is cleared.
- **The two barrier kinds compare in opposite directions.** A type $2$ barrier rises from the ground to $X$, so he needs $X \leq Y_2$; a type $1$ barrier hangs from $X$ upwards, so his ducked height $H - Y_1$ must satisfy $H - Y_1 \leq X$. Using one direction for both fails most cases.
- **A broken barrier is still passed — unless it drains the last life.** The statement is explicit: if no life force remains after the break, he cannot pass *that* barrier. So the loop breaks before incrementing, and the first case passes $5$ of $6$ despite breaking three.
- **Exhaustion on the very first barrier** (the second case: one life, one impassable barrier) → `0`.
- **Lives may survive to the end** (the third case finishes with one left and passes all six).
- **$H - Y_1$ is computed once**, since the ducked height never changes during a run.

## Dry run

First sample: $H = 5$, $Y_1 = 1$ (so ducked height $4$), $Y_2 = 2$, $L = 3$.

| barrier | type | $X$ | test | result | lives | passed |
|---:|---:|---:|---|---|---:|---:|
| 1 | 2 | 2 | $2 \leq 2$ | jump | 3 | 1 |
| 2 | 2 | 1 | $1 \leq 2$ | jump | 3 | 2 |
| 3 | 1 | 10 | $4 \leq 10$ | duck | 3 | 3 |
| 4 | 2 | 8 | $8 \leq 2$ fails | break | 2 | 4 |
| 5 | 2 | 4 | $4 \leq 2$ fails | break | 1 | 5 |
| 6 | 1 | 2 | $4 \leq 2$ fails | break, **exhausted** | 0 | 5 |

Output `5`.
