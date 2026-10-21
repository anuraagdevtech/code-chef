---
topic: Bit Manipulation
subtopic: Independent bits give a closed form
time: $O(1)$ per test case
space: $O(1)$
---
XOR and addition of the two terms both act bit by bit here, with no carries to couple the positions — $(A \oplus X)$ and $(A \oplus Y)$ contribute $0$, $2^b$ or $2 \cdot 2^b$ at bit $b$ depending only on bit $b$ of $A$, $X$ and $Y$. So each bit of $A$ can be chosen independently, and the minimum is the sum of the per-bit minima.

Fix a bit $b$ and let $x, y$ be the corresponding bits of $X, Y$:

- **$x = y$:** pick $a = x$. Both XORs give $0$ at this bit, contributing nothing.
- **$x \neq y$:** whichever $a$ is chosen, it agrees with one of them and differs from the other, so exactly one term contributes $2^b$ — unavoidable.

So the differing bits each cost exactly $2^b$ and the matching bits cost nothing, which is the definition of XOR:

$$\min_A \bigl[(A \oplus X) + (A \oplus Y)\bigr] = X \oplus Y$$

Notice the bound is attained by *any* $A$ that agrees with $X$ and $Y$ on their common bits — $A = X$ and $A = Y$ both work — so the minimiser is not unique even though the minimum is.

The sample has $X = 6 = 0110_2$ and $Y = 12 = 1100_2$, which differ in bits $1$ and $3$, giving $2 + 8 = 10$. Taking $A = 6$ confirms it: $0 + (6 \oplus 12) = 10$.

## Edge cases

- **The bits are independent**, so the minimum is reached bit by bit and no search over $A$ is needed: each bit of $A$ affects only its own column of both terms.
- **Where $X$ and $Y$ agree**, $A$ can match them and that bit contributes $0$ to both terms.
- **Where they differ**, exactly one of the two terms must pay $2^b$ whatever $A$ does — so the cost is forced, and summing those bits is precisely $X \oplus Y$.
- **$X = Y$** → the answer is $0$, achieved at $A = X$.
- **$A$ is unconstrained**, so there is never a case where the optimal $A$ is out of reach; the bound on $X, Y$ never enters.
- **$X, Y$ up to $10^9$** fit in 30 bits, and the XOR cannot exceed the larger of them in bit width.

## Dry run

Sample: $X = 6$, $Y = 12$.

| bit | $2^b$ | $X$ | $Y$ | agree? | best $A$ bit | cost |
|---:|---:|---:|---:|:---:|---:|---:|
| 3 | 8 | 0 | 1 | no | either | 8 |
| 2 | 4 | 1 | 1 | yes | 1 | 0 |
| 1 | 2 | 1 | 0 | no | either | 2 |
| 0 | 1 | 0 | 0 | yes | 0 | 0 |

Total $8 + 2 = $ `10`, which is $6 \oplus 12$.
