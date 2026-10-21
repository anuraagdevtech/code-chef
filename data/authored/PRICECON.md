---
topic: Arrays
subtopic: Summing a clamped excess
time: $O(N)$ per test case
space: $O(1)$
---
An item priced above the ceiling $K$ is sold at $K$ instead, losing $P_i - K$. An item already at or below $K$ is unaffected and loses nothing. So the total lost revenue is

$$\sum_{i=1}^{N} \max(0,\ P_i - K)$$

The clamp is what makes this one expression rather than a filter plus a sum. Items priced below the ceiling would otherwise contribute a **negative** loss, which would wrongly cancel out real losses from expensive items. Sample case 1 is built to catch exactly that: prices $[10, 2, 3, 4, 5]$ against $K = 4$ lose $6$ and $1$ for a total of $7$, whereas an unclamped sum would give $10 + 2 + 3 + 4 + 5 - 20 = 4$.

Sample case 2 has every price below the ceiling, so the answer is $0$ — a good check that the clamp never produces a negative total.

One pass with a running sum is enough; nothing needs sorting or storing. In Python the whole computation is a generator expression inside `sum`, which keeps it to $O(1)$ extra space even for $N = 10{,}000$.

Note that the ceiling only ever lowers a price — the government rule never raises a cheap item to $K$ — which is why the loss is one-sided and the clamp is at zero rather than symmetric.

## Edge cases

- **Every price below the cap** (the second row): the answer is $0$.
- **A price exactly at the cap**: contributes nothing, so the boundary is harmless either way.
- **The clamp is essential.** Without `max(0, ...)` the cheap items subtract: the first row would evaluate to $6 - 2 - 1 + 0 + 1 = 4$ instead of $7$. This is not an off-by-one but a wrong answer.
- **Every price above the cap** (the third row): all five items contribute, summing to $15$.
- **Largest inputs** ($N = 10^4$ with prices up to $1000$): the total stays under $10^7$.

## Dry run

First sample, cap $K = 4$:

| price | excess $\max(0, P-K)$ |
|---:|---:|
| 10 | 6 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 1 |

Total $7$, so the output is `7`. Note the $2$ and $3$ contribute zero rather than $-2$ and $-1$.
