[&larr; 665. XOR Sums](665-SUMXOR2.md) &middot; [Index](README.md) &middot; [667. Merging Binary Strings &rarr;](667-MERGEBS.md)

# 666. Chefs Favourite Function

> [`CHEFFFUNC`](https://www.codechef.com/problems/CHEFFFUNC) &middot; difficulty **2316** &middot; time limit **5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Closed forms for f and g, and only O(log R) candidates |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Bitwise Operation`, `Brute Force` |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log R)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef's new friend hErd gave him two functions $f$ and $g$.

- The function $f$ is defined over $x$ $(x\geq 1)$ as:
$$
f(x) = \begin{cases}
0, & \text{if } x = 1 \\
f\left( \frac{x}{2} \right) + 1, & \text{if } x \text{ is even} \\
f\left( \left\lfloor \frac{x}{2} \right\rfloor \right), & \text{if } x \text{ is odd} \\
\end{cases}
$$

- The function $g$ is defined over $x$ $(x\geq 1)$ as:
$$
g(x) = \begin{cases}
1, & \text{if } x = 1 \\
2\cdot g\left( \frac{x}{2} \right) + 1, & \text{if } x \text{ is even} \\
2\cdot g\left( \left\lfloor \frac{x}{2} \right\rfloor \right), & \text{if } x \text{ is odd} \\
\end{cases}
$$

where $\left\lfloor z \right\rfloor$, denotes the greatest integer less than or equal to $z$.

He also gave Chef two integers $L$ and $R$. Chef has to find the **maximum** value of $f(x)+g(x)$ for $L \leq x \leq R$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains two space-separated integers $L$ and $R$, as mentioned in the statement.

**Output**

For each test case, output on a new line the **maximum** value of $f(x)+g(x)$ for $L \leq x \leq R$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq L \leq R \leq 10^9$

## Sample

**Sample input**

```
3
1 1
1 2
1 20
```

**Sample output**

```
1
4
35
```

<details><summary>Explanation</summary>

**Test case $1$:** $f(1)=0$ and $g(1)=1$. Hence, $f(x) + g(x) = 1$.

**Test case $2$:** There are $2$ possible values of $x$.
- $x = 1$: $f(1)+g(1)=1$
- $x = 2$: $f(2)+g(2)=(f(1) + 1) + (2\cdot g(1) + 1) = 1 + 3 = 4$.

Hence the maximum value of $f(x) + g(x) = 4$.

</details>

## Approach

Unrolling the recursions over the binary digits of $x$ (a $k$-bit number):

- $f$ adds 1 for every 0 digit below the leading one: $f(x) = k - \text{popcount}(x)$.
- $g$ rebuilds the number with all digits below the leading one flipped: $g(x) = 3 \cdot 2^{k-1} - 1 - x$.

So within a fixed bit length we want to minimise $x + \text{popcount}(x)$, and longer numbers have a much larger constant term.

Take any $x > L$ in the range and look at the highest bit where $x$ and $L$ differ; $x$ has a 1 there and $L$ a 0. Clearing all lower bits of $x$ keeps it above $L$, keeps its bit length, and reduces both $x$ and its popcount. Hence some optimum is either $L$ itself or $L$ rounded up to a multiple of $2^j$ for some $j$. These are $O(\log R)$ candidates - they include the powers of two where the bit length changes - and each one that does not exceed $R$ is evaluated with the closed forms.

## Solution

```python
import sys


def solve(tokens):
    low, high = (next(tokens), next(tokens))
    best = 0
    for j in range(high.bit_length() + 1):
        candidate = low + (1 << j) - 1 >> j << j
        if candidate <= high:
            bits = candidate.bit_length()
            best = max(best, 3 * (1 << bits - 1) - 1 - candidate + bits - candidate.bit_count())
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $L = R$: only one candidate.
- Rounding up with $j = 0$ gives $L$ itself.
- A power of two inside the range is usually the best choice for its bit length: $x$ and the popcount are both minimal.
- Candidates beyond $R$ are discarded.

## Dry run

`L = 1, R = 20`. Candidates are 1 rounded up to multiples of 1, 2, 4, 8, 16, 32: `1, 2, 4, 8, 16` (32 is too large).

For $x = 16$ ($k = 5$): $g = 3 \cdot 16 - 1 - 16 = 31$ and $f = 5 - 1 = 4$, total 35. The other candidates give 1, 4, 9 and 18.

Answer 35.

---

Same problem grouped by topic: [../docs/bit-manipulation/CHEFFFUNC.md](../docs/bit-manipulation/CHEFFFUNC.md)
