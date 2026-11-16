[&larr; 612. Maximum Size](612-RISK.md) &middot; [Index](README.md) &middot; [614. Per Capita Income &rarr;](614-PERCAPTA.md)

# 613. Maximal Expression

> [`MAXIMALEXP`](https://www.codechef.com/problems/MAXIMALEXP) &middot; difficulty **2127** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | The two residues have one of two possible sums - split it evenly |
| **CodeChef tags** | `math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given two integers $N$ and $K$.

Let $F(X) = (X \bmod K)\times ((N-X)\bmod K)$, where $\bmod$ denotes the [modulo operator](https://en.wikipedia.org/wiki/Modulo).

Find an integer $X$ such that the value of $F(X)$ is the **maximum** over all $0\le X \le N$.
If there are multiple answers, you may print any.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two integers $N$ and $K$.

**Output**

For each testcase, print a single integer $X$ $(0\leq X\leq N)$ such that the value of $F(X)$ is the maximum over all possible $X$ from $0$ to $N$.

If there are multiple answers, you may print any.

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq N \leq 10^9$
- $1 \leq K \leq 10^9$

## Sample

**Sample input**

```
3
5 2
4 7
8 3
```

**Sample output**

```
0
2
4
```

<details><summary>Explanation</summary>

**Test case $1$:** $F(X)=0$ for all $0\leq X\leq 5$.

**Test case $2$:**
- $F(0) = (0\bmod 7)\times(4\bmod 7) = 0$
- $F(1) = (1\bmod 7)\times(3\bmod 7) = 3$
- $F(2) = (2\bmod 7)\times(2\bmod 7) = 4$
- $F(3) = (3\bmod 7)\times(1\bmod 7) = 3$
- $F(4) = (4\bmod 7)\times(0\bmod 7) = 0$

So, $X=2$ is the only correct answer.

**Test case $3$:**
- $F(X) = 0$ for $X\in\{0,2,3,5,6,8\}$
- $F(X) = 1$ for $X\in\{1,4,7\}$

So, $1$, $4$ and $7$ are all correct answers.

</details>

## Approach

Let $a = X \bmod K$ and $b = (N - X) \bmod K$. Their sum is congruent to $N$ modulo $K$ and lies in $[0, 2K - 2]$, so with $r = N \bmod K$ it is either $r$ or $r + K$; the larger sum requires $N \ge K$.

For a fixed sum the product $a \cdot b$ is largest when the two parts are as equal as possible. That gives two candidates:

- sum $r$: $X = \lfloor r / 2 \rfloor$;
- sum $r + K$ (only if $N \ge K$): $X = \lfloor (r + K) / 2 \rfloor$.

Both values are at most $N$. Evaluate $F$ at each candidate and print the better one; when the larger sum is not actually attainable (for $r = K - 1$) the second candidate just evaluates to something no better.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        residue = n % k
        candidates = [residue // 2]
        if n >= k:
            candidates.append((residue + k) // 2)
        out.append(str(max(candidates, key=lambda x: x % k * ((n - x) % k))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $K = 1$: every residue is 0 and any $X$ is correct.
- $N < K$: only the sum $r = N$ exists and $X = \lfloor N / 2 \rfloor$.
- $N = 0$: the only choice is $X = 0$.
- Several $X$ can be optimal, so the output is checked by value rather than by text.

## Dry run

`N = 4, K = 7`: $r = 4$ and $N < K$, so the only candidate is $X = 2$ with $F = 2 \cdot 2 = 4$.

`N = 8, K = 3`: $r = 2$. Candidates $X = 1$ with $F = 1 \cdot (7 \bmod 3) = 1$ and $X = 2$ with $F = 2 \cdot (6 \bmod 3) = 0$. Print 1; its value equals that of the sample answer $X = 4$.

---

Same problem grouped by topic: [../docs/basic-math/MAXIMALEXP.md](../docs/basic-math/MAXIMALEXP.md)
