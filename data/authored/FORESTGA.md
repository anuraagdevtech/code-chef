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
