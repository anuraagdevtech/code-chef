# 157. Richie Rich

> CodeChef problem code [`CHFRICH`](https://www.codechef.com/problems/CHFRICH) &middot; difficulty **878** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Exact division from a guaranteed divisor |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef aims to be the richest person in Chefland by his new restaurant franchise. Currently, his assets are worth $A$ billion dollars and have no liabilities. He aims to increase his assets by $X$ billion dollars per year.

Also, all the richest people in Chefland are not planning to grow and maintain their current worth.

To be the richest person in Chefland, he needs to be worth at least $B$ billion dollars. How many years will it take Chef to reach his goal if his value increases by $X$ billion dollars each year?

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, three integers $A$, $B$, $X$.

### Output
For each test case, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 21\ 000$
- $100 \leq A < B \leq 200$
- $1 \leq X \leq 50$
- $X$ divides $B - A$

### Subtasks
**Subtask #1 (100 points):** Original constraints

## Constraints

- $1 \leq T \leq 21\ 000$
- $100 \leq A < B \leq 200$
- $1 \leq X \leq 50$
- $X$ divides $B - A$

## Sample

**Sample input**

```
3
100 200 10
111 199 11
190 200 10
```

**Sample output**

```
10
8
1
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef needs to increase his worth by $200 - 100 = 100$ billion dollars and his increment per year being $10$ billion dollars, so it will take him $\frac{100}{10} = 10$ years to do so.

**Test Case $2$:** Chef needs to increase his worth by $199 - 111 = 88$ billion dollars and his increment per year being $11$ billion dollars, so it will take him $\frac{88}{11} = 8$ years to do so.

**Test Case $3$:** Chef needs to increase his worth by $200 - 190 = 10$ billion dollars and his increment per year being $10$ billion dollars, so it will take him $\frac{10}{10} = 1$ year to do so.

</details>

## Approach

Chef starts at $A$ billion and gains $X$ billion per year, needing to reach $B$. The shortfall is $B - A$, so the time required is

$$\frac{B - A}{X}$$

The constraints do two kind things here. $A < B$ guarantees the gap is strictly positive, so no clamping is needed and the answer is at least $1$. And **$X$ divides $B - A$**, which makes the division exact — no ceiling, no rounding rule.

That second guarantee is worth noticing rather than assuming. Without it the answer would be $\lceil (B-A)/X \rceil$, since a partial year still counts as a year in which the target is reached. Problems in this set go both ways, and the constraint block is where the setter tells you which.

The statement's remark that the current richest are not growing is there to rule out a moving target — Chef's goal $B$ is fixed, so this is a simple division rather than a pursuit problem.

Sample case 2 is the one that exercises the division: a gap of $88$ at $11$ per year gives exactly $8$. Case 3 is the one-year case, and case 1 the round $100/10$.

With $T$ up to $21{,}000$, reading the whole input at once and writing one joined block matters more than the arithmetic.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x = map(int, data[1 + 3 * i:4 + 3 * i])
        # x is guaranteed to divide b - a, so this is exact.
        out.append(str((b - a) // x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
