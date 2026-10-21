# 777 &middot; Reach fast

> CodeChef problem code [`REACHFAST`](https://www.codechef.com/problems/REACHFAST) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division over a distance |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/REACHFAST.md](../docs/basic-math/REACHFAST.md)

## Question

Chef is standing at coordinate $A$ while Chefina is standing at coordinate $B$.

In one step, Chef can increase or decrease his coordinate by **at most** $K$.

Determine the **minimum** number of steps required by Chef to reach Chefina.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three integers $A, B,$ and $K$, the initial coordinate of Chef, the initial coordinate of Chefina and the maximum number of coordinates Chef can move in one step.

**Output**

For each test case, output the minimum number of steps required by Chef to reach Chefina.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B \leq 100$
- $1 \leq K \leq 100$

## Sample

**Sample input**

```
4
10 20 3
36 36 5
50 4 100
30 4 2
```

**Sample output**

```
4
0
1
13
```

<details><summary>Explanation</summary>

**Test case $1$:** In the first three steps, Chef increases his coordinate by $K = 3$. In the fourth step, Chef increases his coordinate by $1$ which is less than equal to $K$. It can be shown that this is the minimum number of steps required by Chef.

**Test case $2$:** Chef is already at the same coordinate as Chefina. Thus, he needs $0$ steps.

**Test case $3$:** Chef can use $1$ step to decrease his coordinate by $46$ which is less than $K = 100$ and reach Chefina.

**Test case $4$:** Chef can use $13$ steps to decrease his coordinate by $K = 2$ and reach the coordinate $30-13\cdot 2 = 4$.

</details>

## Approach

The gap to close is $|A - B|$, and a step covers **at most** $K$ units. Since Chef may step any distance up to $K$, the best strategy is full-length steps until the final one, which covers whatever remains:

$$\left\lceil \frac{|A - B|}{K} \right\rceil$$

The phrase "at most $K$" is what makes this a clean ceiling rather than something harder. If a step had to be *exactly* $K$, Chef could overshoot and the answer would involve parity and reachability. Being free to take a shorter final step means the remainder never costs more than one extra move.

Two guards are built in. The absolute value handles Chefina being to the left of Chef, as in sample case 4 where the walk goes from $30$ down to $4$. And a gap of zero yields zero steps — sample case 2, where they already share a coordinate — which the ceiling gives for free since $\lceil 0/K \rceil = 0$.

Sample case 3 is the overshoot-allowed case: a gap of $46$ with $K = 100$ takes a single step, because Chef may move *less* than the maximum.

In integers the ceiling is `(d + k - 1) // k`.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, k = map(int, data[1 + 3 * i:4 + 3 * i])
        d = abs(a - b)
        # Steps are "at most K", so the last one can be short.
        out.append(str((d + k - 1) // k))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
