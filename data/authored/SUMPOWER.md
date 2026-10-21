---
topic: Prefix Sums
subtopic: Counting each boundary's contribution
time: $O(N)$ per test case
space: $O(1)$
---
Board slot $j$ shows $S_{i+j}$ at step $i$ and $S_{i+j+1}$ at step $i+1$, so it changes exactly when those two characters differ. The power of one switch is therefore the number of **adjacent mismatches** inside a window:

$$\text{power}(i) = \sum_{p=i}^{i+K-1} d_p, \qquad d_p = [\,S_p \neq S_{p+1}\,]$$

Summing over all $N-K$ switches and swapping the order of summation turns the double sum into a weighted single sum: each boundary $p$ is counted once for every step $i$ whose window covers it, that is for $i \in [\max(1, p-K+1),\ \min(N-K, p)]$. So

$$\text{answer} = \sum_{p=1}^{N-1} d_p \cdot \Bigl(\min(N-K,\, p) - \max(1,\, p-K+1) + 1\Bigr)$$

with negative weights clamped to zero. Counting by contribution is what makes this linear — evaluating each window separately would be $O(NK)$, which at $\sum N = 10^6$ and $K$ near $N$ is hopeless.

A boundary near either end of the string gets a smaller weight, because fewer windows reach it; interior boundaries get the full $\min(K, N-K)$.

The samples make the weights visible. `aabbcc` with $K = 3$ has mismatches at $p = 2$ and $p = 4$, each covered by two of the three steps, giving $4$. `abccc` with $K = 2$ has mismatches at $p = 1$ and $p = 2$, weighted $1$ and $2$, giving $3$. And `aabb` with $K = 3$ has a single switch and a single mismatch inside it, giving $1$.
