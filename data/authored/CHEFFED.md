---
topic: Brute Force
subtopic: Bounding the search window
time: $O(1)$ — a fixed-width scan
space: $O(1)$
---
Solve $X + S(X) + S(S(X)) = N$ by searching, but only over a **narrow window** below $N$.

The bound comes from how small digit sums are. For $X \leq 10^9$ the digit sum $S(X)$ is at most $9 \times 10 = 90$, and $S(S(X))$ is at most $S(99) = 18$. So the two correction terms together never exceed about $108$, which forces

$$N - 108 \leq X \leq N$$

Scanning a couple of hundred candidates below $N$ and testing each directly is therefore enough — and it is $O(1)$ regardless of how large $N$ is. The window is taken a little wider than the bound for safety, which costs nothing.

Without that bound the search space is $10^9$ and hopeless; recognising that $S$ grows **logarithmically** while $X$ grows linearly is the whole idea, and the same reasoning appears in every "number plus its digit sum" problem.

Candidates must be clamped to stay positive, since $X$ is required to be a positive integer and $N$ may be small — as in the sample, where $N = 6$ and the window would otherwise run below $1$.

Checking that sample: $X = 2$ gives $2 + 2 + 2 = 6$, so the count is $1$. Note $X = 6$ itself gives $6 + 6 + 6 = 18$, far past the target — the solution is well below $N$, which is exactly what the window is for.

Note there is **no $T$**: the input is a single integer $N$.
