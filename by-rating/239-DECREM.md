# 239. Decreasing Srrnmieeda

> [`DECREM`](https://www.codechef.com/problems/DECREM) &middot; difficulty **1423** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A strictly decreasing chain of remainders |
| **CodeChef tags** | `Mathematics`, `Set Theory`, `Algorithms`, `Pigeonhole Principle`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given two integers $L$ and $R$. Find the smallest non-negative integer $N$ such that
$$N \,\%\, L \gt N \,\%\, (L + 1) \gt \ldots \gt N \,\%\, (R - 1) \gt N \,\%\, R \,.$$

Here, $\%$ is the modulo operator, so $A \,\%\, B$ is the remainder of $A$ after division by $B$. For example, $11 \,\%\, 3 = 2$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.

**Output**
For each test case, print a single line containing one integer ― the smallest possible $N$, or $-1$ if no solution exists.

It is guaranteed that when a solution exists, the smallest solution does not exceed $10^{18}$.

**Constraints**
- $1 \le T \le 10^5$
- $1 \le L \lt R \le 10^6$

## Constraints

- $1 \le T \le 10^5$
- $1 \le L \lt R \le 10^6$

## Sample

**Sample input**

```
2
4 6
1 2
```

**Sample output**

```
6
-1
```

<details><summary>Explanation</summary>

**Example case 1:** $N = 6$ satisfies the given condition, since $6 \,\%\, 4 \,(= 2) \gt 6 \,\%\, 5 \,(= 1) \gt 6 \,\%\, 6 \,(= 0)$. Notice that $N = 7$ also satisfies the condition, but it is larger.

**Example case 2:** It is impossible to find a valid solution because for any non-negative integer $N$, we have $N \,\%\, 1 \,(= 0) \le N \,\%\, 2$.

</details>

## Approach

Two observations settle this completely.

**When no solution exists.** The chain $N \bmod L > N \bmod (L+1) > \cdots > N \bmod R$ holds $R - L + 1$ strictly decreasing non-negative integers, so its first term must be at least $R - L$. But $N \bmod L \leq L - 1$ always, so a solution requires

$$L - 1 \geq R - L \quad\Longleftrightarrow\quad R \leq 2L - 1 \quad\Longleftrightarrow\quad R < 2L$$

If $R \geq 2L$ the answer is $-1$. That single test also covers $L = 1$, where $N \bmod 1 = 0$ can never exceed anything.

**When it does, the answer is $N = R$.** For every $k$ in $[L, R]$ we have $k \geq L > R/2$, so $R < 2k$ and therefore $R \bmod k = R - k$. The chain becomes $R-L,\ R-L-1,\ \ldots,\ 1,\ 0$ — strictly decreasing, exactly as required.

It is also the **smallest** such $N$. Any $N < R$ has $N \bmod R = N$, while $N \bmod (R-1)$ is either $N$ itself (when $N < R-1$) or $0$ (when $N = R-1$). The first case needs $N > N$ and the second needs $0 > R-1$; both are impossible. So nothing below $R$ works.

Sample case 1 has $L=4, R=6$ with $6 < 8$, giving $N = 6$: the remainders are $2, 1, 0$. Sample case 2 has $L=1, R=2$ and $2 \geq 2$, so $-1$.

The promise that answers fit in $10^{18}$ is generous — the answer is never larger than $R \leq 10^6$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        l, r = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The chain needs r - l + 1 decreasing values starting below l, so it
        # only fits when r < 2l; then n = r gives remainders r-l, ..., 1, 0.
        out.append(str(r) if r < 2 * l else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$n = r$ is the canonical witness.** Dividing $r$ by each $d \in [l, r]$ gives remainders $r - l, r - l - 1, \ldots, 1, 0$ — decreasing by exactly one each step — provided every divisor exceeds $r/2$ so the quotient is $1$ throughout. That condition is precisely $r < 2l$.
- **When $r \geq 2l$ no $n$ works at all.** Some divisor $d \leq r/2$ then has a quotient of $2$ or more, which breaks the chain, and the answer is $-1$. Checked exhaustively against brute force for all $1 \leq l < r \leq 39$ with no mismatch.
- **$l = 1$ is always hopeless**: $n \bmod 1 = 0$ is the first term and nothing can be smaller, and indeed $r \geq 2 = 2l$ holds automatically. The second sample row is this case.
- **$L < R$ is guaranteed**, so the chain always has at least two terms and the degenerate single-remainder case never arises.
- **The answer can be as large as $10^6$** and needs no search — it is read straight off $R$.
- **$T$ up to $10^5$** with constant work per case.

## Dry run

First sample: $L = 4$, $R = 6$, and $6 < 8$, so $n = 6$.

| divisor $d$ | $6 \bmod d$ |
|---:|---:|
| 4 | 2 |
| 5 | 1 |
| 6 | 0 |

Strictly decreasing, so `6`. The second row has $L = 1$, $R = 2$: $2 \bmod 1 = 0$ already, and nothing is below it, so `-1`.

---

Same problem grouped by topic: [../docs/number-theory/DECREM.md](../docs/number-theory/DECREM.md)
