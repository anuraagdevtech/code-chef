---
topic: Bit Manipulation
subtopic: OR of a prefix of the integers
time: $O(1)$ per test case
space: $O(1)$
---
A MEX of $m$ requires $0, 1, \ldots, m-1$ all to appear, and extra elements can only raise the OR, so the cheapest array achieving MEX $\geq m$ is exactly $\{0, 1, \ldots, m-1\}$. Its OR has a closed form: every bit below the top bit of $m-1$ gets set by some value in the range, so

$$0 \mathbin{|} 1 \mathbin{|} \cdots \mathbin{|} (m-1) = 2^{\,\mathrm{bitlen}(m-1)} - 1$$

a block of ones. So the constraint $\text{OR} \leq X$ becomes $2^t - 1 \leq X$ with $t = \mathrm{bitlen}(m-1)$, and since that bound depends on $m$ only through $t$, the best $m$ is the largest with the same $t$:

$$\text{answer} = 2^t, \qquad t = \max\{\,t : 2^t - 1 \leq X\,\} = \mathrm{bitlen}(X+1) - 1$$

The answer is therefore always a power of two — the MEX jumps from $2^t$ straight to $2^{t+1}$ as $X$ grows, with nothing in between. That is what makes $X = 2$ and $X = 1$ give the same answer: both allow the OR $1$ but not $3$.

The samples trace the jumps. $X = 0$ forces the array $[0]$ alone, so the MEX is $1$. $X = 1$ allows $\{0,1\}$ with OR $1$, so $2$; $X = 2$ cannot afford $\{0,1,2\}$, whose OR is $3$, so it stays at $2$. And $X = 5$ affords $\{0,1,2,3\}$ with OR $3$ but not $\{0,\ldots,4\}$ with OR $7$, giving $4$.

Note the elements need not be distinct or bounded individually — only their OR is constrained — which is why no other construction can do better.

## Edge cases

- **Achieving MEX $= m$ forces the array to contain $0, 1, \dots, m-1$**, whose OR is unavoidable — so the question is the largest $m$ with $\mathrm{OR}(0 \dots m-1) \leq X$.
- **That OR has a closed form**: $\mathrm{OR}(0 \dots m-1) = 2^{\mathrm{bitlen}(m-1)} - 1$, all ones up to the top bit of $m-1$. So it jumps only at powers of two, which makes the answer always a power of two.
- **Extra elements never help.** Adding anything beyond $0 \dots m-1$ can only raise the OR, so the optimal array is exactly that prefix.
- **$X = 0$** forces the array to be all zeros, giving MEX $1$ — the smallest possible answer, and the reason the formula uses $X+1$.
- **$X$ just below a power of two minus one** is the tight case: $X = 2$ still only allows $\{0, 1\}$, because adding $2$ pushes the OR to $3$.
- **The expression $2^{\mathrm{bitlen}(X+1) - 1}$** is the largest power of two at most $X+1$, which is exactly that largest $m$.
- **$X$ up to $10^9$** with constant work per case.

## Dry run

| $X$ | largest prefix $0 \dots m-1$ with OR $\leq X$ | its OR | answer |
|---:|---|---:|---:|
| 0 | $\{0\}$ | 0 | `1` |
| 1 | $\{0,1\}$ | 1 | `2` |
| 2 | $\{0,1\}$ | 1 | `2` |
| 5 | $\{0,1,2,3\}$ | 3 | `4` |

For $X = 5$, extending to $\{0,\dots,4\}$ would give an OR of $7 > 5$.
