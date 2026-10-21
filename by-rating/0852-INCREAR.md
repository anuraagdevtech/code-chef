# 852 &middot; Equal Integers

> CodeChef problem code [`INCREAR`](https://www.codechef.com/problems/INCREAR) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Asymmetric step sizes |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/INCREAR.md](../docs/basic-math/INCREAR.md)

## Question

Chef has two integers $X$ and $Y$. Chef wants to perform some operations to make $X$ and $Y$ equal. In one operation, Chef can either:
- set $X := X + 1$
- or set $Y := Y + 2$

Find the minimum number of operations required to make $X$ and $Y$ equal.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers $X$ and $Y$.

**Output**

For each test case, print the minimum number of operations required to make $X$ and $Y$ equal.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 10^9$

## Sample

**Sample input**

```
5
3 4
5 5
7 3
5 2
7 12
```

**Sample output**

```
1
0
2
3
5
```

<details><summary>Explanation</summary>

Let $(x, y)$ denote the values of $X$ and $Y$ respectively.

**Test case $1$:** Only one operation is required: $(3, 4) \xrightarrow{X := X + 1}{} (4, 4)$

**Test case $2$:** No operations are required since $X$ and $Y$ are already equal.

**Test case $3$:** Two operations are required: $(7, 3) \xrightarrow{Y := Y + 2}{} (7, 5) \xrightarrow{Y := Y + 2}{} (7, 7)$

**Test case $4$:** Three operations are required. One such sequence of operations is: $(5, 2) \xrightarrow{Y := Y + 2}{} (5, 4) \xrightarrow{X := X + 1}{} (6, 4) \xrightarrow{Y := Y + 2}{} (6, 6)$

</details>

## Approach

The two moves are not symmetric: $X$ grows by $1$, $Y$ grows by $2$, and neither can decrease. That asymmetry splits the problem into cases.

**$X \leq Y$.** Raising $Y$ only widens the gap, so the only sensible move is to raise $X$, one step at a time: $Y - X$ operations. Sample cases 1 and 5 are this shape.

**$X > Y$.** Now $Y$ must catch up across a gap $d = X - Y$, in steps of $2$. If $d$ is even that is $d/2$ moves and nothing else is needed — sample case 3, with $d = 4$ and answer $2$.

If $d$ is **odd**, steps of $2$ can never close an odd gap alone, so $X$ must be nudged too. Raising $Y$ by $2k$ and $X$ by $m$ requires $m = 2k - d$, with total cost $m + k = 3k - d$. Minimising means taking the smallest valid $k = \lceil d/2 \rceil = \frac{d+1}{2}$, giving

$$\frac{3(d+1)}{2} - d = \frac{d+3}{2}$$

Sample case 4 is exactly this: $d = 3$ costs $3$ moves — two steps of $+2$ on $Y$ and one $+1$ on $X$, meeting at $6$. The naive reading, $\lceil d/2 \rceil = 2$, is wrong, and that case is in the samples to catch it.

The parity of the gap is what this problem is really testing: a step of size $2$ preserves parity, so an odd difference cannot be closed without involving the step of size $1$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if x <= y:
            ops = y - x                  # only +1 on x can help
        else:
            d = x - y
            # +2 steps preserve parity, so an odd gap needs a +1 as well.
            ops = d // 2 if d % 2 == 0 else (d + 3) // 2
        out.append(str(ops))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
