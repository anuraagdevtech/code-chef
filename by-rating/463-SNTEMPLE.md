[&larr; 462. Stacks](462-STACKS.md) &middot; [Index](README.md) &middot; [464. W String &rarr;](464-WSTRING.md)

# 463. A temple of Snakes

> [`SNTEMPLE`](https://www.codechef.com/problems/SNTEMPLE) &middot; difficulty **1800** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Runs computed from both directions |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(n)$ per test case |
| **Space** | $O(n)$ |

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

## Solution

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

## Edge cases

- **Blocks may only be reduced, never raised**, so the tallest slope ending at a block is capped by its own height — which is what the two running arrays compute, one from each side.
- **The peak of the temple is $\min(\text{left}, \text{right})$ at that block**, since both arms must fit; the best temple is the largest such value over all positions.
- **A temple of peak $x$ uses $x^2$ blocks** ($1 + 2 + \dots + x + \dots + 2 + 1$), so the removal count is the total height minus $x^2$.
- **Every block outside the temple must go entirely**, which is why the answer subtracts from the full sum rather than from a window.
- **A peak of $1$ is always available** (a single block reduced to height $1$), so the answer is well defined even on a flat range.
- **The first sample is already a temple**, so nothing is removed.
- **A tall isolated block is wasted**: the third sample's $6$ can only support a peak of $3$, because its neighbours cap the arms.
- **$h_i$ up to $10^9$ with $n$ up to $10^5$** makes the total reach $10^{14}$, past 32-bit.

## Dry run

Third sample: $h = 1, 2, 6, 2, 1$.

| block | left arm | right arm | possible peak |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | **3** |
| 4 | 2 | 2 | 2 |
| 5 | 1 | 1 | 1 |

Best peak is $3$, using $9$ blocks out of a total height of $12$ — so `3` blocks are removed.

---

Same problem grouped by topic: [../docs/arrays/SNTEMPLE.md](../docs/arrays/SNTEMPLE.md)
