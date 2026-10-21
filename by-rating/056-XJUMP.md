# 056. X Jumps

> [`XJUMP`](https://www.codechef.com/problems/XJUMP) &middot; difficulty **686** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Prefer the large step, then settle the remainder |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Loops`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is currently standing at stair $0$ and he wants to reach stair numbered $X$.

Chef can climb either $Y$ steps or $1$ step in one move.
Find the **minimum** number of moves required by him to reach **exactly** the stair numbered $X$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space separated integers $X$ and $Y$ denoting the number of stair Chef wants to reach and the number of stairs he can climb in one move.

**Output**

For each test case, output the **minimum** number of moves required by him to reach **exactly** the stair numbered $X$.

## Constraints

- $1 \leq T \leq 500$
- $1 \leq X, Y \leq 100$

## Sample

**Sample input**

```
4
4 2
8 3
3 4
2 1
```

**Sample output**

```
2
4
3
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can make $2$ moves and climb $2$ steps in each move to reach stair numbered $4$.

**Test case $2$:** Chef can make a minimum of $4$ moves. He can climb $3$ steps in $2$ of those moves and $1$ step each in remaining $2$ moves to reach stair numbered $8$.

**Test case $3$:** Chef can make $3$ moves and climb $1$ step in each move to reach stair numbered $3$.

**Test case $4$:** Chef can make $2$ moves and climb $1$ step in each move to reach stair numbered $2$.

</details>

## Approach

Chef can move $Y$ stairs or $1$ stair at a time and must land **exactly** on $X$. Since a $Y$-move covers $Y$ stairs for the same price as a $1$-move covers one, the greedy choice is to take as many $Y$-moves as possible and walk the rest:

$$\left\lfloor \frac{X}{Y} \right\rfloor + (X \bmod Y)$$

The greedy is provably optimal because the two move types are independent and unbounded: taking one fewer big jump forces $Y$ extra single steps, a strictly worse trade whenever $Y > 1$. There is no reason to stop short.

The remainder is where the "exactly" matters. Chef cannot overshoot and come back, so the last $X \bmod Y$ stairs must be covered one at a time. That is why the answer is a sum rather than a ceiling division — this is *not* $\lceil X/Y \rceil$.

The degenerate case $Y = 1$ falls out correctly without a guard: the formula gives $X + 0 = X$ single steps, which is right. And when $Y > X$, as in sample case 3, there are no big jumps at all and the answer is $X$ — $0 + 3 = 3$.

Sample case 2 shows both parts working: $8$ stairs with $Y = 3$ gives $2$ jumps covering $6$, then $2$ single steps, for $4$ moves.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # As many y-jumps as fit, then single steps for the remainder.
        out.append(str(x // y + x % y))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The long jump does not fit at all** ($X = 3$, $Y = 4$): no jump of length $Y$ is usable, so the answer is $X$ single steps. The sample's third row.
- **$Y = 1$**: the long jump *is* a single step, so both routes cost the same and the formula still gives $X$.
- **$Y$ divides $X$** ($X = 4$, $Y = 2$): no remainder, so only long jumps.
- Taking a long jump is never worse than $Y$ single steps whenever $Y \geq 1$, so the greedy needs no comparison — it is strictly better for $Y \geq 2$ and exactly equal at $Y = 1$.

## Dry run

| $X$ | $Y$ | long jumps $X // Y$ | steps $X \bmod Y$ | total | output |
|---:|---:|---:|---:|---:|---|
| 4 | 2 | 2 | 0 | 2 | `2` |
| 8 | 3 | 2 | 2 | 4 | `4` |
| 3 | 4 | 0 | 3 | 3 | `3` |
| 2 | 1 | 2 | 0 | 2 | `2` |

Row 3 never uses the long jump; row 4 is the case where both options coincide.

---

Same problem grouped by topic: [../docs/greedy/XJUMP.md](../docs/greedy/XJUMP.md)
