---
topic: Graphs
subtopic: Connected components by DSU, then a product of sizes
time: $O((N + M)\,\alpha(N))$ per test case
space: $O(N)$
---
Friends must share a route, and friendship is *not* transitive — but "must share" is, so the constraint propagates along chains. Two employees therefore end up on the same route exactly when they are in the same **connected component** of the friendship graph. Maximising routes means giving each component its own:

$$\text{routes} = \#\text{components}$$

That is the most possible, since merging two components would only reduce the count, and it is legal, since no constraint spans components.

Each route then needs one captain chosen from its own members, and the choices are independent, so

$$\text{ways} = \prod_{\text{components } c} |c| \pmod{10^9 + 7}$$

The product can be astronomically large — $2^{50000}$ for a graph of $10^5$ people paired off — which is why the modulus is there. Note the count of *routes* is not reduced modulo anything; only the second number is.

A disjoint-set-union structure with union by size and path compression computes both numbers in one pass, and the component sizes come for free from the DSU's own size array. A BFS or DFS over adjacency lists would also work; DSU avoids building the lists.

Isolated employees are components of size $1$ and contribute a factor of $1$ — they add a route without adding choices. The samples show that directly: $4$ people with the chain $1$–$2$–$3$ give $2$ routes and $3 \cdot 1 = 3$ ways, while the triangle on $\{1,2,3\}$ plus two isolated people gives $3$ routes and again $3$ ways. The third sample's three disjoint pairs give $3$ routes and $2^3 = 8$ ways.

## Edge cases

- **Friends must share a route, so each connected component becomes one route** — and maximising the route count means using exactly one per component, since merging two would waste a route.
- **Friendship is not transitive but connectivity is**, which is the whole point: the components, not the individual friendships, decide the grouping.
- **An isolated employee is their own route** (the first sample's employee $4$), so singletons count.
- **$M$ may be $0$**, leaving $N$ routes and exactly one captain choice per route, for $1$ way in total.
- **The captain count is a product over components**, since each route picks its own captain independently — $3 \cdot 1 = 3$ in the first sample, $2^3 = 8$ in the third.
- **Extra edges inside a component change nothing** (the second sample's triangle has three edges and still forms one component of size $3$).
- **The product needs the modulus**: $5 \times 10^4$ components of size $2$ give $2^{50000}$, far past any fixed integer width.
- **Union by size with path halving** keeps the DSU near-linear at $N, M \leq 10^5$.

## Dry run

Third sample: $N = 6$ with edges $(1,2)$, $(3,4)$, $(5,6)$.

| component | members | size |
|---:|---|---:|
| 1 | $\{1, 2\}$ | 2 |
| 2 | $\{3, 4\}$ | 2 |
| 3 | $\{5, 6\}$ | 2 |

Three routes, and $2 \times 2 \times 2 = 8$ ways to pick the captains. Output `3 8`.
