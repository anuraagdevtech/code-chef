---
topic: Prefix Sums
subtopic: Best split between an open prefix and a close suffix
time: $O(N)$ per test case
space: $O(1)$
---
Unfolding the definition, a dense sequence is $\underbrace{(\cdots(}_{k}\underbrace{)\cdots)}_{k}$ — $k$ opening brackets followed by $k$ closing brackets, for some $k \geq 0$. Nothing else qualifies: the recursion only ever wraps, never concatenates, so `()()` is *not* dense even though it is balanced.

Removing brackets leaves a subsequence, so the task is to find the **longest dense subsequence** and remove the rest. A dense subsequence of size $2k$ takes $k$ openings from some prefix and $k$ closings from the complementary suffix, so with $\mathrm{open}(i)$ counting `(` in $S_1 \ldots S_i$ and $\mathrm{close}(i)$ counting `)` in $S_{i+1} \ldots S_N$,

$$k^* = \max_{0 \leq i \leq N} \min\bigl(\mathrm{open}(i),\ \mathrm{close}(i)\bigr), \qquad \text{answer} = N - 2k^*$$

Both counts are prefix sums, so one left-to-right sweep that increments the running open count and decrements the remaining close count evaluates every split in $O(1)$. The answer is well defined because $k = 0$ is always available — the empty sequence is dense, so the worst case is removing everything.

The samples separate "balanced" from "dense". `((()))` is already dense, so $0$. `()()()()()` is perfectly balanced yet costs $4$: the best split takes three `(` from the left and three `)` from the right, keeping $6$ of $10$. `()(())()` keeps the same $6$, costing $2$. And `((()))()` also costs $2$ — the trailing `()` must go, since appending it breaks the nesting even though the prefix was already dense.

## Edge cases

- **Dense means a single nest**, $(((\ldots)))$ — $k$ opens then $k$ closes — so the task is to keep the largest such nest and remove everything else.
- **The split point matters, not the balance.** For each position, the usable nest is $\min(\text{opens to the left}, \text{closes to the right})$, and the answer is $N - 2\max$. A validity or balance check would answer a different question entirely.
- **Already dense** (the second row, `((()))`) → $0$ removals, found at the midpoint split.
- **A fully alternating string** (`()()()()()`) keeps only a nest of depth $3$ out of $10$ characters, so $4$ must go — the worst case relative to length.
- **The closes counter is pre-loaded with the total and decremented as the scan passes each `)`**, so at every step it holds exactly the closes still ahead; recomputing it per position would be quadratic.
- **An empty result is dense**, so the answer is well defined even for a string with no usable nest, where $\max$ stays $0$ and everything is removed.
- **Sum of $N \leq 3 \cdot 10^5$**: one pass over the bytes, comparing against the literal `0x28`.

## Dry run

First sample: `()(())()`, $N = 8$, with $4$ opens and $4$ closes.

| position | char | opens so far | closes ahead | $\min$ |
|---:|---|---:|---:|---:|
| 1 | `(` | 1 | 4 | 1 |
| 2 | `)` | 1 | 3 | 1 |
| 3 | `(` | 2 | 3 | 2 |
| 4 | `(` | 3 | 3 | **3** |
| 5 | `)` | 3 | 2 | 2 |
| 6 | `)` | 3 | 1 | 1 |
| 7 | `(` | 4 | 1 | 1 |
| 8 | `)` | 4 | 0 | 0 |

Best nest is $3$ deep, so $8 - 2 \cdot 3 = $ `2` brackets are removed.
