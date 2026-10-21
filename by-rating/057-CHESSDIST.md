# 057. Chessboard Distance

> [`CHESSDIST`](https://www.codechef.com/problems/CHESSDIST) &middot; difficulty **690** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Chebyshev distance |
| **CodeChef tags** | `Basic Programming Concepts`, `Conditional Statements`, `Inbuilt functions` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

The Chessboard Distance for any two points $(X_1, Y_1)$ and $(X_2, Y_2)$ on a Cartesian plane is defined as $max(|X_1 - X_2|, |Y_1 - Y_2|)$.

You are given two points $(X_1, Y_1)$ and $(X_2, Y_2)$. Output their Chessboard Distance.

Note that, $|P|$ denotes the absolute value of integer $P$. For example, $|-4| = 4$ and $|7| = 7$.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing $4$ space separated integers - $X_1, Y_1, X_2, Y_2$ - as defined in the problem statement.

**Output**

For each test case, output in a single line the chessboard distance between $(X_1, Y_1)$ and $(X_2, Y_2)$

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X_1, Y_1, X_2, Y_2 \leq 10^5$

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
3
2 4 5 1
5 5 5 3
1 4 3 3
```

**Sample output**

```
3
2
2
```

<details><summary>Explanation</summary>

- In the first case, the distance between $(2, 4)$ and $(5, 1)$ is $max(|2- 5|, |4 - 1|) = max(|-3|, |3|) = 3$.

- In the second case, the distance between $(5, 5)$ and $(5, 3)$ is $max(|5- 5|, |5 - 3|) = max(|0|, |2|) = 2$.

- In the third case, the distance between $(1, 4)$ and $(3, 3)$ is $max(|1- 3|, |4 - 3|) = max(|-2|, |1|) = 2$.

</details>

## Approach

The problem hands over the formula directly:

$$D = \max\left(|X_1 - X_2|,\; |Y_1 - Y_2|\right)$$

so the implementation is `max(abs(x1 - x2), abs(y1 - y2))`.

What is worth knowing is *why* this is called the chessboard distance. It counts the moves a **king** needs to travel between two squares. A king may step one square in any of eight directions, so it closes the horizontal and vertical gaps simultaneously whenever both are non-zero; the journey therefore costs only the larger of the two gaps, with the smaller one covered for free along the diagonal.

This metric, also called the Chebyshev or $L_\infty$ distance, sits alongside two neighbours worth contrasting:

- **Manhattan** ($L_1$): $|{\Delta x}| + |{\Delta y}|$ — a rook-like walk with no diagonals, so the gaps add.
- **Euclidean** ($L_2$): $\sqrt{\Delta x^2 + \Delta y^2}$ — straight-line distance.

The absolute values are essential and are the only place to slip. Sample case 3 has $\Delta x = 1 - 3 = -2$; without `abs`, the `max` would pick $\Delta y = 1$ and answer $1$ instead of $2$.

Sample case 2 shows the degenerate axis-aligned case: the points share an $x$, so the answer is purely the vertical gap.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x1, y1, x2, y2 = map(int, data[1 + 4 * i:5 + 4 * i])
        # King-move distance: the diagonal closes both gaps at once.
        out.append(str(max(abs(x1 - x2), abs(y1 - y2))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/geometry/CHESSDIST.md](../docs/geometry/CHESSDIST.md)
