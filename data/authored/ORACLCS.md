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
