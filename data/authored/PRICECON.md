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
