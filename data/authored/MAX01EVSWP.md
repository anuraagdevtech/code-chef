---
topic: Constructive
subtopic: Matching on a path, with a parity-forced shortfall
time: $O(N)$ per test case
space: $O(1)$
---
Same-parity swaps let the odd positions be permuted freely among themselves, and likewise the even ones. So the only data that matters is four counts: $o_A, z_A$ ones and zeros on odd positions, and $o_B, z_B$ on even positions.

Occurrences of `01` are automatically **disjoint** — two of them cannot share a character, since the shared position would have to be both `1` and `0`. So they form a matching on the path of adjacent position pairs, where each edge joins one odd and one even position. An edge of **type A** (odd, even) needs a zero on the odd side and a one on the even side; **type B** (even, odd) needs the reverse. With $x$ type-A and $y$ type-B edges,

$$x \leq X := \min(z_A, o_B), \qquad y \leq Y := \min(z_B, o_A), \qquad x + y \leq \lfloor N/2 \rfloor$$

The last bound is the maximum matching of the path. For **odd** $N$ the path has an odd number of vertices and every split of the maximum size is realisable, so the answer is $\min(X + Y, \lfloor N/2 \rfloor)$.

For **even** $N$ the path has $N$ vertices and its perfect matching is **unique** — all type A. So the maximum $\lfloor N/2 \rfloor$ is reachable only when $X \geq N/2$, which forces every odd position to hold `0` and every even one `1`, i.e. the string $0101\ldots01$. Otherwise one occurrence is lost:

$$\text{answer} = \begin{cases} \lfloor N/2 \rfloor & N \text{ odd, or } X \geq N/2 \\ \min(X+Y,\ N/2 - 1) & \text{otherwise}\end{cases}$$

capped by $X+Y$ throughout. That shortfall is the whole subtlety, and a brute force over all strings up to length $14$ confirms the formula exactly.

The samples are all $N = 5$, hence odd: `00100` has $X = 0, Y = 1$ for $1$; `01010` has $X = 2$ for $2$; and `10001` has $Y = 2$ for $2$.
