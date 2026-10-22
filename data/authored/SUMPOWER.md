---
topic: Prefix Sums
subtopic: Counting each boundary's contribution
time: $O(N)$ per test case
space: $O(1)$
---
Board slot $j$ shows $S_{i+j}$ at step $i$ and $S_{i+j+1}$ at step $i+1$, so it changes exactly when those two characters differ. The power of one switch is therefore the number of **adjacent mismatches** inside a window:

$$\text{power}(i) = \sum_{p=i}^{i+K-1} d_p, \qquad d_p = [\,S_p \neq S_{p+1}\,]$$

Summing over all $N-K$ switches and swapping the order of summation turns the double sum into a weighted single sum: each boundary $p$ is counted once for every step $i$ whose window covers it, that is for $i \in [\max(1, p-K+1),\ \min(N-K, p)]$. So

$$\text{answer} = \sum_{p=1}^{N-1} d_p \cdot \Bigl(\min(N-K,\, p) - \max(1,\, p-K+1) + 1\Bigr)$$

with negative weights clamped to zero. Counting by contribution is what makes this linear — evaluating each window separately would be $O(NK)$, which at $\sum N = 10^6$ and $K$ near $N$ is hopeless.

A boundary near either end of the string gets a smaller weight, because fewer windows reach it; interior boundaries get the full $\min(K, N-K)$.

The samples make the weights visible. `aabbcc` with $K = 3$ has mismatches at $p = 2$ and $p = 4$, each covered by two of the three steps, giving $4$. `abccc` with $K = 2$ has mismatches at $p = 1$ and $p = 2$, weighted $1$ and $2$, giving $3$. And `aabb` with $K = 3$ has a single switch and a single mismatch inside it, giving $1$.

## Edge cases

- **Count by boundary, not by step.** A board cell changes between steps $i$ and $i+1$ exactly when the two characters it shows differ, so each adjacent pair $(S_p, S_{p+1})$ of different letters contributes once for every window that spans it.
- **The window count for boundary $p$ is $\min(N-K,\, p) - \max(1,\, p-K+1) + 1$**, clipped at both ends — the step index must stay within $1 \dots N-K$ and the boundary must fall inside the window.
- **Equal adjacent characters contribute nothing**, however many windows cover them, which is what makes `aabbcc` cheaper than an alternating string of the same length.
- **Boundaries near the ends are covered by fewer windows**, which the clipping captures: in the second sample the first boundary is seen once and the second twice.
- **$N > K$ is guaranteed**, so there is at least one transition and the step count is positive.
- **A clip can empty the interval**, hence the explicit guard, though with $N > K$ every interior boundary has at least one covering window.
- **Sum of $N \leq 10^6$**: one pass over the boundaries with constant work each.

## Dry run

First sample: $N = 6$, $K = 3$, $S = $ `aabbcc`, so there are $3$ transitions.

| boundary $p$ | $S_p, S_{p+1}$ | differ? | windows covering it | contribution |
|---:|---|:---:|---|---:|
| 1 | `a`, `a` | no | — | 0 |
| 2 | `a`, `b` | yes | steps $1, 2$ | 2 |
| 3 | `b`, `b` | no | — | 0 |
| 4 | `b`, `c` | yes | steps $2, 3$ | 2 |
| 5 | `c`, `c` | no | — | 0 |

Total `4`.
