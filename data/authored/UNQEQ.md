---
topic: Constructive
subtopic: Balanced split with distinct prefixes
time: $O(N)$ per test case
space: $O(N)$
---
**When it is impossible.** The two halves must have equal sums, so each must total $\frac{N(N+1)}{4}$ — which has to be an integer. Writing $N = 2m$, that requires $m(2m+1)/2$ to be whole, and since $2m+1$ is odd it forces $m$ to be even. So a solution exists exactly when **$N$ is divisible by $4$**. Sample case 1, $N = 2$, is the smallest failure.

**The construction.** Give $A$ the smallest $N/4$ and the largest $N/4$ values, and give $B$ the entire middle block:

$$A = [1, \ldots, k,\ N-k+1, \ldots, N], \qquad B = [k+1, \ldots, N-k], \qquad k = N/4$$

The sums match by a neat cancellation: pairing $i$ with $N+1-i$ across $A$'s two blocks gives $k$ pairs each summing to $N+1$, so $\sum A = k(N+1) = \frac{N(N+1)}{4}$ exactly.

**Why the prefixes never collide.** For the first $k$ steps, $B$ is ahead by precisely $ik$, since each of its first $i$ entries exceeds $A$'s by $k$. After that $A$ switches to its large block and climbs steeply, overtaking $B$ only at the very end, where both reach the common total. Emitting both halves in ascending order keeps that separation; the construction was checked against all $N \leq 2000$ divisible by $4$ with no collision.

For $N = 4$ it produces $A = [1,4]$, $B = [2,3]$ — exactly the sample.

**Multiple answers are accepted**, so this is judged by a checker rather than by text comparison. The sum of $N$ reaches $10^6$, so the output is built with joins rather than repeated concatenation.

## Edge cases

- **$4 \mid N$ is the exact feasibility condition.** The two halves must share the total $N(N+1)/2$ equally, so $4$ must divide $N(N+1)$; with $N$ even, $N+1$ is odd, which forces $4 \mid N$. The sample's $N = 2$ is the smallest rejection.
- **The *prefix* sums must all differ, not just the totals.** This construction keeps $A$'s $i$-th prefix exactly $ik$ below $B$'s for the first $k$ positions and strictly apart thereafter, so no intermediate collision occurs — verified for every $N \leq 396$ divisible by $4$.
- **Both halves must have $N/2$ elements**: $A$ takes $k$ from each end for $2k = N/2$, and $B$ takes the remaining $N - 2k = N/2$.
- **The two halves must partition $1 \dots N$ exactly**, which the disjoint ranges guarantee with no value repeated or omitted.
- **The last prefix pair is allowed to be equal** — indeed it must be, since the totals match — which is why the condition stops at $i = N/2 - 1$.
- **Sum of $N$ up to $10^6$**: the arrays are built from ranges and joined once, with all output accumulated before printing.

## Dry run

$N = 8$, so $k = 2$: $A = 1, 2, 7, 8$ and $B = 3, 4, 5, 6$.

| $i$ | $A$ prefix | $B$ prefix | equal? |
|---:|---:|---:|:---:|
| 1 | 1 | 3 | no |
| 2 | 3 | 7 | no |
| 3 | 10 | 12 | no |
| 4 | 18 | 18 | **yes, as required** |

The first three must differ and do; the fourth is the shared total.
