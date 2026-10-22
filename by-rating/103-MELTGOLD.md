[&larr; 102. Mileage matters](102-MILEAGE.md) &middot; [Index](README.md) &middot; [104. Circular Track &rarr;](104-LOOP.md)

# 103. Melt Gold

> [`MELTGOLD`](https://www.codechef.com/problems/MELTGOLD) &middot; difficulty **835** &middot; time limit **1.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Triangular numbers and their inverse |
| **CodeChef tags** | `Mathematics` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has an ore with melting point of $X$ degrees.
 Chef’s kiln has a initial temperature of $Y$ degrees. The temperature of the kiln increases by $i$ degrees after the $i^{th}$ minute.

Find the **minimum** time in minutes after which the ore starts melting.

Note:
- We are only concerned about the temperature at the end of each minute and not during a minute.
- The ore starts melting if the temperature of the kiln becomes greater than or equal to the melting point.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the melting point of the ore and the initial temperature of kiln.

**Output**

For each test case, output on a new line, the **minimum** time in minutes after which the ore starts melting.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq Y \lt X \leq 10^5$

## Sample

**Sample input**

```
3
3 2
5 3
10 5
```

**Sample output**

```
1
2
3
```

<details><summary>Explanation</summary>

**Test case $1$:** The initial temperature of the kiln is $2$ and the melting point of ore is $3$.
After first minute, the temperature of kiln increases by $1$.
Thus, after $1$ minute the temperature of kiln becomes $2+1=3$, which is equal to the melting point. Thus, the ore starts melting.

**Test case $2$:** The initial temperature of the kiln is $3$ and the melting point of ore is $5$.
After first minute, the temperature of kiln increases by $1$, and becomes $4$.
After second minute, the temperature of kiln increases by $2$, and becomes $6$.

Thus, after $2$ minutes the temperature of kiln becomes $6$, which is greater than the melting point. Thus, the ore starts melting.

**Test case $3$:** The initial temperature of the kiln is $5$ and the melting point of ore is $10$.
After first minute, the temperature of kiln increases by $1$, and becomes $6$.
After second minute, the temperature of kiln increases by $2$, and becomes $8$.
After third minute, the temperature of kiln increases by $3$, and becomes $11$.

Thus, after $3$ minutes the temperature of kiln becomes $11$, which is greater than the melting point. Thus, the ore starts melting.

</details>

## Approach

After $t$ minutes the kiln has gained $1 + 2 + \cdots + t$ degrees, which is the $t$-th **triangular number**:

$$\sum_{i=1}^{t} i = \frac{t(t+1)}{2}$$

So the temperature is $Y + \frac{t(t+1)}{2}$, and melting begins at the smallest $t$ with

$$\frac{t(t+1)}{2} \geq X - Y$$

Writing $d = X - Y$ (positive, since $Y < X$ is guaranteed), this is a quadratic in $t$. Solving $t^2 + t - 2d \geq 0$ gives

$$t \geq \frac{-1 + \sqrt{1 + 8d}}{2}$$

Rather than taking a float square root and rounding — where a value landing a hair under an exact root silently gives $t - 1$ — the code computes `math.isqrt(8 * d + 1)` for an exact integer root, derives a candidate, and nudges it up while it falls short. The correction loop runs at most once or twice, so the whole thing stays $O(1)$.

A plain loop adding $1, 2, 3, \ldots$ until the target is reached would also be fast enough here, since $t$ never exceeds about $450$ when $d \leq 10^5$. But with $T$ up to $10^5$ that is $10^7$ iterations in Python, which is the kind of thing that turns a correct solution into a timeout. The closed form avoids the question.

The note that only end-of-minute temperatures count is what makes this a discrete search over integers rather than a continuous one. Checking sample 3: $d = 5$, and the triangular numbers run $1, 3, 6$ — so $t = 3$ is the first to reach it.

## Solution

```python
import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        d = x - y
        # Smallest k with k(k+1)/2 >= d, from the quadratic root.
        k = (math.isqrt(8 * d + 1) - 1) // 2
        while k * (k + 1) // 2 < d:
            k += 1
        out.append(str(k))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The smallest gap** ($d = 1$): one step, since $1 \cdot 2/2 = 1$ already covers it.
- **$d$ exactly triangular** ($d = 3 \to k = 2$, $d = 6 \to k = 3$): the closed-form estimate lands exactly and the correction loop never fires.
- **The estimate can come out one too low**, which is why the `while` loop follows it: inverting $k(k+1)/2 \geq d$ through an integer square root is off by one near the boundary, and the loop repairs that without any floating point.
- **$Y < X$ is guaranteed**, so $d \geq 1$ and there is no zero case.
- **Largest gap** ($d \approx 10^5$): $k \approx 446$, so the loop runs at most a step or two.

## Dry run

| $X$ | $Y$ | gap $d$ | triangular numbers | smallest $k$ with $\frac{k(k+1)}{2} \geq d$ | output |
|---:|---:|---:|---|---:|---|
| 3 | 2 | 1 | $1, 3, 6, \ldots$ | 1 | `1` |
| 5 | 3 | 2 | $1, 3, 6, \ldots$ | 2 | `2` |
| 10 | 5 | 5 | $1, 3, 6, \ldots$ | 3 | `3` |

Row 3 needs $6 \geq 5$, so three steps rather than the two that $3$ would allow.

---

Same problem grouped by topic: [../docs/basic-math/MELTGOLD.md](../docs/basic-math/MELTGOLD.md)
