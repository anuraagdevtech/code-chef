# 234. Maximize Colours

> [`COLOUR`](https://www.codechef.com/problems/COLOUR) &middot; difficulty **1415** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Enumerating a tiny decision space |
| **CodeChef tags** | `Special`, `Mathematics`, `Bit Manipulation`, `Case work`, `Bitmasking` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case — eight combinations |
| **Space** | $O(1)$ |

## Question

For the human eye, primary colours are red, green, and blue.

Combining $1$ drop each of **any two primary** colours produces a new type of secondary colour. For example, mixing red and green gives yellow, mixing green and blue gives cyan, and, mixing red and blue gives magenta.

You have $X, Y,$ and $Z$ drops of red, green, and blue colours respectively. Find the **maximum** total number of **distinct** colours (both primary and secondary) you can have at any particular moment.

**Note**: You **cannot** mix a secondary colour with a primary or another secondary colour to get a new type of colour.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space separated integers $X, Y, $ and $Z$, the number of drops of red, green, and blue colours respectively.

**Output**

For each test case, output on a new line the **maximum** total number of colours (both primary and secondary) you can have using the given primary colours.

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq X, Y, Z\leq 100$

## Sample

**Sample input**

```
4
1 0 1
3 3 0
1 1 1
0 0 0
```

**Sample output**

```
2
3
3
0
```

<details><summary>Explanation</summary>

**Test case $1$:** We have $1$ drop each of red and blue colour. If we mix these colours, we will have magenta but no red or blue. Thus, to maximize the total number of colours, it is better that we keep the red and blue colours as it is. The maximum number of colours we can have is $2$.

**Test case $2$:** We have $3$ drops each of red and green colour. We can use $1$ drop each of red and green to have yellow. We still have $2$ drops each of red and green left. Thus, we have $3$ different types of colours now.

**Test case $3$:** If we mix any two colours, we will loose two colours and get only one colour in return. Thus, it is best to keep all colours as it is and keep $3$ different varieties of colours.

**Test case $4$:** There are no types of colours available.

</details>

## Approach

There are exactly three secondary colours — yellow (red+green), cyan (green+blue), magenta (red+blue) — and making a second drop of one already-made secondary adds nothing, since only **distinct** colours are counted. So each secondary is a yes/no decision, giving $2^3 = 8$ combinations to try.

For a choice $(y, c, m) \in \{0,1\}^3$, the drops consumed are $y + m$ red, $y + c$ green, and $c + m$ blue. The total distinct colours is then

$$\underbrace{[\,X - (y{+}m) \geq 1\,] + [\,Y - (y{+}c) \geq 1\,] + [\,Z - (c{+}m) \geq 1\,]}_{\text{primaries still in hand}} \;+\; y + c + m$$

subject to every remainder being non-negative. Taking the maximum over the eight combinations answers it.

The tension is that a secondary **consumes** the primaries it is made from, so a colour can be lost to gain one. Sample case 3 is exactly that trade: with one drop each, keeping all three primaries scores $3$, while mixing any pair destroys two primaries to gain one secondary and scores only $2$.

Sample case 2 shows when the trade pays: three drops each of red and green leave plenty spare, so mixing one of each yields yellow *and* keeps both primaries, for $3$.

Sample case 1 is the opposite: one red and one blue can make magenta, but doing so consumes both, leaving a single colour instead of two.

Enumerating beats case analysis here — the interactions between the three decisions are fiddly, and eight evaluations cost nothing even at $T = 10^5$.

## Solution

```python
import sys
from itertools import product


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        best = 0
        # yellow = red + green, cyan = green + blue, magenta = red + blue
        for yel, cya, mag in product((0, 1), repeat=3):
            r, g, b = x - (yel + mag), y - (yel + cya), z - (cya + mag)
            if r < 0 or g < 0 or b < 0:
                continue
            # Primaries still in hand, plus the secondaries actually made.
            total = (r >= 1) + (g >= 1) + (b >= 1) + yel + cya + mag
            best = max(best, total)
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Making a secondary can lose you colours.** Each one consumes a unit of each of its two primaries, so with $1, 1, 1$ the best move is to make nothing and keep three distinct colours; mixing yellow drops red and green and leaves only two.
- **Leftover primaries count once each**, however many units remain — hence `(r >= 1)` rather than `r`. The second row keeps red and green with two units each and still scores them as one apiece.
- **All zeros** → $0$, with every combination either infeasible or empty.
- **At most one of each secondary is ever worth making**, because a second copy adds nothing to the distinct count while consuming more primaries — which is why the search is over $\{0,1\}^3$ and not over quantities.
- **Infeasible combinations must be rejected, not clamped.** A negative remainder means the primaries were over-spent, and treating it as zero would invent colours.
- **$X$, $Y$, $Z$ may be zero independently**, which rules out several secondaries at once — the first row has no green, so neither yellow nor cyan is possible.

## Dry run

Third sample: $X = Y = Z = 1$.

| yellow | cyan | magenta | red left | green left | blue left | feasible | distinct colours |
|:---:|:---:|:---:|---:|---:|---:|:---:|---:|
| 0 | 0 | 0 | 1 | 1 | 1 | yes | **3** |
| 1 | 0 | 0 | 0 | 0 | 1 | yes | 2 |
| 0 | 1 | 0 | 1 | 0 | 0 | yes | 2 |
| 0 | 0 | 1 | 0 | 1 | 0 | yes | 2 |
| 1 | 1 | 0 | 0 | $-1$ | — | no | — |

Output `3`: mixing anything here is a loss.

---

Same problem grouped by topic: [../docs/brute-force/COLOUR.md](../docs/brute-force/COLOUR.md)
