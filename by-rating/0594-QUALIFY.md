# 594 &middot; Qualify the round

> CodeChef problem code [`QUALIFY`](https://www.codechef.com/problems/QUALIFY) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Weighted sum against a threshold |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Arithmetic` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/QUALIFY.md](../docs/basic-math/QUALIFY.md)

## Question

In a coding contest, there are two types of problems:

- Easy problems, which are worth $1$ point each
- Hard problems, which are worth $2$ points each

To qualify for the next round, a contestant must score at least $X$ points. Chef solved $A$ Easy problems and $B$ Hard problems. Will Chef qualify or not?

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing three space-separated integers — $X, A$, and $B$.

**Output**

For each test case, output a new line containing the answer — `Qualify` if Chef qualifies for the next round, and `NotQualify` otherwise.

Each character of the answer may be printed in either uppercase or lowercase. For example, if the answer is `Qualify`, outputs such as `qualify`, `quALiFy`, `QUALIFY` and `QuAlIfY` will also be accepted as correct.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
- $0 \leq A, B \leq 100$

## Sample

**Sample input**

```
3
15 9 3
5 3 0
6 2 8
```

**Sample output**

```
Qualify
NotQualify
Qualify
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef solved $9$ easy problems and $3$ hard problems, making his total score $9\cdot 1 + 3\cdot 2 = 15$. He needs at least $15$ points to qualify, which he has and hence he qualifies.

**Test Case $2$:** Chef solved $3$ easy problems and $0$ hard problems, making his total score $3\cdot 1 + 0\cdot 2 = 3$. He needs at least $5$ points to qualify, which he doesn't have and hence doesn't qualify.

**Test Case $3$:** Chef solved $2$ easy problems and $8$ hard problems, making his total score $2\cdot 1 + 8\cdot 2 = 18$. He needs at least $6$ points to qualify, which he has and hence he qualifies.

</details>

## Approach

Easy problems are worth $1$ point and hard ones $2$, so solving $A$ easy and $B$ hard problems scores

$$A + 2B$$

Chef qualifies when that total reaches the threshold $X$. Because the bar is "**at least** $X$ points", the comparison is `>=` and scoring exactly $X$ qualifies.

The only way to go wrong is to mix up which count carries the weight. The input order is $X, A, B$ — threshold first, then easy, then hard — which is deliberately not the order the quantities are introduced in the prose. Reading the three integers into the wrong names gives a plausible-looking program that fails immediately; sample case 3 ($X=6, A=2, B=8$) would score $2 + 16 = 18$ correctly but $8 + 4 = 12$ if $A$ and $B$ were swapped, and both pass the threshold, so the first sample is the one that actually exposes the error.

Note that $A$ and $B$ may be zero — Chef need not have attempted both kinds — so no positivity assumption is safe. Case 2 has $B = 0$ and falls short with $3 < 5$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # Input order is X, A, B: threshold first, then easy, then hard.
        x, a, b = map(int, data[1 + 3 * i:4 + 3 * i])
        out.append("Qualify" if a + 2 * b >= x else "NotQualify")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
