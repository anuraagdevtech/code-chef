---
topic: Number Theory
subtopic: An invariant from step size and parity
time: $O(1)$ per test case
space: $O(1)$
---
Both move **exactly** $K$ every second, so after $t$ seconds the policeman stands at $x + K p$ and the thief at $y + K q$, where $p$ and $q$ are sums of $t$ terms of $\pm 1$ — hence both have the **same parity as $t$**.

Meeting requires $x + Kp = y + Kq$, that is

$$x - y = K\,(q - p)$$

Two conditions fall out. First, $K$ must divide $x - y$. Second, $q - p$ is a difference of two integers of equal parity, so it is **even** — meaning $(x-y)/K$ must be even too.

Together:

$$K \mid (x - y) \quad\text{and}\quad \frac{x - y}{K} \text{ is even}$$

Both are invariants no evasion can break, so when either fails the answer is `No` regardless of play. When both hold, the policeman can close the gap and pin the thief against a wall, so the answer is `Yes`.

The parity half is the easily missed one, and the samples target it. Case 1 has adjacent positions with $K = 1$: the gap is $1$, odd, so they swap places forever and never coincide. Case 2 has a gap of $3$ with $K = 1$ — divisible, but odd — also `No`. Case 3 has a gap of $2$, even, giving `Yes`.

Cases 4 and 5 show the divisibility doing work: gaps of $4$ and $6$ against steps of $2$ and $3$ give quotients $2$ and $2$, both even.

Note the simultaneous-move rule means they can pass *through* each other without meeting, which is exactly what the parity obstruction encodes.

## Edge cases

- **Both displacements share the parity of the elapsed time.** After $t$ seconds each has moved $\pm K$ exactly $t$ times, so each net displacement is $K$ times an integer congruent to $t$ modulo $2$ — making their difference an *even* multiple of $K$.
- **So the gap must be divisible by $K$ and the quotient must be even.** Both halves are needed: the second row has $|x-y| = 3$, divisible by $K = 1$ but with an odd quotient, so `No`.
- **A divisibility failure alone** is enough to answer `No` when $K > 1$ and the gap is not a multiple.
- **An odd gap with $K = 1$ is always hopeless** (the first row), since the quotient is the gap itself.
- **The board bounds do not matter.** $K \leq N$ is guaranteed, so both can always oscillate within $[0, N]$ without being forced into a corner — which is why $N$ is read and never used.
- **They may not meet mid-move**, only at the end of a second, which is exactly what the parity argument captures: positions are only ever compared at integer times.
- **$x \neq y$ is guaranteed**, so the gap is at least $1$ and the trivial "already caught" case does not arise.

## Dry run

| $x$ | $y$ | gap | $K$ | gap $\bmod K$ | quotient | quotient even? | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 0 | 1 | 1 | 1 | 0 | 1 | no | `No` |
| 1 | 4 | 3 | 1 | 0 | 3 | no | `No` |
| 4 | 2 | 2 | 1 | 0 | 2 | **yes** | `Yes` |
| 3 | 7 | 4 | 2 | 0 | 2 | **yes** | `Yes` |
| 8 | 2 | 6 | 3 | 0 | 2 | **yes** | `Yes` |

In row 3 both step right then the policeman steps right again while the thief steps left: positions $4 \to 5 \to 4$ and $2 \to 3 \to 4$.
