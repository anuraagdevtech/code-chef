# 075. Cyclic Quadrilateral

> [`CYCLICQD`](https://www.codechef.com/problems/CYCLICQD) &middot; difficulty **735** &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Cyclic quadrilateral angle condition |
| **CodeChef tags** | `Algorithms`, `Implementation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given the sizes of angles of a simple quadrilateral (in degrees) $A$, $B$, $C$ and $D$, in some order along its perimeter. Determine whether the quadrilateral is cyclic.

Note: A quadrilateral is cyclic if and only if the sum of opposite angles is $180^{\circ}$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $A$, $B$, $C$ and $D$.

**Output**
Print a single line containing the string `"YES"` if the given quadrilateral is cyclic or `"NO"` if it is not (without quotes).

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \leq T \leq 10^4$
- $1 \leq A, B, C, D \leq 357$
- $A + B + C + D = 360$

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A, B, C, D \leq 357$
- $A + B + C + D = 360$

## Sample

**Sample input**

```
3
10 20 30 300
10 20 170 160
179 1 179 1
```

**Sample output**

```
NO
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:** The sum of two opposite angles $A + C = 10^{\circ} + 30^{\circ} \neq 180^{\circ}$.

**Example case 2:** The sum of two opposite angles $A + C = 10^{\circ} + 170^{\circ} = 180^{\circ}$ and $B + D = 20^{\circ} + 160^{\circ} = 180^{\circ}$.

**Example case 3:** The sum of two opposite angles $B + D = 1^{\circ} + 1^{\circ} \neq 180^{\circ}$.

</details>

## Approach

A quadrilateral is cyclic — its vertices lie on a common circle — exactly when each pair of **opposite** angles sums to $180°$. The angles arrive in order around the perimeter, so the opposite pairs are $(A, C)$ and $(B, D)$.

The useful observation is that checking one pair is enough. The constraints guarantee

$$A + B + C + D = 360$$

so if $A + C = 180$ then $B + D = 360 - 180 = 180$ automatically. The two conditions are equivalent, and testing `a + c == 180` settles it.

Adjacency is where this goes wrong. Pairing $(A, B)$ and $(C, D)$ — the values that sit next to each other in the input — tests something geometrically meaningless. Sample case 2 distinguishes the two readings: $10 + 170 = 180$ for the opposite pair gives `YES`, while the adjacent pair $10 + 20 = 30$ would give `NO`.

Sample case 3 is a good check that the angle sum alone is not sufficient: $179 + 1 + 179 + 1 = 360$, a perfectly valid quadrilateral, yet $A + C = 358$ and it is not cyclic.

Everything here is integer arithmetic on angles in whole degrees, so there is no tolerance to worry about and the equality test is exact.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # Angles come in perimeter order, so A and C are opposite.
        # The total is fixed at 360, so B + D = 180 follows automatically.
        out.append("YES" if a + c == 180 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/geometry/CYCLICQD.md](../docs/geometry/CYCLICQD.md)
