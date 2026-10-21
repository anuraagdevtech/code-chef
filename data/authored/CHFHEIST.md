---
topic: Basic Math
subtopic: Summing an arithmetic progression
time: $O(1)$ per test case
space: $O(1)$
---
The printing rate steps up every $d$ days: $P$ for the first block, $P + Q$ for the second, $P + 2Q$ for the third, and so on. Over $D$ days there are

$$f = \left\lfloor \frac{D}{d} \right\rfloor \text{ complete blocks, plus } r = D \bmod d \text{ leftover days}$$

Each complete block $k$ (counting from $0$) runs for $d$ days at rate $P + kQ$, and the leftover days run at the next rate $P + fQ$. So

$$\text{total} = d\sum_{k=0}^{f-1}(P + kQ) \;+\; r\,(P + fQ)
= d\left(fP + Q\frac{f(f-1)}{2}\right) + r\,(P + fQ)$$

using the arithmetic-series sum $0 + 1 + \cdots + (f-1) = \frac{f(f-1)}{2}$.

The closed form matters: with $D$ up to $10^6$ and $T$ up to $10^5$, looping day by day would be $10^{11}$ steps. The formula is $O(1)$.

The partial block is the easy thing to drop. Sample case 2 has $D = 3, d = 2$: one full block of two days at rate $1$, then a single leftover day at the **raised** rate $2$, totalling $4$. Ignoring the remainder would give $2$; charging it at the old rate would give $3$.

Sample case 3 is the same shape with a bigger step: two blocks at rates $1$ and $3$ over two days each ($2 + 6 = 8$), plus one day at rate $5$, giving $13$.

The result reaches roughly $10^{15}$, so this **needs 64-bit arithmetic** outside Python — a point the problem's subtask split quietly signals.

## Edge cases

- **$D$ not a multiple of $d$** (the second and third rows): the leftover days run at the *next* rate up, $p + \mathrm{full} \cdot q$, which the trailing term supplies — dropping it loses those days entirely.
- **$D$ an exact multiple of $d$** (the first row): the remainder is $0$ and the trailing term vanishes on its own.
- **$d > D$**: there are no complete blocks, so the series term is $0$ and the whole period runs at the base rate $p$, giving $D \cdot p$.
- **$q$ is added per *block*, not per day**, which is why the series is over $\mathrm{full}$ terms and each is multiplied by $d$.
- **The triangular factor must be integer-divided after multiplying**, `full * (full - 1) // 2`, to stay exact.
- **Magnitudes**: with $D \leq 10^6$, $d = 1$, $p, q \leq 10^6$ the total reaches about $5 \cdot 10^{17}$ — past 32-bit and close to the 64-bit ceiling, though native in Python.

## Dry run

Third sample: $D = 5$, $d = 2$, $p = 1$, $q = 2$. Two complete blocks, one day left over.

| days | rate | earned |
|---|---:|---:|
| 1–2 | $p = 1$ | 2 |
| 3–4 | $p + q = 3$ | 6 |
| 5 | $p + 2q = 5$ | 5 |

Total `13`. The formula gives $2(2 \cdot 1 + 2 \cdot 1) + 1 \cdot 5 = 8 + 5$.
