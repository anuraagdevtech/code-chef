# 107. Summer Heat

> CodeChef problem code [`COCONUT`](https://www.codechef.com/problems/COCONUT) &middot; difficulty **852** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Independent requirements summed |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

**Read problem statements in [Vietnamese](https://www.codechef.com/download/translated/JUNE21/vietnamese/COCONUT.pdf),**
Chefland has $2$ different types of coconut, type $A$ and type $B$. Type $A$ contains only $x_a$ milliliters of coconut water and type $B$ contains only $x_b$ grams of coconut pulp. Chef's nutritionist has advised him to consume $X_a$ milliliters of coconut water and $X_b$ grams of coconut pulp every week in the summer. Find the total number of coconuts (type $A$ + type $B$) that Chef should buy each week to keep himself active in the hot weather.

**Input**

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, four integers $x_a$, $x_b$, $X_a$, $X_b$.

**Output**

For each test case, output in a single line the answer to the problem.

## Constraints

- $1 \leq T \leq 15000$
- $100 \leq x_a \leq 200$
- $400 \leq x_b \leq 500$
- $1000 \leq X_a \leq 1200$
- $1000 \leq X_b \leq 1500$
- $x_a$ divides $X_a$.
- $x_b$ divides $X_b$.

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
3
100 400 1000 1200
100 450 1000 1350
150 400 1200 1200
```

**Sample output**

```
13
13
11
```

<details><summary>Explanation</summary>

**TestCase $1$:**
Number of coconuts of Type $A$ required = $\frac{1000}{100} = 10$ and number of coconuts of Type $B$ required = $\frac{1200}{400} = 3$.  So the total number of coconuts required is $10 + 3 = 13$.

**TestCase $2$:**
Number of coconuts of Type $A$ required = $\frac{1000}{100} = 10$ and number of coconuts of Type $B$ required = $\frac{1350}{450} = 3$.  So the total number of coconuts required is $10 + 3 = 13$.

**TestCase $3$:**
Number of coconuts of Type $A$ required = $\frac{1200}{150} = 8$ and number of coconuts of Type $B$ required = $\frac{1200}{400} = 3$.  So the total number of coconuts required is $8 + 3 = 11$.

</details>

## Approach

Type A coconuts supply only water and type B supply only pulp, so the two requirements are completely **independent** — neither type can help with the other's quota. Chef needs

$$\frac{X_a}{x_a} + \frac{X_b}{x_b}$$

coconuts in total.

The constraints promise that $x_a$ divides $X_a$ and $x_b$ divides $X_b$, so both divisions are exact and no rounding question arises. That guarantee is doing real work: without it each term would need a ceiling, since a partial coconut cannot be bought, and the answer would be larger.

Because the two types are disjoint in what they provide, there is no optimisation to perform — no trade-off, no minimum to search for. Summing the two independently computed counts is the whole solution. This is the same "independent components" idea as the shoes problem, minus the clamping, because here neither side can overshoot and spill into the other.

Sample case 2 is a good check that the two divisions must be kept separate: $1000/100 = 10$ and $1350/450 = 3$, giving $13$. Mixing the quantities — dividing total volume by total capacity, say — would produce nonsense, because millilitres of water and grams of pulp are not the same unit.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        xa, xb, big_xa, big_xb = map(int, data[1 + 4 * i:5 + 4 * i])
        # Water and pulp come from different coconuts; both divisions are exact.
        out.append(str(big_xa // xa + big_xb // xb))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Basic Math`
