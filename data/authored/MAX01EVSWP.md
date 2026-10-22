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

## Edge cases

- **Same-parity swaps mean the two parity classes are separate multisets**, so only four counts matter: zeros and ones at odd positions, and the same at even positions.
- **Each `01` occurrence needs a zero immediately before a one**, so it uses one position of each parity — giving two edge types, odd-zero beside even-one and even-zero beside odd-one.
- **The answer is capped at $\lfloor N/2 \rfloor$**, the number of disjoint adjacent pairs available in a string of length $N$.
- **An even $N$ has a unique perfect matching on the path, and it is all one type** — so when the type-A supply falls short of $\lfloor N/2 \rfloor$, the maximum drops to $\lfloor N/2 \rfloor - 1$ rather than simply $A + B$. That asymmetry is the whole subtlety, and it was verified exhaustively up to $N = 14$ with no mismatch.
- **An odd $N$ has slack**, so the plain $\min(A + B,\, \lfloor N/2 \rfloor)$ applies — all three samples are odd-length.
- **An all-zero or all-one string** gives $0$, since one of the two counts in every product is zero.
- **Sum of $|S| \leq 10^5$**, so the four counts come from one strided pass.

## Dry run

Third sample: $S = $ `10001` with $N = 5$.

| class | zeros | ones |
|---|---:|---:|
| odd positions ($1,3,5$) | 1 | 2 |
| even positions ($2,4$) | 2 | 0 |

| edge type | supply |
|---|---:|
| A: odd zero beside even one | $\min(1, 0) = 0$ |
| B: even zero beside odd one | $\min(2, 2) = 2$ |

$N$ is odd, so the answer is $\min(0 + 2,\, \lfloor 5/2 \rfloor) = $ `2` — for instance `00101`, which contains `01` twice.
