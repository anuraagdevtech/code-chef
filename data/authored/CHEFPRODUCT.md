---
topic: Number Theory
subtopic: Size feasibility from a square bound and a parity
time: $O(\sqrt[2]{N})$-free, $O(1)$ per test case
space: $O(1)$
---
"Every non-empty subset has an odd product" is a strong condition in disguise: the singletons are subsets, so **every element must be odd**. In particular $0$ is excluded, so the set consists of distinct positive odd integers — and then every subset product is automatically odd.

Now ask which sizes $k$ are possible for a set of $k$ distinct positive odds summing to $N$. Two constraints:

- **Minimum sum.** The smallest such set is $1 + 3 + \cdots + (2k-1) = k^2$, so $k^2 \leq N$.
- **Parity.** A sum of $k$ odd numbers is congruent to $k$ mod $2$, so $k \equiv N \pmod 2$.

Both are also sufficient: starting from $\{1, 3, \ldots, 2k-1\}$, raising the largest element by $2$ at a time reaches every value of the right parity above $k^2$, keeping the elements distinct and odd. So the count of valid sizes is

$$\#\{\,k \geq 1 : k^2 \leq N,\ k \equiv N \!\!\pmod 2\,\}$$

which with $m = \lfloor \sqrt{N} \rfloor$ is $\lfloor m/2 \rfloor$ for even $N$ and $\lceil m/2 \rceil$ for odd $N$.

Use `isqrt` rather than a floating-point square root: at $N = 10^{18}$ a `double` cannot distinguish $m^2$ from $m^2 - 1$, and the bound $k^2 \leq N$ is exactly where that matters.

The samples show the parity filter doing the work. For $N = 4$ we have $m = 2$, and only $k = 2$ survives ($\{1,3\}$); $k = 1$ fails because a single odd number cannot be even. For $N = 18$, $m = 4$ gives $k \in \{2, 4\}$ — for instance $\{1,17\}$ and $\{1,3,5,9\}$ — so the answer is $2$.
