---
topic: Strings
subtopic: Binary alphabet reduces the LCS to two letter counts
time: $O(nm)$ per test case
space: $O(1)$
---
All strings, the hidden omen included, have the same length $m$ and use only `a` and `b`. The omen is chosen adversarially to make the common LCS as small as possible.

**Upper bound.** An all-`a` omen has only runs of `a` as subsequences, so the LCS of everything is $\min_i \mathrm{cnt}_a(s_i)$. An all-`b` omen likewise gives $\min_i \mathrm{cnt}_b(s_i)$. So the adversary achieves

$$\min\Bigl(\min_i \mathrm{cnt}_a(s_i),\ \min_i \mathrm{cnt}_b(s_i)\Bigr)$$

**Lower bound.** Write $\alpha = \min_i \mathrm{cnt}_a$, $\beta = \min_i \mathrm{cnt}_b$ and suppose the omen has $x$ letters `a` and $m - x$ letters `b`. The run $\texttt{a}^{\min(\alpha, x)}$ is a common subsequence of everything, and so is $\texttt{b}^{\min(\beta, m-x)}$, so the LCS is at least $\max$ of those two. Could the adversary keep both small — $x < \alpha$ and $m - x < \beta$? That would need $m < \alpha + \beta$. But each string has length $m$, so $\mathrm{cnt}_b(s_i) = m - \mathrm{cnt}_a(s_i)$ and hence $\beta = m - \max_i \mathrm{cnt}_a$, giving $\alpha + \beta \leq m$. So no: at least one of the two runs is at full length, and the LCS is at least $\min(\alpha, \beta)$.

The bounds meet, so the answer is exactly $\min(\alpha, \beta)$ — the whole problem is two letter counts per string, with no LCS dynamic programming at all.

The samples: `ab` and `ba` both have one of each letter, giving $1$. `aa` and `bb` give $\alpha = 0$ and $\beta = 0$, so an omen of either kind kills the LCS — $0$. And the three length-$4$ strings each have two of each letter, giving $2$.

## Edge cases

- **The omen is chosen to *minimise* the bad luck**, so the answer is the smallest achievable joint LCS — not the largest. An all-`a` omen caps it at the scarcest `a` count, an all-`b` omen at the scarcest `b` count, and the smaller of those two is the answer.
- **No mixed omen does better**, which is the part worth checking: verified by brute force over all $5050$ instances with $m \leq 4$ and $n \leq 3$, against the true minimum over every omen.
- **A string with no `a` forces the answer to $0$** (the second sample row, with questions `aa` and `bb`), since the all-`a` omen already shares nothing with `bb`.
- **The omen has the same length $m$ as the questions**, so length is never the binding constraint — only the letter counts are.
- **$n = 1$** reduces to the smaller of that single string's two letter counts.
- **No LCS is ever computed**, which is what makes the solution a pair of minima rather than a dynamic program over $n$ strings.
- **The alphabet is exactly $\{a, b\}$**, the omen included, which is what makes two candidate omens exhaustive.

## Dry run

Third sample: the questions are `aabb`, `abab`, `baab`.

| string | count of `a` | count of `b` |
|---|---:|---:|
| `aabb` | 2 | 2 |
| `abab` | 2 | 2 |
| `baab` | 2 | 2 |

The scarcest `a` count is $2$ and the scarcest `b` count is $2$, so the answer is $\min(2,2) = $ `2` — an omen of `aaaa` leaves a common subsequence of length $2$.
