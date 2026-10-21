# 240. Average Array

> [`AVGARR`](https://www.codechef.com/problems/AVGARR) &middot; difficulty **1424** &middot; time limit **0.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Pairing symmetrically around the mean |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Constructive` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given two integers $N$ and $X$. Output an array $A$ of length $N$ such that:
- $-1000 \le A_i \le 1000$ for all $1 \le i \le N$.
- All $A_i$ are **distinct**.
- $\texttt{mean}(A) = X$.

If there are multiple answers, print any. It is guaranteed that under the given constraints at least one array satisfying the given conditions exists.

As a reminder, the mean of an array $B$ of size $M$ is defined as: $\texttt{mean}(B) = \dfrac{\sum_{i = 1}^{M} B_i}{M}$.

For example, $\texttt{mean}([3, 1, 4, 8]) = \frac{3 + 1 + 4 + 8}{4} = \frac{16}{4} = 4$.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N$ and $X$ - the size of the array $A$ and the mean of the array $A$.

**Output**

For each test case, output an array $A$ of length $N$ which satisfies the given conditions.

## Constraints

- $1 \leq T \leq 100$
- $1 \le N \le 1000$
- $0 \le X \le 100$

## Sample

**Sample input**

```
3
3 7
5 1
1 10
```

**Sample output**

```
5 10 6
1 2 3 4 -5
10
```

<details><summary>Explanation</summary>

**Test case 1:** $\texttt{mean}([5, 10, 6]) = \frac{5 + 10 + 6}{3} = \frac{21}{3} = 7$.

**Test case 2:** $\texttt{mean}([1, 2, 3, 4, -5]) = \frac{1 + 2 + 3 + 4 + (-5)}{5} = \frac{5}{5} = 1$.

**Test case 3:** $\texttt{mean}([10]) = \frac{10}{1} = 10$.

</details>

## Approach

A mean of $X$ over $N$ elements means the total must be exactly $NX$. The clean construction builds that total out of **symmetric pairs around $X$**: the pair $(X - d,\ X + d)$ sums to $2X$ and contributes a mean of $X$ by itself.

- **$N$ even:** emit $N/2$ pairs with offsets $d = 1, 2, \ldots, N/2$.
- **$N$ odd:** emit $X$ itself, then $(N-1)/2$ such pairs.

Every value is distinct, because the offsets are distinct and positive and $X$ appears at most once.

The construction also has to respect $|A_i| \leq 1000$, which is worth checking rather than assuming. The largest offset is $\lfloor N/2 \rfloor \leq 500$, and $0 \leq X \leq 100$, so values stay within $[-500,\ 600]$ — comfortably inside the bound.

The alternative of "write $X$ many times" fails the distinctness requirement, and "fill with $0 \ldots N-1$ and patch the last element" tends to collide with an existing value or overflow the range. Pairing sidesteps both.

**Multiple answers are accepted**, so this is judged by a special checker and the output will generally differ from the sample text — the sample's `5 10 6` for $N=3, X=7$ sums to $21$, as does the `7 6 8` produced here. A verbatim diff would report a mismatch where none exists, so the repository checks this one by validating the three properties instead: correct length, all distinct, in range, and the mean exactly $X$.

$N = 1$ is the degenerate case, emitting the single value $X$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        vals = []
        if n % 2:
            vals.append(x)              # the centre contributes the mean itself
        # Each pair (x - d, x + d) averages to x, and offsets stay distinct.
        for d in range(1, n // 2 + 1):
            vals.append(x - d)
            vals.append(x + d)
        out.append(" ".join(map(str, vals)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/constructive/AVGARR.md](../docs/constructive/AVGARR.md)
