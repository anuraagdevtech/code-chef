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

## Edge cases

- **$A_i = 1$ pairs with every $j$**, since $1^j = 1 \leq A_j$ for all $A_j \geq 1$ — contributing $(\text{count of ones}) \times N$ before any root is taken.
- **For $A_i \geq 2$ only $j \leq 29$ can work**, because $2^j \leq A_j \leq 10^9$ bounds the exponent — which is what keeps the loop at $30$ iterations instead of $N$.
- **The exponent is the *index* $j$, not a value**, so the bound comes from the position; `a[j - 1]` reads $A_j$ from the original array while the sorted copy serves the counting.
- **The integer root must be exact.** `round(a ** (1.0/j))` can land one off for large $a$, so it is corrected by stepping down while $r^j > a$ and up while $(r+1)^j \leq a$.
- **A limit below $2$ means no $A_i \geq 2$ qualifies**, which the `if limit >= 2` guard skips — otherwise the ones would be double-counted.
- **Ordered pairs are counted**, so $(1,2)$ and $(2,1)$ are distinct and $i = j$ is allowed.
- **Sum of $N \leq 2 \cdot 10^5$**: one sort plus $30$ binary searches per case.

## Dry run

Third sample: $A = 1000, 100, 1, 10, 1$, sorted to $1, 1, 10, 100, 1000$ with two ones.

| contribution | count |
|---|---:|
| ones paired with every $j$ ($2 \times 5$) | 10 |
| $j = 1$: $A_i \leq \sqrt[1]{1000} = 1000$, excluding ones | 3 |
| $j = 2$: $A_i \leq \sqrt{100} = 10$, excluding ones | 1 |
| $j = 3, 4, 5$: limits are $1$, so nothing | 0 |

Total `14`.
