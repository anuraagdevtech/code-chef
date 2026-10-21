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
