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

## Edge cases

- **The search window is provable, not a guess.** For $X \leq 10^9$ the digit sum is at most $81$ and the digit sum of that at most $16$, so any solution satisfies $X \geq N - 97$. Scanning $200$ values back therefore cannot miss one.
- **$X$ must be positive**, which `max(1, n - 200)` enforces for small $N$.
- **$X = N$ is never a solution** for $N \geq 1$, since the two digit-sum terms are both positive — but including it costs nothing and keeps the range simple.
- **The answer can exceed $1$.** $N = 9939$ has four solutions ($9898$, $9907$, $9910$, $9913$), so the loop must count rather than stop at the first hit.
- **The answer can be $0$** for many $N$, as the map $X \mapsto X + S(X) + S(S(X))$ is not onto.
- **There is no test-case count** — the input is a single integer.

## Dry run

$N = 6$: scan $X$ from $1$ upward.

| $X$ | $S(X)$ | $S(S(X))$ | total |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 3 |
| 2 | 2 | 2 | **6** |
| 3 | 3 | 3 | 9 |
| 4 | 4 | 4 | 12 |
| 5 | 5 | 5 | 15 |

Exactly one solution, so the output is `1`.
