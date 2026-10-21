# 439. Average Gift

> CodeChef problem code [`AVGGIFT`](https://www.codechef.com/problems/AVGGIFT) &middot; difficulty **1701** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Mean reachability as a sign condition |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has a set $S$ containing $N$ **distinct** integers.

Chef wants to gift Chefina an array $A$ of any finite length such that the following conditions hold true:

- $A_i \in S$ $\forall i$. In other words, each element of the array $A$ should belong to the set $S$.
- [Mean](https://en.wikipedia.org/wiki/Mean) value of all the elements in $A$ is **exactly** $X$.

Find whether there exists an array $A$ of finite length satisfying the above conditions.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- First line of each test case contains two integers $N$ and $X$ - denoting the size of set $S$ and the mean value of the required array.
- Second line contains $N$ distinct integers $S_1, S_2, \dots , S_N$ - denoting the set $S$.

**Output**

For each test case, output in a single line, `YES` if there exists an array satisfying the given conditions, `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq S_i \leq 10^9$
- $1 \leq X \leq 10^9$
- $S_i \neq S_j$ for $ i \neq j$
- Sum of $N$ over all test case do not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
4
3 2
1 2 3
1 5
3
2 5
4 6
1 5
5
```

**Sample output**

```
YES
NO
YES
YES
```

<details><summary>Explanation</summary>

**Test Case $1$:** One of the valid arrays is $A = [2,2]$. Here, $2 \in \{1, 2, 3\}$. Also, mean value of the array is $\frac{2+2}{2} = 2$.

**Test Case $2$:** Since all elements of the array can only be equal to $3$, the mean value of $A$ cannot be equal to $5$.

**Test Case $3$:** One of the valid arrays is $A = [4,6]$. Here, $4 \in \{4, 6\}$ and $6 \in \{4, 6\}$. Also, mean value of the array is $\frac{4+6}{2} = 5$.

**Test Case $4$:** One of the valid arrays is $A = [5]$. Here, $5 \in \{5\}$. Also, mean value of the array is $\frac{5}{1} = 5$.

</details>

## Approach

An array with elements $S_i$ repeated $c_i \geq 0$ times has mean $X$ exactly when

$$\sum_i c_i S_i = X \sum_i c_i \quad\Longleftrightarrow\quad \sum_i c_i\,(S_i - X) = 0$$

with the $c_i$ not all zero. So the problem is whether the shifted values $S_i - X$ admit a non-trivial non-negative integer combination summing to zero.

That is possible in exactly two ways:

- some $S_i - X$ is **zero** — then the one-element array $[X]$ works;
- some value is **positive** and another **negative** — if $p > 0$ and $-q < 0$ are available, take $q$ copies of the first and $p$ copies of the second, giving $qp - pq = 0$.

If every shifted value has the same strict sign, every non-trivial sum inherits that sign and can never vanish. Combining the cases, the condition collapses to a range test:

$$\text{answer} = \text{YES} \iff \min S \leq X \leq \max S$$

The array may be as long as needed, so there is no size constraint to worry about — the integer multiples above are always allowed.

The samples cover the three shapes. $S = \{1,2,3\}$ with $X = 2$ contains $X$ outright. $S = \{4,6\}$ with $X = 5$ has values on both sides, so $[4,6]$ has mean $5$ even though $5 \notin S$. $S = \{5\}$ with $X = 5$ is the degenerate single-element case, `YES`. And $S = \{3\}$ with $X = 5$ is out of range — every element is $3$, so every mean is $3$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        vals = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        # Zero is reachable iff some shifted value is 0, or signs differ.
        out.append("YES" if min(vals) <= x <= max(vals) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`
