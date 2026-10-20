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
