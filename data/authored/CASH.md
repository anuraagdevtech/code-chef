---
topic: Number Theory
subtopic: A conserved total modulo K
time: $O(N)$ per test case
space: $O(1)$
---
The elaborate rules about choosing $c$, taking from a prefix and depositing into a suffix are a smokescreen. Two facts settle the problem.

**Coins are conserved.** Moving coins between bags never creates or destroys any, so the grand total $\sum A_i$ is fixed. The leftover $R$ is whatever the bags do not absorb.

**The final configuration absorbs a multiple of $K$.** Every bag ends divisible by $K$, so the coins in bags sum to a multiple of $K$. Therefore

$$R = \sum A_i - (\text{multiple of } K)$$

and the smallest non-negative such $R$ is

$$R = \left(\sum A_i\right) \bmod K$$

That value is also achievable, so it is the answer — and it does not depend on $c$ at all.

It is worth seeing *why* $c$ drops out. Moving one bag from the suffix to the prefix changes the prefix's required withdrawal by $A_i \bmod K$ and the suffix's required deposit by $(K - A_i \bmod K) \bmod K$. Those two always sum to $0$ or $K$, so the difference between withdrawals and deposits shifts by a multiple of $K$ and its residue is **invariant**. Every choice of $c$ gives the same leftover.

Checking sample 1: $1 + 14 + 4 + 41 + 1 = 61$, and $61 \bmod 7 = 5$. Sample 2: $1 + 10 + 19 = 30$, and $30 \bmod 9 = 3$.

Spotting the conserved quantity turns an apparent optimisation over $N+1$ split points into a single modulo — which also makes the $10^5$ bound on $\sum N$ a non-issue.

## Edge cases

- **Where the splits are made is irrelevant.** Coins are conserved and every bag ends holding a multiple of $K$, so the leftover is $\left(\sum A_i\right) \bmod K$ whatever the arrangement — no search over distributions is needed.
- **$A_i$ may be $0$**, contributing nothing to the total.
- **A total of $0$** gives $0$ left over.
- **$K$ larger than the total**: no bag can be filled at all, and the modulo already returns the whole sum.
- **$K$ divides the total**: nothing is left over, and the answer is $0$.
- **Sums reach $10^5 \times 10^9 = 10^{14}$**, past 32-bit but native in Python.

## Dry run

| coins | total | $K$ | total $\bmod K$ |
|---|---:|---:|---:|
| $1, 14, 4, 41, 1$ | 61 | 7 | `5` |
| $1, 10, 19$ | 30 | 9 | `3` |

$61 = 8 \cdot 7 + 5$, so eight bags fill and five coins remain.
