---
topic: Combinatorics
subtopic: Elementary symmetric polynomials by DP
time: $O(m \min(K, m))$ after an $O(N)$ tally, where $m$ is the number of distinct values
space: $O(m)$
---
A good subsequence never repeats a value, so it is built by **choosing a set of distinct values and then one occurrence of each**. If value $v$ appears $c_v$ times, a chosen set $S$ can be realised in $\prod_{v \in S} c_v$ ways, so the number of good subsequences of size exactly $j$ is the **elementary symmetric polynomial**

$$e_j(c_1, \ldots, c_m) = \sum_{|S| = j} \prod_{v \in S} c_v$$

and the answer is $\sum_{j=0}^{K} e_j$, with $e_0 = 1$ for the empty subsequence.

The $e_j$ come from the standard product expansion $\prod_v (1 + c_v x)$, evaluated as a DP over values: $\mathrm{dp}[j] \mathrel{+}= c_v \cdot \mathrm{dp}[j-1]$, sweeping $j$ downward so each value is used at most once.

The crucial bound is that the $A_i$ are **primes at most $8000$**, of which there are $1007$. So $m \leq 1007$ regardless of $N = 10^5$, and $e_j = 0$ for $j > m$ — you cannot pick more distinct values than exist. Capping $K$ at $m$ turns a nominal $O(NK) = 10^{10}$ into about $10^6$ operations.

For the sample $[2,2,3,3,5]$ with $K = 3$ the multiplicities are $2, 2, 1$, giving $e_0 = 1$, $e_1 = 5$, $e_2 = 2{\cdot}2 + 2{\cdot}1 + 2{\cdot}1 = 8$ and $e_3 = 4$, summing to $18$. Note $e_1 = 5 = N$: picking one element is always $N$ ways, since different occurrences of the same value are different subsequences.

That the values are prime is a red herring — only their distinctness matters — and the input has a single case with no leading $T$.
