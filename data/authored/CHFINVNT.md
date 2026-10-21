---
topic: Basic Math
subtopic: Counting residues below a threshold in closed form
time: $O(1)$ per test case
space: $O(1)$
---
The testing order groups indices by residue: first every $i \equiv 0$, then every $i \equiv 1$, and so on, each group in increasing order. So the day gas $p$ is tested is

$$\text{day} = \#\{\,i < N : i \bmod K < r\,\} \;+\; \left\lfloor \frac{p}{K} \right\rfloor + 1$$

where $r = p \bmod K$. The second term is $p$'s rank inside its own group — $p$ is the $(\lfloor p/K \rfloor + 1)$-th index with that residue — and the first counts everything tested in earlier groups.

That count cannot be summed group by group, since $K$ reaches $10^9$. Split $[0, N)$ into complete blocks of $K$ instead: with $q = \lfloor N/K \rfloor$ and $\rho = N \bmod K$, each complete block contributes exactly $r$ indices with residue below $r$, and the trailing partial block holds residues $0 \ldots \rho-1$, contributing $\min(r, \rho)$:

$$\#\{\,i < N : i \bmod K < r\,\} = qr + \min(r, \rho)$$

The $\min$ is the part that is easy to get wrong — the last block is short, so it may not contain all $r$ of the small residues.

Working through the statement's worked example, $N = 5$, $p = 2$, $K = 3$: $r = 2$, $q = 1$, $\rho = 2$, so earlier groups cover $1 \cdot 2 + 2 = 4$ indices and $p$ is first in its group, giving day $5$.

The samples show the ordering effect clearly: with $N = 10$ and $K = 5$, gas $5$ is tested on day $2$ (it is second in group $0$, after gas $0$), while gas $4$ waits until day $9$ because its residue group is last.

## Edge cases

- **The order is by residue first, then by index**, so the gases tested before $p$ are all those with a smaller residue plus those sharing $p$'s residue at a smaller index.
- **The short tail is where the arithmetic bites.** Among $0 \dots N-1$ each residue appears $\lfloor N/K \rfloor$ times, and the first $N \bmod K$ residues get one extra — so the count of smaller residues is $\lfloor N/K \rfloor \cdot r + \min(r, N \bmod K)$, not simply $\lfloor N/K \rfloor \cdot r$.
- **$p$ itself must be counted**, hence the trailing $+1$: the answer is a 1-based position.
- **$r = 0$** (the first row, $p = 5$ with $K = 5$) means nothing precedes $p$'s residue class, so the answer is just $p/K + 1 = 2$.
- **$K$ larger than $N$** makes every residue class a singleton, so the answer is $p + 1$.
- **$K = 1$** puts everything in one class and the answer is $p + 1$ as well.
- **$N, K$ up to $10^9$** with $T$ up to $10^5$, so the closed form replaces any simulation.

## Dry run

Third sample: $N = 10$, $p = 4$, $K = 5$. Residue $r = 4$, with $\lfloor N/K \rfloor = 2$ and $N \bmod K = 0$.

| residue | indices tested | count |
|---:|---|---:|
| 0 | $0, 5$ | 2 |
| 1 | $1, 6$ | 2 |
| 2 | $2, 7$ | 2 |
| 3 | $3, 8$ | 2 |
| 4 | $4$, then $9$ | — |

Eight gases precede residue $4$, none shares it at a lower index, so $p = 4$ is tested $9$th. Output `9`.
