---
topic: Basic Math
subtopic: Checkerboard parity across alternating moves
time: $O(1)$ per test case
space: $O(1)$
---
Colour the grid like a checkerboard. Every step flips colour, so after Alice's $k$-th move her colour is $kX \bmod 2$ starting from $(1,1)$, and after Bob's $(k-1)$-th move his is $(N+M) + (k-1)Y \bmod 2$ starting from $(N,M)$. Meeting right after Alice's $k$-th move requires equal colours:

$$kX \;\equiv\; (N+M) + (k-1)Y \pmod 2$$

Distance is never the obstacle. With $N, M \geq 2$ every cell has a neighbour, so either walker can burn two steps going back and forth, and for large enough $k$ the step budget covers the whole grid. So parity is the *only* constraint, and the question is whether some $k \geq 1$ satisfies the congruence.

Reading it mod $2$ with $x = X \bmod 2$ and $y = Y \bmod 2$:

- $x \neq y$: the left side's dependence on $k$ survives, so one of the two parities of $k$ works. Always `Yes`.
- $x = y$: the $k$ terms combine to a constant — $0$ when both are even, $1$ when both are odd — so the answer is `Yes` exactly when $N + M$ matches that constant, i.e. when $N + M \equiv X \pmod 2$.

The samples are all on a tiny grid, which is where parity is starkest. $2\,2\,1\,1$ fails because both move lengths are odd while $N+M = 4$ is even — Alice is always on her starting colour after an odd-length move pair, and Bob is always on the opposite one. Changing Alice's move to $2$ steps, or Bob's to $2$, makes the parities differ and the answer flips to `Yes`. And $2\,3\,3\,3$ has both odd with $N+M = 5$ odd, which matches.

## Edge cases

- **The grid is a checkerboard and each step flips colour**, so Alice's colour after $k$ moves shifts by $kX$ and Bob's by $(k-1)Y$ — they can only share a cell when those parities agree.
- **Equal move parities fix the gap.** If $X \equiv Y$, then $kX - (k-1)Y \equiv X \pmod 2$ for every $k$, so meeting requires $(N+M) \equiv X \pmod 2$ and no choice of $k$ can help.
- **Unequal move parities let $k$ choose the colour.** If $X \not\equiv Y$ the expression is $k + Y \pmod 2$, so some $k$ always works and the answer is `Yes` regardless of the grid.
- **They must meet right after Alice's move**, which is why Bob has made $k-1$ moves and not $k$ — the asymmetry is what puts $Y$ in the odd-parity branch.
- **Steps may be wasted**, since $N, M \geq 2$ always leaves a neighbour to bounce off, so distance is never an obstacle and only parity matters.
- **$X$ and $Y$ reach $10^9$** while only their parities are used.
- **The second sample row is the sole `No`**: both moves odd, and $(N+M)$ even against an odd $X$.

## Dry run

| $N$ | $M$ | $X$ | $Y$ | parities | condition | output |
|---:|---:|---:|---:|---|---|---|
| 2 | 2 | 2 | 1 | differ | $k$ is free | `Yes` |
| 2 | 2 | 1 | 1 | same | $(N{+}M) \bmod 2 = 0 \neq 1$ | `No` |
| 2 | 2 | 1 | 2 | differ | $k$ is free | `Yes` |
| 2 | 3 | 3 | 3 | same | $(N{+}M) \bmod 2 = 1 = 1$ ✓ | `Yes` |

In the second row Alice always lands on a colour Bob has just left.
