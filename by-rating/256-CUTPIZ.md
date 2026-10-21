# 256. Cutting Pizza

> [`CUTPIZ`](https://www.codechef.com/problems/CUTPIZ) &middot; difficulty **1446** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | GCD of angular gaps |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Algorithms`, `Geometry`, `GCD`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(n + \log 360)$ per test case |
| **Space** | $O(1)$ |

## Question

Vasya has ordered a pizza delivery. The pizza can be considered a perfect circle. There were $n$ premade cuts in the pizza when it was delivered. Each cut is a straight segment connecting the center of the pizza with its boundary.

Let $O$ be the center of the pizza, $P_i$ be the endpoint of the $i$-th cut lying on the boundary, and $R$ be the point of the boundary straight to the right of $O$. Then the counterclockwise-measured angle $\angle ROP_i$ is equal to $a_i$ degrees, where $a_i$ is an integer between $0$ and $359$. Note that angles between $0$ and $180$ angles correspond to $P_i$ in the top half of the pizza, while angles between $180$ and $360$ angles correspond to the bottom half.

Vasya may cut his pizza a few more times, and the new cuts still have to be straight segments starting at the center. He wants to make the pizza separated into several equal slices, with each slice being a circular sector with no cuts inside of it. How many new cuts Vasya will have to make?

**Input:**
The first line of input contains $T$ , i.e number of test cases per file.

The first line of each test case contains a single integer $n-$  the numbers of premade cuts ($2 \leq n \leq 360$).

The second lines contains $n$ integers $a_1, \ldots, a_n-$ angles of the cuts $1, \ldots, n$ respectively ($0 \leq a_1 < \ldots, a_{n - 1} < 360$).

**Output:**
Print a single integer$-$ the smallest number of additional cuts Vasya has to make so that the pizza is divided into several equal slices.

**Constraints**
- $1  \leq T  \leq 36$
- $2 \leq n \leq 360$
- $0 \leq a_1 < \ldots, a_{n - 1} < 360$

## Constraints

- $1  \leq T  \leq 36$
- $2 \leq n \leq 360$
- $0 \leq a_1 < \ldots, a_{n - 1} < 360$

## Sample

**Sample input**

```
3
4 
0 90 180 270
2
90 210
2
0 1
```

**Sample output**

```
0
1
358
```

<details><summary>Explanation</summary>

In the first sample the pizza is already cut into four equal slices.

In the second sample the pizza will be cut into three equal slices after making one extra cut at $330$ degrees.

In the third sample Vasya will have to cut his pizza into $360$ pieces of $1$ degree angle each.

</details>

## Approach

Equal slices mean the final cuts sit at a fixed angular spacing $d$, at positions $a_0, a_0 + d, a_0 + 2d, \ldots$ all the way round. Two conditions follow: $d$ must divide $360$ so the cuts close up, and $d$ must divide every gap $a_i - a_0$ so the existing cuts land on the grid.

The **largest** such $d$ gives the fewest total cuts, and it is exactly

$$d = \gcd\bigl(360,\ a_1 - a_0,\ a_2 - a_0,\ \ldots,\ a_{n-1} - a_0\bigr)$$

The final pizza then has $360/d$ cuts, of which $n$ already exist, so the answer is

$$\frac{360}{d} - n$$

Including $360$ in the gcd is what ties the pattern to a full revolution — without it, a spacing that divides all the gaps but not $360$ would leave a ragged last slice.

Measuring gaps from a common reference $a_0$ rather than between consecutive cuts is equivalent, since the gcd of the differences is the same either way. Using $a_0$ keeps it to one pass.

Sample case 3 is the extreme: cuts at $0°$ and $1°$ force $d = \gcd(360, 1) = 1$, so the pizza must be sliced into $360$ one-degree wedges, needing $358$ more cuts. A single awkward cut can dominate the whole answer.

Sample case 2 has cuts at $90°$ and $210°$, a gap of $120$, so $d = 120$ and one more cut at $330°$ completes three equal thirds. Sample case 1 is already a perfect quartering.

Note the answer is never negative: $d$ divides every gap, so all $n$ distinct cuts lie on the grid of $360/d$ positions.

## Solution

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
        angles = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # 360 must be in the gcd so the pattern closes up over a full turn.
        d = 360
        base = angles[0]
        for a in angles[1:]:
            d = gcd(d, a - base)
        out.append(str(360 // d - n))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/number-theory/CUTPIZ.md](../docs/number-theory/CUTPIZ.md)
