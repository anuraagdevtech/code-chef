# 257. Counting Flags

> [`FLAGS`](https://www.codechef.com/problems/FLAGS) &middot; difficulty **1446** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Chromatic polynomials of small graphs |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Mike is a famous traveler. He visits about 100 countries a year and buys the flag of each country he has been to.

Mike knows, that there are some flags, that correspond to one pattern, but colored in different ways. E.g. the flag of Ireland([link](http://en.wikipedia.org/wiki/File:Flag_of_Ireland.svg)) and the flag of Belgium([link](http://en.wikipedia.org/wiki/File:Flag_of_Belgium.svg)). In this problem we consider only **five** 2,2cm✕1,1cm patterns of flags:

<img src="/download/extimages/e0a288110c029176f586f6eac23b4546.jpg" width="500" alt="e0a288110c029176f586f6eac23b4546.jpg" />

There are **N** different colors available to paint the flags and the colors are denoted by integers from 1 to **N**.

Mike wants you to count the number of different well-painted flags. We call a flag well-painted if it's made according to the following algorithm:

- Pick up one of the flag patterns considered above;

- Paint each one-colored polygon on the pattern in a color encoded by an integer from **1** to **N**. Different colors are encoded with different integers. If two different one-colored polygons share a common side(not corner), than they must be painted in different colors. In any other case they can be painted in both equal and different colors.

Two flags are different, if they look different(have at least one pixel painted with different color).

Help Mike!

**Text version of the pictures: **

**Picture 1**

112233

112233

112233

111111

222222

333333

112222

112222

113333

122223

111333

144443

111222

333222

333444

**Picture 2**

112211

112211

112211

221122

221122

221122

111111

222222

111111

222222

111111

222222

**Input**

The first line of the input contains integer **T**, denoting the number of testcases. The description of **T** testcases follows.

The only line of each test case contains integer **N**, denoting the number of different colors, that can be used while painting a flag pattern.

 

**Output**

For each testcase, output a single line containing an integer - the answer for the corresponding query.

 

**Constraints**

1 ≤ **T** ≤ 10 000;

1 ≤ **N** ≤ 10 000 for each testcase.

## Constraints

1 ≤ T ≤ 10 000;
1 ≤ N ≤ 10 000 for each testcase.

## Sample

**Sample input**

```
3
1
2
3
```

**Sample output**

```
0
4
42
```

<details><summary>Explanation</summary>

There are **four** different well-painted flags for **N** = 2 different colors :

<img src="/download/extimages/57c2f54761cda108c18bd840f4638fda.jpg" width="500" alt="57c2f54761cda108c18bd840f4638fda.jpg" />

</details>

## Approach

Each pattern is a map whose regions must be coloured so that regions **sharing an edge** differ. That is exactly proper graph colouring, so each pattern contributes its graph's **chromatic polynomial** evaluated at $N$, and the answer is the sum over the five patterns.

Reading the adjacency structure off the five patterns:

| Pattern | Region graph | Colourings |
|---|---|---|
| three vertical stripes | path $1{-}2{-}3$ | $N(N-1)^2$ |
| three horizontal stripes | path $1{-}2{-}3$ | $N(N-1)^2$ |
| L-shape split | triangle $K_3$ | $N(N-1)(N-2)$ |
| pinwheel of three | triangle $K_3$ | $N(N-1)(N-2)$ |
| four-region block | $K_4$ minus one edge | $N(N-1)(N-2)^2$ |

Summing gives

$$2N(N-1)^2 \;+\; 2N(N-1)(N-2) \;+\; N(N-1)(N-2)^2$$

The standard results behind the table: a **path** of $k$ vertices has $N(N-1)^{k-1}$ colourings, since each vertex after the first need only differ from its single predecessor; a **triangle** has $N(N-1)(N-2)$, all three being mutually adjacent; and $K_4$ minus an edge — two triangles sharing an edge — has $N(N-1)(N-2)^2$, because the shared edge takes $N(N-1)$ and each remaining vertex avoids both of its endpoints.

Checking against the samples confirms the reading. $N = 1$ gives $0$: with one colour, even a single shared edge is unsatisfiable. $N = 2$ gives $4$ — only the two striped patterns are two-colourable, at $2$ each, while the three patterns containing a triangle contribute nothing. $N = 3$ gives $12 + 12 + 6 + 6 + 6 = 42$.

Evaluating the polynomial is $O(1)$, which matters at $T = 10^4$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Two 3-stripe paths, two triangles, and one K4-minus-an-edge.
        total = (2 * n * (n - 1) ** 2
                 + 2 * n * (n - 1) * (n - 2)
                 + n * (n - 1) * (n - 2) ** 2)
        out.append(str(max(0, total)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$N = 1$ gives $0$**, since every one of the five patterns has at least two regions that touch and so needs at least two colours. The `max(0, …)` guard matters here because the $(n-2)$ factors turn negative at $n = 1$.
- **$N = 2$ gives $4$**: only the two three-stripe patterns are colourable, contributing $2 n (n-1)^2 = 4$, while the patterns needing three distinct colours contribute $0$ through their $(n-2)$ factors.
- **The three term shapes are chromatic counts of the five patterns**: two patterns count $n(n-1)^2$ each, two count $n(n-1)(n-2)$ each, and one counts $n(n-1)(n-2)^2$.
- **For $N \geq 2$ every term is non-negative**, so the clamp only ever fires on the single $N = 1$ case.
- **Adjacent regions must differ**, which is why consecutive factors drop by one; non-adjacent regions may repeat a colour, which is why the squared factors appear.
- **$N$ up to $10^4$** puts the total near $10^{16}$ — past 32-bit, and the cube is the dominant term.

## Dry run

| $N$ | $2n(n-1)^2$ | $2n(n-1)(n-2)$ | $n(n-1)(n-2)^2$ | total |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | `0` |
| 2 | 4 | 0 | 0 | `4` |
| 3 | 24 | 12 | 6 | `42` |

At $N = 2$ only the stripe patterns survive; the others need a third colour.

---

Same problem grouped by topic: [../docs/combinatorics/FLAGS.md](../docs/combinatorics/FLAGS.md)
