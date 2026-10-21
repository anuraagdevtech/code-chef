---
topic: Combinatorics
subtopic: A condition that reduces to its singletons
time: $O(n)$ per test case
space: $O(1)$
---
A subsequence is *good* when **every** non-empty subsequence of it has sum divisible by $m$. The condition looks expensive — exponentially many sub-subsequences — but it collapses.

The singletons are themselves non-empty subsequences, so every chosen element must individually be divisible by $m$. Conversely, if all chosen elements are multiples of $m$, then any sum of them is a multiple of $m$ too, so every sub-subsequence qualifies automatically.

So a subsequence is good **exactly when all of its elements are divisible by $m$**, and the count is the number of non-empty subsets of those elements:

$$2^{c} - 1, \qquad c = \#\{i : m \mid a_i\}$$

The $-1$ excludes the empty subsequence, which the problem rules out.

Spotting that the strongest constraints are the smallest ones — the singletons — is the move here. Without it, one might reach for a subset-sum DP over residues, which at $n = 30$ would be $2^{30}$ by brute force or $O(n \cdot m)$ by DP, both unnecessary.

Sample case 1 has $a = [1, 2]$ with $m = 3$: neither element is a multiple of $3$, so $c = 0$ and the answer is $2^0 - 1 = 0$. Sample case 2 has $a = [1, 3]$: only the $3$ qualifies, giving $2^1 - 1 = 1$ — the subsequence $[3]$ alone.

With $n \leq 30$ the count fits comfortably in $2^{30}$, so no modular arithmetic is needed.

## Edge cases

- **The singletons carry the whole condition.** Every non-empty subsequence must have a sum divisible by $m$, and the one-element subsequences force each chosen $a_i \equiv 0 \pmod m$ — after which every larger sum is a sum of multiples and is automatically divisible. So the condition collapses to a per-element test.
- **No divisible element** (the first row, $m = 3$ with values $1, 2$) → $0$ good subsequences, since even a single element fails.
- **The subsequence must be non-empty**, hence the $-1$: with $c$ divisible elements there are $2^c$ subsets but the empty one does not count.
- **Duplicates count as distinct positions**, so two copies of a divisible value give $3$ good subsequences, not $1$.
- **$m = 1$** would make every element divisible and the answer $2^n - 1$.
- **$n \leq 30$** keeps $2^c$ inside 32 bits, and the shift is exact in Python regardless.

## Dry run

| $n$ | $m$ | values | divisible by $m$ | $c$ | $2^c - 1$ |
|---:|---:|---|---|---:|---:|
| 2 | 3 | $1, 2$ | none | 0 | `0` |
| 2 | 3 | $1, 3$ | $3$ | 1 | `1` |

The only good subsequence in the second row is $[3]$ itself.
