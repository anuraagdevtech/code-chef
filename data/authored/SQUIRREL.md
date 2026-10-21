---
topic: Binary Search
subtopic: Searching time, with a greedy capacity check
time: $O(m \log m \log(\text{time}))$ per test case
space: $O(m)$
---
Tree $i$ has dropped its first chestnut at second $T_i$ and one more every $P_i$ seconds after, so by second $S$ it has produced

$$c_i(S) = \begin{cases} 0 & S < T_i \\ \left\lfloor \dfrac{S - T_i}{P_i} \right\rfloor + 1 & \text{otherwise} \end{cases}$$

The $n$ squirrels station themselves under $n$ different trees, so the harvest at time $S$ is the sum of the **$n$ largest** $c_i(S)$.

Every $c_i$ is non-decreasing in $S$, so the harvest is too — which makes "enough by time $S$" a monotone predicate and **binary search on $S$** the natural tool.

Each probe computes the $m$ counts and sums the top $n$; `heapq.nlargest` does that without a full sort when $n \ll m$.

The search bound deserves a thought. With $k$ up to $10^7$, a single tree, and $P_i$ up to $100$, the answer can reach about $10^9$ — so the upper limit is set there rather than at something comfortable, and roughly $30$ probes cover it.

The two samples differ only in one period, which is enough to move the answer. In the first, the trees have periods $1, 2, 1$ and by second $4$ the best two have produced $3 + 2 = 5$. In the second, speeding the middle tree to period $1$ lets the best two reach $3 + 2 = 5$ a second earlier.

Note the floor-plus-one: a tree that has just dropped its first chestnut at exactly $S = T_i$ counts as one, not zero.

## Edge cases

- **The answer is monotone in time**, so binary search applies: once enough chestnuts have fallen by second $s$, the same holds for every later second.
- **Tree $i$ has dropped $\lfloor (s - T_i)/P_i \rfloor + 1$ chestnuts by second $s$**, once $s \geq T_i$ — the $+1$ is the first chestnut at $T_i$ itself, and forgetting it undercounts every tree.
- **Trees not yet dropping must be excluded**, which the `if s >= ti` filter does; $(s - T_i)$ would otherwise go negative and the floor division would produce a nonsense count.
- **The squirrels occupy $n$ distinct trees**, so only the $n$ most productive count — summing all $m$ would overcount whenever $m > n$.
- **$n$ may exceed $m$**, in which case every tree is used and `nlargest` simply returns all of them.
- **The two samples differ only in one period** ($P_3 = 2$ against $1$), which shifts the answer from $4$ to $3$ — so the per-tree arithmetic has to be exact.
- **The upper bound must be generous**: with $k$ up to $10^7$ and a single slow tree, the answer can reach $10^9$, so the search starts there.

## Dry run

First sample: $n = 2$ squirrels, $k = 5$ chestnuts, trees $(T, P) = (5,1), (1,2), (2,1)$.

| $s$ | tree 1 | tree 2 | tree 3 | best two | total |
|---:|---:|---:|---:|---|---:|
| 3 | — (not started) | $\lfloor 2/2 \rfloor + 1 = 2$ | $\lfloor 1/1 \rfloor + 1 = 2$ | $2, 2$ | 4 |
| 4 | — | $\lfloor 3/2 \rfloor + 1 = 2$ | $\lfloor 2/1 \rfloor + 1 = 3$ | $3, 2$ | **5** |

Output `4`.
