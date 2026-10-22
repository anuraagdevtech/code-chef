---
topic: Binary Search
subtopic: Searching time on a monotonic yield
time: $O(N \log(\text{months}))$
space: $O(N)$
---
After $m$ months tree $i$ stands at $H_i + R_i m$, and it may be cut only once that reaches the legal minimum $L$. So the harvest available at month $m$ is

$$f(m) = \sum_{i \,:\, H_i + R_i m \,\geq\, L} \bigl(H_i + R_i m\bigr)$$

$f$ is **non-decreasing** in $m$ for two reinforcing reasons: every already-legal tree keeps growing, and trees only ever *enter* the legal set, never leave it. That monotonicity is what licenses binary search on the answer — find the smallest $m$ with $f(m) \geq W$.

The search bound needs care. With $W$ up to $10^{18}$ and a single tree growing at $R = 1$, the answer can itself approach $10^{18}$, so the upper limit must be set around $2 \times 10^{18}$ rather than something comfortable like $10^9$. Each probe is one $O(N)$ pass, and roughly $61$ probes cover that range.

Note the legality test uses the **tree's own height**, not the total — a short fast-growing tree contributes nothing until it individually clears $L$.

The sample makes that concrete: with $L = 51$ and $W = 74$, at month $6$ the trees stand at $14$, $47$ and $56$, so only the last is legal and yields $56$ — short of the order. One month later they reach $16$, $54$ and $65$; two are now legal and together give $119$. So the answer is $7$, and the jump from $56$ to $119$ comes from a tree *becoming* harvestable rather than merely growing.

There is **no $T$**: the file holds a single test case.

## Edge cases

- **The yield only ever grows**, since every tree gets taller each month and a tree once legal stays legal — so the first sufficient month can be binary searched.
- **Legality is per tree, not per total.** A tree below the minimum height $L$ contributes nothing at all, which is why the probe tests each tree separately rather than summing everything.
- **The early exit matters.** Once the running total reaches $W$ the probe returns, which keeps each of the $\sim 60$ binary-search steps cheap even at $N = 10^5$.
- **Month $0$ must be a candidate**, since the forest may already suffice — the search's lower bound is $0$, not $1$.
- **The upper bound must be generous**: with $W$ up to $10^{18}$ and a growth rate of $1$, the answer can approach $10^{18}$, so the search starts at twice that.
- **Heights reach $10^9 + 10^9 \cdot 10^{18}$** inside the probe, so exact integers are essential.
- **There is no test-case count**: the input is $N$, $W$, $L$ followed by the tree data.

## Dry run

Sample: $W = 74$, $L = 51$, trees $(H, R) = (2,2), (5,7), (2,9)$.

| months | heights | legal (≥ 51) | harvest |
|---:|---|---|---:|
| 6 | $14, 47, 56$ | just the third | 56 |
| 7 | $16, 54, 65$ | the second and third | 119 |

Month $6$ falls short of $74$ and month $7$ clears it, so the answer is `7`.
