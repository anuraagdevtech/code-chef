---
topic: Greedy
subtopic: The larger of two independent lower bounds
time: $O(N)$ per test case
space: $O(1)$
---
Two constraints act independently, and the answer is simply the larger.

**Each admin needs $N$ hours.** Every admin must visit all $N$ shops, one hour apiece, and cannot be in two shops at once. So no schedule finishes before hour $N$.

**Each shop needs $\lceil X / A_i \rceil$ hours.** Shop $i$ must serve all $X$ admins and holds at most $A_i$ at a time, so it needs that many hours of throughput. The binding shop is the tightest one.

Hence

$$\text{answer} = \max\left(N,\ \max_i \left\lceil \frac{X}{A_i} \right\rceil\right)$$

Both bounds are simultaneously achievable, which is the part worth believing. Admins can be staggered — think of a round-robin where admin $j$ starts at shop $(j \bmod N)$ and rotates — so each shop sees a steady, evenly spread stream and nobody collides. The freedom to idle, which the statement grants explicitly, is what lets a schedule absorb whichever bound is slack.

Sample case 2 is bound by the admin count: four shops means at least four hours, even though the tightest shop ($A = 1$ with $X = 2$) needs only two. Sample case 3 is the reverse: a single shop of capacity $2$ serving six admins takes three hours, far more than the $N = 1$ lower bound.

Sample case 1 has both bounds met at $2$ and $1$, giving $2$.

The ceiling is computed as `(x + a - 1) // a` to stay in integers at $X, A_i$ up to $10^9$.

## Edge cases

- **Two independent lower bounds, and the answer is the larger.** Every admin must spend $N$ hours (one per shop), and every shop must absorb $X$ visits at $A_i$ at a time, needing $\lceil X / A_i \rceil$ hours. Both are achievable simultaneously, so the maximum of the two is exact.
- **Either bound can dominate.** The second row is limited by the shop count ($N = 4$ against a worst shop needing $2$), while the third is limited by a single tight shop ($N = 1$ against $\lceil 6/2 \rceil = 3$).
- **Only the tightest shop matters**, so the per-shop bound collapses to a maximum over $\lceil X / A_i \rceil$.
- **The ceiling must be integer**: `(x + a - 1) // a` rather than a float division, since $X$ and $A_i$ reach $10^9$ and a float divide can round the wrong way near an exact multiple.
- **$A_i \geq X$ makes a shop free** — its bound is $1$ — which the first row shows with capacity $3$ for $3$ admins.
- **Admins may visit shops in any order**, which is what makes the two bounds simultaneously satisfiable; a fixed order would be a scheduling problem instead.

## Dry run

| $N$ | $X$ | capacities | per-shop $\lceil X/A_i \rceil$ | worst | $\max(N, \text{worst})$ |
|---:|---:|---|---|---:|---:|
| 2 | 3 | $3, 3$ | $1, 1$ | 1 | `2` |
| 4 | 2 | $1,2,3,4$ | $2,1,1,1$ | 2 | `4` |
| 1 | 6 | $2$ | $3$ | 3 | `3` |

Row 3: one shop holding two at a time must serve six admins, so three hours even though each admin needs only one.
