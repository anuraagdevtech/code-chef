---
topic: Sorting
subtopic: Bounding the exponent, then counting by integer root
time: $O(N \log N + 30 \log N)$ per test case
space: $O(N)$
---
Two observations shrink the $N^2$ pair space to almost nothing.

**Ones are free.** If $A_i = 1$ then $A_i^j = 1 \leq A_j$ for every $j$, since all values are positive. So each index holding a $1$ contributes $N$ pairs outright.

**Otherwise the exponent is tiny.** If $A_i \geq 2$ then $A_i^j \geq 2^j$, and the condition forces $2^j \leq A_j \leq 10^9$, so $j \leq 29$. Only the first $30$ indices can ever be the second element of a pair — the rest of the array is irrelevant as a $j$.

For each such $j$, the condition $A_i^j \leq A_j$ with $A_i \geq 2$ is just $A_i \leq \lfloor A_j^{1/j} \rfloor$. So sort a copy of $A$ once and answer each $j$ with a binary search:

$$\text{answer} = c_1 \cdot N + \sum_{j=1}^{\min(N,30)} \Bigl(\#\{\,i : 2 \leq A_i \leq \lfloor A_j^{1/j} \rfloor\,\}\Bigr)$$

where $c_1$ is the number of ones. Compute the root with an integer routine and correct it by stepping, since `a ** (1/j)` in floating point is off by one near exact powers and would silently miscount.

The third sample is the one that shows both parts. $A = [1000, 100, 1, 10, 1]$ has two ones, contributing $2 \cdot 5 = 10$ pairs. Then $j = 1$ admits $A_i \leq 1000$, i.e. all three non-one values, and $j = 2$ admits $A_i \leq \lfloor\sqrt{100}\rfloor = 10$, i.e. just the $10$. Total $10 + 3 + 1 = 14$.

Note $(i,j)$ with $i = j$ is allowed, which is where $j = 1$ picking up $A_1$ itself comes from in the first sample.
