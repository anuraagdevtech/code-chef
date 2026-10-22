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

## Edge cases

- **$pref_i = suf_{i+1}$ means the running sum hits exactly half the total**, since the two partition every character — so the question is how often the prefix sum of $B$ equals $M \cdot (\text{ones in } A) / 2$.
- **An odd total is impossible** → $0$, which must be checked before any division.
- **An all-zero $A$ makes every index good**, since all the sums are $0$ — giving $N M$, the only case where the answer is quadratic in the input size.
- **Only one or two copies can host a match.** Inside copy $j$ the prefix sum is $j \cdot \text{ones} + pref_A(r)$, and $pref_A(r)$ lies in $[0, \text{ones}]$ — so $j$ must be $\lfloor H/\text{ones} \rfloor$ or one less.
- **The positions are counted by prefix value**, so a tally over one copy of $A$ answers both candidates in constant time.
- **The index $i = 0$ is excluded** ($1 \le i$), which the tally respects by only recording positions $1 \dots N$.
- **$N M$ reaches $10^{10}$** in the all-zero case, past 32-bit.

## Dry run

Third sample: $A = $ `101`, $M = 3$, so $B = $ `101101101` with $6$ ones and a half of $3$.

| prefix value within one copy | positions reaching it |
|---:|---|
| 1 | $r = 1, 2$ |
| 2 | $r = 3$ |

With $\text{ones} = 2$, the base copy is $\lfloor 3/2 \rfloor = 1$:

| copy $j$ | needed $pref_A(r)$ | matches |
|---:|---:|---:|
| 0 | $3 - 0 = 3$ | 0 |
| 1 | $3 - 2 = 1$ | 2 |

Output `2` — the good indices are $4$ and $5$.
