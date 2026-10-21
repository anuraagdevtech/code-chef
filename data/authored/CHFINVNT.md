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
