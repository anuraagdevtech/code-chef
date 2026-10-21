---
topic: Prefix Sums
subtopic: Splitting a repeated string's running total
time: $O(N + M)$ per test case
space: $O(N)$
---
Let $\Sigma$ be the total number of ones in $B$, so $\Sigma = M \cdot S$ with $S$ the count in one copy of $A$. Since $\mathrm{suf}_{i+1} = \Sigma - \mathrm{pref}_i$, the condition $\mathrm{pref}_i = \mathrm{suf}_{i+1}$ is simply

$$2\,\mathrm{pref}_i = \Sigma$$

So if $M S$ is **odd** the answer is $0$ outright, and otherwise the task is to count the indices where the running total equals $H = MS/2$.

Because $B$ is $M$ copies of $A$, an index inside copy $j$ (0-indexed) at offset $k$ has $\mathrm{pref} = jS + \mathrm{pref}^A_k$. Setting that equal to $H$ gives

$$\mathrm{pref}^A_k = H - jS = S\left(\tfrac{M}{2} - j\right)$$

and since $0 \leq \mathrm{pref}^A_k \leq S$, only $j \in \{\lfloor H/S \rfloor - 1,\ \lfloor H/S \rfloor\}$ can contribute. So tally the prefix values of $A$ once and look up at most two targets — no need to build $B$, whose length can reach $10^{10}$.

The all-zero case is separate and striking: with $S = 0$ every prefix is $0 = H$, so **every** index is good. That is the first sample, $N = M = 2$ on `00`, giving $4$.

For `11` with $M = 4$, $H = 4$ is reached only at the very middle of $B$, so the answer is $1$. And for `101` with $M = 3$, $H = 3$ is hit twice — at the `1` ending copy $2$'s first character and again at the `0` after it — giving $2$.
