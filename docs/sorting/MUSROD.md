[&larr; 638. Symmetric Swaps](SYMARRSWAP.md) &middot; [Index](../../README.md) &middot; [687. Chef and Ants &rarr;](ANTSCHEF.md)

# 662. Musical Rods

> CodeChef problem code [`MUSROD`](https://www.codechef.com/problems/MUSROD) &middot; difficulty **2160** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Exchange argument - order rods by beauty per unit length |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You have $N$ rods with you. The $i$-th rod has a length of $A_i$ and a beauty of $B_i$.

You'd like to arrange these rods side-by-side in some order on the number line, starting from $0$.

Let $x_i$ be the starting position of the $i$-th rod in an arrangement. The beauty of this arrangement is
$$
\sum_{i=1}^N x_i\cdot B_i
$$

What is the maximum beauty you can attain?

Note that the left endpoint of the first rod you place **must** be $0$, and you cannot leave any space between rods.

**Input**

- The first line of input contains an integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$, the number of rods.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$
    - The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$

**Output**

- For each test case print on a new line the answer: the maximum value of $\sum_{i=1}^N x_i B_i$ if the order of rods is chosen optimally.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_{i} \leq 10^4$
- $1 \leq B_{i} \leq 10^4$
- The sum of $N$ across all testcases won't exceed $10^5$.

## Sample

**Sample input**

```
2
2
1 2
4 6
4
2 8 9 11
25 27 100 45
```

**Sample output**

```
8
2960
```

<details><summary>Explanation</summary>

**Test case $1$:** Place the second rod followed by the first one. This makes $x_2 = 0$ and $x_1 = 2$, giving us a beauty of $2\cdot 4 + 0\cdot 6 = 8$, which is the maximum possible.

**Test case $2$:** Place the rods in the order $[2, 4, 3, 1]$. This gives us $x = [28, 0, 19, 8]$, and the beauty is $28\cdot 25 + 0\cdot 27 + 19\cdot 100 + 8\cdot 45 = 2960$.

</details>

## Approach

Take two rods $x$ and $y$ that are adjacent in the arrangement. Swapping them does not move any other rod. If $x$ comes first, $y$ starts $A_x$ later than otherwise and the pair contributes an extra $A_x B_y$; if $y$ comes first the extra is $A_y B_x$. So $x$ should be before $y$ when

$$A_x B_y \ge A_y B_x \iff \frac{B_x}{A_x} \le \frac{B_y}{A_y}.$$

Sorting by increasing $B / A$ makes every adjacent pair optimal, and by the usual exchange argument the whole order is optimal: rods that are long and not very beautiful go first, pushing the valuable short ones to large coordinates. The comparison is done with integer cross products to avoid floating point, and the answer is accumulated in one pass.

## Solution (Python)

```python
import sys
from functools import cmp_to_key


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        lengths = [next(tokens) for _ in range(n)]
        beauties = [next(tokens) for _ in range(n)]
        rods = sorted(zip(lengths, beauties), key=cmp_to_key(lambda x, y: (x[1] * y[0] > y[1] * x[0]) - (x[1] * y[0] < y[1] * x[0])))
        position = total = 0
        for length, beauty in rods:
            total += position * beauty
            position += length
        out.append(str(total))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Equal ratios can be ordered either way without changing the total.
- A single rod starts at 0 and scores 0.
- Cross-multiplication keeps the comparison exact.
- The total can reach about $10^{17}$.

## Dry run

Rods (length, beauty): `(1, 4)` and `(2, 6)`. Ratios 4 and 3, so the rod `(2, 6)` goes first.

Positions: 0 for `(2, 6)`, 2 for `(1, 4)`. Beauty $0 \cdot 6 + 2 \cdot 4 = 8$.

The other order would give $1 \cdot 6 = 6$.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#622 of 735): [../../by-rating/622-MUSROD.md](../../by-rating/622-MUSROD.md)
