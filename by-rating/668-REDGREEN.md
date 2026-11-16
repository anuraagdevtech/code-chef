[&larr; 667. Merging Binary Strings](667-MERGEBS.md) &middot; [Index](README.md) &middot; [669. Palindrome In Making &rarr;](669-MAKEPAL3.md)

# 668. Red Green Grids

> [`REDGREEN`](https://www.codechef.com/problems/REDGREEN) &middot; difficulty **2319** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Count (grid, path) pairs path by path |
| **CodeChef tags** | `Mathematics`, `Combinatorics` |
| **Complexity class** | Logarithmic $O(\log n)$ (one-off precomputation) |
| **Time** | $O(N + M)$ precomputation, $O(\log (N M))$ per test case |
| **Space** | $O(N + M)$ |

## Question

There is an empty grid (all cells are colored white) of $N$ rows and $M$ columns.

Chef can fill each cell with either `RED` or `GREEN` color.
Chef defines a *valid* path as a path of cells starting from $(1,1)$ and ending at $(N,M)$, where, Chef moves either `right` or `down` by $1$ cell each time.

For a particular grid, Chef defines the *score* of the grid as the number of *valid* paths containing **equal** number of `RED` and `GREEN` cells.

Find the **sum** of *scores* of all possible colored grids containing $N$ rows and $M$ columns.
Since the answer can be large, output it modulo $998244353$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $N$ and $M$ - denoting the dimensions of the grid.

**Output**

For each test case, output the **sum** of *scores* of all possible colored grids containing $N$ rows and $M$ columns, modulo $998244353$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, M \leq 1000$

## Sample

**Sample input**

```
3
1 1
1 2
2 3
```

**Sample output**

```
0
2
72
```

<details><summary>Explanation</summary>

**Test case $1$:** There are $2$ possible coloured grids of size $1 \times 1$. In the first grid, the one and only cell is colored `RED`. In the second grid, the one and only cell is colored `GREEN`. Neither of the grids have a *valid* path with equal number of red and green cells. Thus, score of each grid is $0$.

**Test case $2$:** There are $4$ possible coloured grids of the given dimension:

<img src="https://s3.amazonaws.com/codechef_shared/download/Images/START60.png" width="500">

For grids $1$ and $4$, the scores are $0$ as there are no valid paths with equal red and green cells. Grids $2$ and $3$ have score $1$ each. The valid path with equal red and green cells is $(1,1) \rightarrow (1,2)$ in both the grids.

Thus, the sum of scores of all possible coloured grids is $2$.

</details>

## Approach

The sum of scores over all grids is the number of pairs (colouring, path) in which the path is balanced. Count it from the side of the paths.

There are $\binom{N + M - 2}{N - 1}$ monotone paths, and each visits exactly $L = N + M - 1$ cells. For a fixed path, the colourings in which it is balanced choose which $L / 2$ of its cells are red, $\binom{L}{L/2}$ ways, and colour the remaining $N M - L$ cells freely, $2^{N M - L}$ ways. The count is the same for every path, so

$$\text{answer} = \binom{N + M - 2}{N - 1} \cdot \binom{L}{L/2} \cdot 2^{N M - L}.$$

If $L$ is odd no path can be balanced and the answer is 0.

## Solution

```python
import sys


MOD = 998244353
fact = [1] * 200001
for i in range(1, 200001):
    fact[i] = fact[i - 1] * i % MOD
inv_fact = [1] * 200001
inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
for i in range(200000, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    mod = 998244353
    length = n + m - 1
    if length & 1:
        return '0'

    def comb(a, b):
        return fact[a] * inv_fact[b] % mod * inv_fact[a - b] % mod
    return str(comb(n + m - 2, n - 1) * comb(length, length // 2) % mod * pow(2, n * m - length, mod) % mod)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $N + M$ even means an odd path length: answer 0.
- A $1 \times M$ grid has a single path covering every cell.
- The exponent $N M - L$ can be about $10^6$; modular exponentiation handles it.
- The modulus here is $998244353$.

## Dry run

`2 x 3` grid: $L = 4$.

Paths: $\binom{3}{1} = 3$. Balanced colourings of one path: $\binom{4}{2} = 6$. Free cells: $6 - 4 = 2$, so $2^2 = 4$.

Answer $3 \cdot 6 \cdot 4 = 72$.

---

Same problem grouped by topic: [../docs/combinatorics/REDGREEN.md](../docs/combinatorics/REDGREEN.md)
