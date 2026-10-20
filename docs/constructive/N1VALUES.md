# 267. Exactly N plus 1 Values

> CodeChef problem code [`N1VALUES`](https://www.codechef.com/problems/N1VALUES) &middot; difficulty **1495** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Building a sum from a run plus a remainder |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You are given a positive integer $N$. You have to print exactly $N + 1$ positive integers
satisfying the following conditions:

- Exactly one value should appear twice, all the remaining values should appear only once.
- Sum of all these values should be equal to $2^N$.

You have to print the values in non-decreasing order. If there are multiple solutions, you can print any of them.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**

For each test case, print a single line containing $N + 1$ positive integers in non-decreasing order that satisfy the given conditions. If there are multiple solutions, you may print any of them.

## Constraints

- $1 \le T \le 60$
- $1 \le N \le 60$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
2
3
4
```

**Sample output**

```
1 2 2 3
1 2 3 3 7
```

<details><summary>Explanation</summary>

**Test Case $1$:** $2$ is repeated twice and the remaining elements occurred only once and the sum of all the elements is equal to $8$, which is $2^3$.

**Test Case $2$:** $3$ is repeated twice and the remaining elements occurred only once and the sum of all the elements is equal to $16$, which is $2^4$.

</details>

## Approach

We need $N+1$ positive integers summing to $2^N$, with exactly one value repeated and the rest distinct.

Start from the cheapest distinct run, $1, 2, \ldots, N-1$, which uses $N-1$ of the slots and contributes $\frac{N(N-1)}{2}$. Two slots remain. Fill one by **repeating $N-1$** — that supplies the required duplicate — and let the last slot absorb everything left over:

$$L = 2^N - \frac{N(N-1)}{2} - (N-1)$$

The result, sorted, is $1, 2, \ldots, N-2,\ N-1,\ N-1,\ L$.

This works because $2^N$ grows exponentially while the run grows quadratically, so $L$ is comfortably larger than $N-1$ for every $N \geq 2$ — which keeps it distinct from the rest and keeps the list non-decreasing without re-sorting. At $N = 5$, for instance, $L = 32 - 10 - 4 = 18$.

$N = 1$ needs its own answer: two values summing to $2$, and since exactly one value must repeat, the only option is `1 1`.

The construction reproduces both samples exactly — $N = 3$ gives `1 2 2 3` and $N = 4$ gives `1 2 3 3 7` — though **any valid answer is accepted**, so this is judged by a checker rather than by text.

$N$ reaches $60$, so $2^N$ is about $1.15 \times 10^{18}$ — inside a signed 64-bit range, but only just, and worth noting for a C implementation.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        if n == 1:
            out.append("1 1")
            continue
        # 1..n-1 distinct, then repeat n-1, then absorb the remainder.
        vals = list(range(1, n)) + [n - 1]
        vals.append((1 << n) - n * (n - 1) // 2 - (n - 1))
        out.append(" ".join(map(str, vals)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`
