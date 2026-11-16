[&larr; 710. Coin Partition](710-COINPART.md) &middot; [Index](README.md) &middot; [712. Perfect Tree Problem &rarr;](712-PTREE.md)

# 711. Adi and the Matrix

> [`ADIMAT`](https://www.codechef.com/problems/ADIMAT) &middot; difficulty **2900** &middot; time limit **1 - 1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Burnside over row cycle types with a cycle-index DP for the columns |
| **Complexity class** | Exponential subset DP $O(2^K K^2)$ |
| **Time** | $O(p(n) \cdot m^2)$, $n = \min(N, M)$, $m = \max(N, M)$ and $p$ the partition function |
| **Space** | $O(n + m)$ |

## Question

Adi likes binary matrices, i.e. matrices containing only elements $0$ and $1$. Adi is wondering how many binary matrices with $N$ rows and $M$ columns there are. Everyone knows the answer to this question - it is just $2^{N \cdot M}$. What most people do not know, however, is that Adi considers two matrices identical if and only if one of them can be turned into the other by first suitably permuting the $N$ rows of this matrix and then suitably permuting the $M$ columns of the resulting matrix.

The problem is much harder now and Adi does not know how to solve it anymore! Help Adi by finding the number of binary $N \times M$ matrices which are distinct according to his definition. Since the answer may be quite large, compute it modulo $10^9 + 7$.

**Input**
The first and only line of the input contains two space-separated integers $N$ and $M$.

**Output**
Print a single line containing one integer — the number of matrices modulo $10^9 + 7$.

**Constraints**
- $1 \le N, M, N \cdot M \le 550$

**Example Input**
```
1 5
```

**Example Output**
```
6
```

**Explanation**
According to Adi's definition, there are $6$ different binary matrices. This is because the number of $1$-s uniquely identifies a $1 \times 5$ matrix and the number of $1$-s can take any value between $0$ and $5$ inclusive.

**Example Input**
```
10 10
```

**Example Output**
```
508361223
```

## Constraints

- $1 \le N, M, N \cdot M \le 550$

## Approach

Matrices are identified under the group $S_N \times S_M$ of row and column permutations, so by Burnside's lemma the answer is the average number of matrices fixed by a pair (row permutation, column permutation).

A pair fixes a matrix when the matrix is constant on every orbit of cells. A row cycle of length $a$ and a column cycle of length $b$ together split their $a \cdot b$ cells into $\gcd(a, b)$ orbits, so the pair fixes $2^{\sum \gcd(a_i, b_j)}$ matrices.

Take $N \le M$ (swap otherwise). Enumerate the cycle type of the row permutation - a partition of $N$ - with weight $1 / \prod (\text{length}^{count} \cdot count!)$, which is the fraction of permutations with that type. For a fixed row type a column cycle of length $j$ contributes the factor $c_j = 2^{\sum_i \gcd(a_i, j)}$, and the average over all column permutations is the cycle index evaluated at these values:

$$Z_0 = 1, \qquad Z_k = \frac{1}{k} \sum_{j=1}^{k} c_j \, Z_{k-j}.$$

Summing weight times $Z_M$ over all partitions gives the answer.

## Solution

```python
import sys
from math import gcd


MOD = 1000000007


def solve():
    n, m = sorted(map(int, sys.stdin.buffer.read().split()))
    if n == 1:
        print(m + 1)
        return
    inv = [0, 1] + [0] * (m - 1)
    for i in range(2, m + 1):
        inv[i] = MOD - MOD // i * inv[MOD % i] % MOD
    answer = 0
    cycles = []

    def visit(remaining, minimum, weight):
        nonlocal answer
        if not remaining:
            fixed = [0] * (m + 1)
            for j in range(1, m + 1):
                fixed[j] = pow(2, sum((count * gcd(length, j) for length, count in cycles)), MOD)
            dp = [0] * (m + 1)
            dp[0] = 1
            for k in range(1, m + 1):
                dp[k] = sum((fixed[j] * dp[k - j] for j in range(1, k + 1))) % MOD * inv[k] % MOD
            answer = (answer + weight * dp[m]) % MOD
            return
        for length in range(minimum, remaining + 1):
            w = weight
            for count in range(1, remaining // length + 1):
                w = w * inv[length] * inv[count] % MOD
                cycles.append((length, count))
                visit(remaining - length * count, length + 1, w)
                cycles.pop()
    visit(n, 1, 1)
    print(answer)


if __name__ == "__main__":
    solve()
```

## Edge cases

- With a single row only the number of ones matters: the answer is $M + 1$.
- The recursion enumerates partitions, so the smaller dimension must be the one that is partitioned.
- All divisions are modular inverses, computed once up to $M$.
- The input is a single line with both dimensions.

## Dry run

`2 x 2`. Row types: two fixed points (weight $1/2$) and one 2-cycle (weight $1/2$).

- Two fixed rows: $c_1 = 2^{1+1} = 4$, $c_2 = 2^{1+1} = 4$. $Z_1 = 4$, $Z_2 = (c_1 Z_1 + c_2 Z_0) / 2 = (16 + 4) / 2 = 10$.
- One 2-cycle: $c_1 = 2^{1} = 2$, $c_2 = 2^{2} = 4$. $Z_1 = 2$, $Z_2 = (4 + 4) / 2 = 4$.

Answer $(10 + 4) / 2 = 7$.

---

Same problem grouped by topic: [../docs/combinatorics/ADIMAT.md](../docs/combinatorics/ADIMAT.md)
