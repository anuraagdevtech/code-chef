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
