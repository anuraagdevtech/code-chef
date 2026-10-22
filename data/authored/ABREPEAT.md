---
topic: Combinatorics
subtopic: Splitting pairs into within-copy and across-copy
time: $O(N)$ per test case
space: $O(1)$
---
The repeated string has length up to $10^9$, so the count must come from $S$ alone. Split the pairs by which copies they span.

**Within one copy.** Let $P$ be the number of `ab` subsequences inside $S$, computed in one pass by keeping a running count of `a`s seen and adding it at each `b`. Each of the $K$ copies contributes $P$.

**Across two copies.** For copies $u < v$, *every* `a` in copy $u$ precedes *every* `b` in copy $v$, so the pair contributes $a \cdot b$ where $a$ and $b$ are the letter counts in $S$. There are $\binom{K}{2}$ such ordered copy pairs. So

$$\text{answer} = K \cdot P \;+\; a \cdot b \cdot \frac{K(K-1)}{2}$$

The decomposition works precisely because position order between copies is total — no comparison inside $S$ is needed for the cross terms, which is what turns an apparently quadratic count into one linear pass.

The magnitudes are the real trap: with $NK \leq 10^9$ the answer reaches about $10^{17}$, so C++ needs `long long` (the statement says as much), while Python's integers are unbounded.

The samples check both terms. `abcb` with $K = 2$ has $P = 2$ and $a \cdot b = 1 \cdot 2 = 2$, giving $2 \cdot 2 + 2 \cdot 1 = 6$. `aayzbaa` with $K = 1$ has no cross term at all, leaving $P = 2$ — only the two leading `a`s precede the single `b`. And the third sample's $K \approx 8 \times 10^7$ makes the cross term dominate completely.

## Edge cases

- **The pairs split into two kinds**: both characters inside one copy, or the `a` in an earlier copy and the `b` in a later one.
- **Within-copy pairs are counted once per copy**, so the single-copy count multiplies by $K$.
- **Across-copy pairs multiply by $\binom{K}{2}$**, since *every* `a` of the earlier copy precedes *every* `b` of the later one — giving $(\text{total } a) \times (\text{total } b)$ per ordered pair of copies.
- **$K = 1$ leaves only the within-copy term**, as $\binom{1}{2} = 0$ (the second sample row).
- **The answer is huge**: at $NK \leq 10^9$ the count reaches about $6 \times 10^{16}$, past 32-bit and into the upper reaches of 64-bit.
- **Characters other than `a` and `b` are ignored**, but they still occupy positions — which is why the counting is by letter rather than by index.
- **A string with no `a` or no `b`** gives $0$ from both terms.

## Dry run

First sample: $S = $ `abcb` repeated $K = 2$ times, giving `abcbabcb`.

| quantity | value |
|---|---:|
| `a`s in one copy | 1 |
| `b`s in one copy | 2 |
| `ab` pairs inside one copy | 2 |
| within-copy total, $K \times 2$ | 4 |
| copy pairs, $K(K-1)/2$ | 1 |
| across-copy total, $1 \times 2 \times 1$ | 2 |

Total `6`.
