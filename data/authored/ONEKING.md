---
topic: Greedy
subtopic: Stabbing intervals at earliest right endpoints
time: $O(N \log N)$ per test case
space: $O(N)$
---
A bomb at $x$ destroys every kingdom whose interval contains $x$, so this is the classic **interval point cover** (or stabbing) problem: pick the fewest points so that every interval holds at least one.

Sort the kingdoms by **right endpoint** and sweep. Whenever the current kingdom is not already hit by the last bomb placed, drop a new bomb at that kingdom's right endpoint:

$$\text{place at } b_i \iff a_i > x_{\text{last}}$$

Choosing the right endpoint is what makes the greedy optimal. Some bomb must hit this interval, and among all positions that do, $b_i$ is the furthest right — so it covers a superset of the later intervals that any other valid choice would. Formally, exchanging an optimal solution's bomb for $b_i$ keeps it feasible, and induction finishes the argument.

Sorting by right endpoint rather than left is essential; sorting by left endpoint and bombing greedily can be arbitrarily bad, since a wide interval early on would let the sweep place bombs that cover nothing useful later.

In the sample, $[1,3]$, $[2,5]$ and $[6,9]$ sort as given. A bomb at $3$ destroys the first two kingdoms — note it covers $[2,5]$ even though $5 > 3$, which is exactly the reach the greedy buys. The third kingdom starts beyond $3$, so a second bomb at $9$ finishes the job: $2$ bombs.

Note equal right endpoints need no tie-break, since any of them accepts the same bomb.

## Edge cases

- **Bombing the earliest right endpoint is optimal.** Sorting by right endpoint and placing a bomb there whenever the current kingdom is not already covered is the classic interval-stabbing greedy — the bomb reaches as far forward as possible without missing the kingdom that forced it.
- **Sorting by right endpoint, not left**, is what makes it work; sorting by left endpoint and bombing greedily can overcount.
- **Overlapping kingdoms share a bomb** (the sample's first two, which both contain the point $3$), so the answer is $2$ rather than $3$.
- **Touching intervals count as overlapping**, since the endpoints are inclusive — an interval starting exactly where the bomb sits is destroyed.
- **A degenerate kingdom $[a, a]$ is allowed** ($a_i \leq b_i$ with equality permitted) and simply forces a bomb at that point.
- **The sentinel starts below every coordinate**, since $a_i \geq 0$ means $-1$ is safely outside the range.
- **The tuple is stored as (right, left)** so the default sort orders by right endpoint with no key function.

## Dry run

Sample: kingdoms $[1,3]$, $[2,5]$, $[6,9]$, sorted by right endpoint.

| kingdom | left | already covered? | bomb placed at |
|---|---:|---|---:|
| $[1,3]$ | 1 | no | **3** |
| $[2,5]$ | 2 | yes ($2 \leq 3$) | — |
| $[6,9]$ | 6 | no | **9** |

Output `2`.
