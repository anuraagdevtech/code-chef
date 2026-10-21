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
