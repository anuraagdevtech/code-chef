[&larr; 678. Is This JEE](ICM2003.md) &middot; [Index](../../README.md)

# 714. Two Averages

> CodeChef problem code [`TWOAVG`](https://www.codechef.com/problems/TWOAVG) &middot; difficulty **2353** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Only K into A and 1 into B help; binary search the number of appends |
| **Time** | $O(N + M + \log \text{answer})$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef has an array $A$ of size $N$ such that $1 \le A_i \le K$ for all $1 \le i \le N$. $\\$
Chef also has another array $B$ of size $M$ such that $1 \le B_i \le K$ for all $1 \le i \le M$

Chef can perform the following operation: $\\$
**1)** Select an integer $X$ such that $1 \le X \le K$ $\\$
**2)** Append $X$ to the end of exactly one array among $A$ and $B$

Find the **minimum** number of operations required to make $mean(A)$ **strictly** greater than $mean(B)$ or determine it is not possible to do so.

For an array $X$ of length $M$, $mean(X)$ is defined as $\frac{\Sigma X_i}{M}$. For example,
- $mean([5, 6]) = \frac{5+6}{2} = 5.5$
- $mean([10, 13, 20]) = \frac{10+13+20}{3} = 14.333...$
- $mean([3, 3, 3, 3, 3]) = 3$

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains three space-separated integers $N$, $M$ and $K$ - the size of array $A$, the size of array $B$ and the upper bound of values in arrays $A$ and $B$.
    - The next line contains $N$ space-separated integers $A_1$, $A_2$, ..., $A_N$ denoting the array $A$.
    - The third line contains $M$ space-separated integers $B_1$, $B_2$, ..., $B_M$ denoting the array $B$.

**Output**

For each test case, output the minimum number of operations required to make $mean(A) > mean(B)$.

Output $-1$ if it is not possible to do so.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, M \leq 10^5$
- $1 \leq K \leq 10^6$
- $1 \leq A_i, B_i \leq K$
- Sum of $N$ over all test cases won't exceed $10^5$.
- Sum of $M$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
4
6 3 9
3 7 3 5 2 4
8 3 5
1 1 4
4
2
2 2 1
1 1
1 1
5 5 5
3 4 3 4 3
4 5 4 5 4
```

**Sample output**

```
2
0
-1
3
```

<details><summary>Explanation</summary>

**Test case 1:** $A = [3, 7, 3, 5, 2, 4]$ and $B = [8, 3, 5]$. Chef can perform the following operations:
- Append $X = 8$ to array $A$
- Append $X = 2$ to array $B$

After that, $mean(A)=\frac{3+7+3+5+2+4+8}{7} = 4.5714...$ and $mean(B)=\frac{8+3+5+2}{4} = 4.5$

**Test case 2:** There is no need to append new elements as $mean(A)=4 > 2=mean(B)$.

**Test case 3:** As $K=1$, it is impossible to make $mean(A) > mean(B)$ as $mean(A) = mean(B) = 1$ no matter how many operations Chef performs.

**Test case 4:** Chef can append $2$, $1$ and $2$ to array $B$ in three operations.

</details>

## Approach

To push $mean(A)$ above $mean(B)$, an append to $A$ should be as large as possible ($K$) and an append to $B$ as small as possible (1). If $K = 1$ all values are 1 and the means are always equal: answer $-1$. Otherwise appending enough $K$'s and 1's always works, so an answer exists.

Fix the total number of appends $z$ and let $x$ of them go to $A$. The condition, cross-multiplied to stay in integers, is

$$(S_A + K x)(M + z - x) > (S_B + z - x)(N + x).$$

The difference of the two sides is a quadratic in $x$ with leading coefficient $-(K - 1) < 0$, hence concave: its maximum over the integers of $[0, z]$ is attained at an endpoint or at one of the two integers around the vertex. Testing those four candidates decides whether $z$ appends suffice.

More appends never hurt, so feasibility is monotone in $z$: double an upper bound until it is feasible, then binary search for the smallest feasible $z$.

## Solution (Python)

```python
import sys


def solve(tokens):
    n, m, k = (next(tokens), next(tokens), next(tokens))
    sum_a = sum((next(tokens) for _ in range(n)))
    sum_b = sum((next(tokens) for _ in range(m)))
    if k == 1:
        return '-1'

    def ok(z):
        numerator = k * (m + z) - sum_a - sum_b - z + n
        denominator = 2 * (k - 1)
        x = numerator // denominator
        for t in (0, z, max(0, min(z, x)), max(0, min(z, x + 1))):
            if (sum_a + k * t) * (m + z - t) > (sum_b + z - t) * (n + t):
                return True
        return False
    low = -1
    high = 1
    while not ok(high):
        high *= 2
    while high - low > 1:
        mid = (high + low) // 2
        if ok(mid):
            high = mid
        else:
            low = mid
    return str(high)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N + M + \log \text{answer})$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The means may already satisfy the inequality: answer 0.
- The inequality is strict; equality does not count.
- $K = 1$ is the only impossible case.
- Cross-multiplication avoids floating point entirely.

## Dry run

`A = [3, 7, 3, 5, 2, 4]` (sum 24), `B = [8, 3, 5]` (sum 16), `K = 9`.

- $z = 0$: $24 \cdot 3 = 72 > 16 \cdot 6 = 96$? No.
- $z = 1$: appending 9 to $A$ gives $33 \cdot 3 = 99$ against $16 \cdot 7 = 112$; appending 1 to $B$ gives $24 \cdot 4 = 96$ against $17 \cdot 6 = 102$. No.
- $z = 2$, $x = 1$: $33 \cdot 4 = 132 > 17 \cdot 7 = 119$. Yes.

Answer 2.

> CodeChef tags: `Algorithms`, `Searching`

---

Same problem in rating order (#678 of 735): [../../by-rating/678-TWOAVG.md](../../by-rating/678-TWOAVG.md)
