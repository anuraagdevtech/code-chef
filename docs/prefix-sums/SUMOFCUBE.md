[&larr; 670. Cherry and Bits](CENS20A.md) &middot; [Index](../../README.md)

# 691. Sum of Cube 

> CodeChef problem code [`SUMOFCUBE`](https://www.codechef.com/problems/SUMOFCUBE) &middot; difficulty **2259** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Expand the cube of a prefix difference and keep three running power sums |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given an array $A$ consisting of $N$ positive integers.

Find $\sum_{i=1}^{N} \sum_{j=i}^{N} F^3(i,j)$, where $F(i,j)=\sum_{k=i}^{j} A_k$.

Since the value might be quite large, print it modulo $998244353$.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

**Output**

For each test case, output on a new line, the answer, modulo $998244353$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 5 \cdot 10^5$
- $1 \leq A_i \leq 10^6$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
2
1 1
3
1 2 1
5
8 5 6 2 3
```

**Sample output**

```
10
128
42621
```

<details><summary>Explanation</summary>

**Test case $1$:** $F(1, 1) = 1, F(1, 2) = 1+1=2, F(2, 2) = 1$.

Thus, $\sum_{i=1}^{N} \sum_{j=i}^{N} F^3(i,j) = 1^3 + 2^3 + 1^3 = 10$.

**Test case $2$:** $F(1, 1) = 1, F(1, 2) = 1+2=3, F(1, 3) = 1+2+1 =4, F(2, 2) = 2, F(2, 3) = 2+1=3, F(3, 3) = 1$.

Thus, $\sum_{i=1}^{N} \sum_{j=i}^{N} F^3(i,j) = 1^3 + 3^3 + 4^3+2^3+3^3+1^3 = 128$.

</details>

## Approach

With prefix sums $P_0 = 0, P_1, \dots, P_N$, a subarray sum is $P_j - P_i$ for $i < j$, and

$$(P_j - P_i)^3 = P_j^3 - 3 P_j^2 P_i + 3 P_j P_i^2 - P_i^3.$$

Fix $j$ and sum over the $j$ earlier prefixes $i = 0 \dots j - 1$:

$$j \cdot P_j^3 - 3 P_j^2 \, S_1 + 3 P_j \, S_2 - S_3,$$

where $S_1, S_2, S_3$ are the sums of the first, second and third powers of the earlier prefix sums. So one pass suffices: compute the new prefix, add the expression to the answer, then add the powers of the new prefix to the three running sums. $P_0 = 0$ contributes nothing to the sums but is counted in the factor $j$.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    MOD = 998244353
    prefix = s1 = s2 = s3 = total = 0
    for i in range(1, n + 1):
        prefix = (prefix + next(tokens)) % MOD
        p2 = prefix * prefix % MOD
        p3 = p2 * prefix % MOD
        total = (total + i * p3 - 3 * p2 * s1 + 3 * prefix * s2 - s3) % MOD
        s1 = (s1 + prefix) % MOD
        s2 = (s2 + p2) % MOD
        s3 = (s3 + p3) % MOD
    return str(total)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Everything is reduced modulo $998244353$, including the prefix sums themselves.
- The factor in front of $P_j^3$ is $j$, the number of earlier prefixes including $P_0$.
- Negative intermediate values are fixed by the final reduction.
- A single element gives its cube.

## Dry run

`A = [1, 1]`, prefixes $P_1 = 1$, $P_2 = 2$.

- $j = 1$: $1 \cdot 1 - 0 + 0 - 0 = 1$. Sums become $S_1 = S_2 = S_3 = 1$.
- $j = 2$: $2 \cdot 8 - 3 \cdot 4 \cdot 1 + 3 \cdot 2 \cdot 1 - 1 = 9$.

Total 10 = $1^3 + 1^3 + 2^3$.

> CodeChef tags: `Algorithms`, `Simple Algos`

---

Same problem in rating order (#653 of 735): [../../by-rating/653-SUMOFCUBE.md](../../by-rating/653-SUMOFCUBE.md)
