# 330. A temple of Snakes

> CodeChef problem code [`SNTEMPLE`](https://www.codechef.com/problems/SNTEMPLE) &middot; difficulty **1800** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Runs computed from both directions |
| **Time** | $O(n)$ per test case |
| **Space** | $O(n)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

You want to build a temple for snakes. The temple will be built on a mountain range, which can be thought of as **n** blocks, where height of i-th block is given by **h**_i. The temple will be made on a consecutive section of the blocks and its height should start from 1 and increase by exactly 1 each time till some height and then decrease by exactly 1 each time to height 1,
i.e. a consecutive section of 1, 2, 3, .. x-1, x, x-1, x-2, .., 1 can correspond to a temple. Also, heights of all the blocks other than of the temple should have zero height, so that the temple is visible to people who view it from the left side or right side.

You want to construct a temple. For that, you can reduce the heights of some of the blocks. In a single operation, you can reduce the height of a block by 1 unit. Find out minimum number of operations required to build a temple.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains an integer **n**.

The next line contains **n** integers, where the i-th integer denotes **h**_i

**Output**

For each test case, output a new line with an integer corresponding to the answer of that testcase.

**Constraints**

- 1 ≤ **T** ≤ 10

- 2 ≤ **n** ≤ 10^5

- 1 ≤ **h**_i ≤ 10^9

## Constraints

- 1 ≤ T ≤ 10
- 2 ≤ n ≤ 10^5
- 1 ≤ h_i ≤ 10^9

## Sample

**Sample input**

```
3
3
1 2 1
4
1 1 2 1
5
1 2 6 2 1
```

**Sample output**

```
0
1
3
```

<details><summary>Explanation</summary>

**Example 1**. The entire mountain range is already a temple. So, there is no need to make any operation.

**Example 2**. If you reduce the height of the first block to 0. You get 0 1 2 1. The blocks 1, 2, 1 form a temple. So, the answer is 1.

**Example 3**. One possible temple can be 1 2 3 2 1. It requires 3 operations to build. This is the minimum amount you have to spend in order to build a temple.

</details>

## Approach

A temple with peak $x$ has heights $1, 2, \ldots, x-1, x, x-1, \ldots, 1$, which sum to

$$\underbrace{\frac{x(x-1)}{2}}_{\text{left}} + x + \underbrace{\frac{x(x-1)}{2}}_{\text{right}} = x^2$$

Everything else must be flattened to zero, and heights may only be **reduced**. So the total cost is $\sum h_i - x^2$, and minimising cost means **maximising the peak** $x$.

For a peak at index $i$, the left slope must descend $x-1, x-2, \ldots, 1$ and the right slope likewise. The tallest ascent that can end at $i$ is

$$\mathrm{left}[i] = \min\bigl(h_i,\ \mathrm{left}[i-1] + 1\bigr)$$

— capped by the block's own height, and by one more than whatever the previous block can support. The mirror recurrence going right-to-left gives $\mathrm{right}[i]$, and a peak at $i$ can reach

$$x_i = \min(\mathrm{left}[i], \mathrm{right}[i])$$

Taking the maximum over $i$ gives the best peak in two linear sweeps.

The `min` with $h_i$ is what encodes "reduce only" — a block can never be raised to support a taller slope.

Sample case 3, $[1,2,6,2,1]$, has a central block of height $6$, but its neighbours cap the slopes at $3$ on each side, so $x = 3$ and the cost is $12 - 9 = 3$ — the tall block is cut down to $3$. Sample case 2, $[1,1,2,1]$, supports $x = 2$ at index $2$, costing $5 - 4 = 1$: the leading block is flattened.

Sample case 1 is already a temple and costs nothing.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        h = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Tallest slope that can end here, capped by the block's own height
        # because blocks may only be reduced.
        left = [0] * n
        left[0] = min(h[0], 1)
        for i in range(1, n):
            left[i] = min(h[i], left[i - 1] + 1)
        right = [0] * n
        right[n - 1] = min(h[n - 1], 1)
        for i in range(n - 2, -1, -1):
            right[i] = min(h[i], right[i + 1] + 1)
        peak = max(min(left[i], right[i]) for i in range(n))
        out.append(str(sum(h) - peak * peak))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(n)$ per test case
- **Space:** $O(n)$
