# 435. Array sorting

> CodeChef problem code [`ARRSORT`](https://www.codechef.com/problems/ARRSORT) &middot; difficulty **1681** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | GCD of the displacements |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an **unsorted** permutation $P$ of size $N$. An operation is defined as:

- Swap $P_i$ and $P_{i+K}$ for any $i$ in the range $[1,N-K]$.

Find the **maximum** value of $K$, such that, the permutation $P$ can be **sorted** by applying any finite number of operations.

Note that, a permutation of size $N$ contains all integers from $1$ to $N$ **exactly** once.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$, the size of permutation.
    - The next line contains $N$ integers describing the permutation $P$.
- It is guaranteed that the given permutation is **not sorted**.

**Output**

For each test case, output on a new line the **maximum** possible value of $K$.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $10^5$.

## Sample

**Sample input**

```
3
4
4 2 3 1
5
1 4 3 2 5
2
2 1
```

**Sample output**

```
3
2
1
```

<details><summary>Explanation</summary>

- **Test Case $1$:** Permutation can be sorted by swapping $P_1$ and $P_4$. So, the maximum possible value of $K$ is $3$. It can be shown that we cannot sort the permutation for any $K\gt 3$.

- **Test Case $2$:** Swapping $P_2$ and $P_4$ will sort the permutation. So, the maximum possible value of $K$ is $2$. It can be shown that we cannot sort the permutation for any $K\gt 2$.

- **Test Case $3$:** Swapping $P_1$ and $P_2$ will sort the permutation. So, the maximum possible value of $K$ is $1$. It can be shown that we cannot sort the permutation for any $K\gt 1$.

</details>

## Approach

A swap at distance $K$ moves an element by $K$ positions, so an element can only ever reach indices **congruent to its own mod $K$**. The index classes mod $K$ are therefore independent, and within one class the distance-$K$ swaps act as adjacent transpositions, which generate every permutation of that class. So sorting is possible exactly when every element's target index matches its current index mod $K$:

$$K \mid (P_i - i) \quad \text{for every } i$$

That makes $K$ a common divisor of all the displacements, so the largest workable value is

$$K = \gcd_i \bigl(|P_i - i|\bigr)$$

taking $\gcd(0, x) = x$ so that already-correct positions impose nothing. The permutation is guaranteed unsorted, so at least one displacement is non-zero and the GCD is positive — and since $|P_i - i| \leq N-1$, the result never exceeds $N-1$, which is the largest $K$ for which a swap even exists.

Note the two directions matter equally: divisibility is *necessary* because of the residue classes, and *sufficient* because each class can be sorted internally — neither half alone would justify taking the GCD.

The samples show the range. $[4,2,3,1]$ displaces only the ends, by $3$ each, so $K = 3$: one swap of positions $1$ and $4$ sorts it. $[1,4,3,2,5]$ displaces two elements by $2$, giving $K = 2$. And $[2,1]$ has displacements $1$ and $1$, so $K = 1$ — adjacent swaps, the weakest operation, are all that works.

## Solution (Python)

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # gcd(0, x) == x, so sorted positions impose no constraint.
        step = 0
        for i in range(n):
            step = gcd(step, abs(int(data[pos + 1 + i]) - (i + 1)))
        pos += 1 + n
        out.append(str(step))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Number Theory`, `Algorithms`
