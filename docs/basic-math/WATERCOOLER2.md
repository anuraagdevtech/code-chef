# 91. The Cooler Dilemma 2

> CodeChef problem code [`WATERCOOLER2`](https://www.codechef.com/problems/WATERCOOLER2) &middot; difficulty **798** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Strict inequality turned into a floor |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:
- Rent a cooler at the cost of $X$ coins per month.
- Purchase a cooler for $Y$ coins.

Chef wonders what is the **maximum** number of months for which he can rent the cooler such that the cost of renting is **strictly less** than the cost of purchasing it.

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

**Output**

For each test case, output the **maximum** number of months for which he can rent the cooler such that the cost of renting is **strictly less** than the cost of purchasing it.

If Chef should not rent a cooler at all, output $0$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 10^9$

## Sample

**Sample input**

```
2
5 12
5 5
```

**Sample output**

```
2
0
```

<details><summary>Explanation</summary>

**Test case $1$**: Cost of renting the cooler $= 5$ coins per month. Cost of purchasing the cooler $= 12$ coins. So, Chef can rent the cooler for $2$ months at the cost of $10$ coins, which is **strictly less** than $12$ coins.

**Test case $2$**: Cost of renting the cooler $= 5$ coins per month. Cost of purchasing the cooler $= 5$ coins. If Chef rents the cooler for $1$ month, it will cost $5$ coins, which is **not strictly less** than the cost of purchasing it. So, Chef should not rent the cooler.

</details>

## Approach

Renting for $m$ months costs $mX$, and Chef wants that to stay **strictly** below the purchase price $Y$:

$$mX < Y$$

The largest integer $m$ satisfying a strict inequality is

$$m = \left\lceil \frac{Y}{X} \right\rceil - 1 = \left\lfloor \frac{Y - 1}{X} \right\rfloor$$

and the second form is the one to use — a single floor division, no ceiling helper needed.

The $-1$ inside the numerator is what encodes *strictly*. Plain $\lfloor Y/X \rfloor$ answers "how many months cost **at most** $Y$", which is off by one exactly when $X$ divides $Y$. Sample case 2 is that case: $X = Y = 5$ gives $\lfloor 5/5 \rfloor = 1$, but renting for one month costs exactly the purchase price and is not strictly cheaper, so the answer is $0$.

Sample case 1 confirms the non-dividing case: $Y = 12$ at $X = 5$ gives $\lfloor 11/5 \rfloor = 2$ months ($10 < 12$), while a third month would cost $15$ and lose.

The "output $0$ if Chef should not rent at all" instruction needs no separate branch — the formula already returns $0$ whenever $X \geq Y$, since $Y - 1 < X$ then.

With $X, Y$ up to $10^9$ the arithmetic stays well inside integer range, and Python has no limit regardless.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Largest m with m * x < y. The -1 is what makes it strict.
        out.append(str((y - 1) // x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Basic Math`
