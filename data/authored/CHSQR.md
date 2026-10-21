---
topic: Constructive
subtopic: A shifted cyclic Latin square
time: $O(K^2)$ per test case
space: $O(K)$
---
**What $F(K)$ is.** Row $\frac{K+1}{2}$ — the centre row — contains exactly one $1$, somewhere in columns $1 \ldots K$. Its distance to the centre is purely horizontal and at most $\frac{K-1}{2}$. So

$$F(K) \leq \frac{K-1}{2}$$

and the task is to build a grid achieving it.

**The construction.** Take the cyclic Latin square shifted by $s = \frac{K+1}{2}$:

$$L[r][c] = \bigl((c - r - s) \bmod K\bigr) + 1 \qquad (0\text{-indexed})$$

Each row is a rotation of $1 \ldots K$ and each column likewise, so it is a valid Latin square by construction. The $1$s sit exactly where $c \equiv r + s \pmod K$ — a diagonal wrapped by half the board.

Checking the distances with $m = \frac{K-1}{2}$ as the centre index: the row $r = m$ places its $1$ at column $0$, distance $m$; rows $m+1$ and $K-1$ also give $m$; and every other row gives $m+1$ or more. So the minimum is exactly $m$, meeting the bound.

The half-board shift is what matters. The *unshifted* cyclic square puts its $1$s on the main diagonal, which passes straight through the centre — distance $0$, the worst possible. Rotating by $\frac{K+1}{2}$ pushes the diagonal as far from the centre as it can go.

$K = 1$ falls out correctly: the single cell is the centre and holds $1$, so $F(1) = 0$.

For $K = 3$ this yields

```
2 3 1
1 2 3
3 1 2
```

whose nearest $1$ to the centre is at distance $1 = F(3)$. The published sample is a different grid with the same property — **any** valid answer is accepted, so this is judged by a checker.

## Edge cases

- **$K$ is odd**, so the centre is a single cell at $((K-1)/2, (K-1)/2)$ and the distance to the nearest $1$ is well defined — an even $K$ would have four central cells and a different answer.
- **A Latin square forces a $1$ in every row**, so the nearest one can never be far: within $\lceil K/2 \rceil$ rows of the centre there must be a $1$, and the construction pushes it as far as that allows.
- **$K = 1$** is the degenerate case: the only cell holds $1$ and sits at the centre, so the distance is $0$.
- **The shift by $(K+1)/2$ is what maximises the distance.** A plain cyclic square $((c - r) \bmod K) + 1$ puts a $1$ on the main diagonal, which passes straight through the centre; shifting the diagonal moves it off.
- **Python's `%` on a negative operand returns a non-negative result**, which is what keeps `(c - r - s) % k` in range without an explicit `+ k`.
- **This square differs from the sample's** at $K = 3$ (`2 3 1 / 1 2 3 / 3 1 2` against `3 2 1 / 1 3 2 / 2 1 3`), but the $1$s sit in the same three cells, so both achieve the same $F(K)$ — a special judge measures the distance.

## Dry run

$K = 3$, so the shift is $s = 2$ and the centre is cell $(1,1)$ (0-based).

| row | row contents | position of the $1$ | distance to centre |
|---:|---|---|---:|
| 0 | `2 3 1` | $(0, 2)$ | 2 |
| 1 | `1 2 3` | $(1, 0)$ | **1** |
| 2 | `3 1 2` | $(2, 1)$ | **1** |

The closest $1$ is one step away, which is the best a $3 \times 3$ Latin square allows.
