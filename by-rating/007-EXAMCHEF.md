[&larr; 006. Janmansh and Assignments](006-JASSIGNMENTS.md) &middot; [Index](README.md) &middot; [008. Chef And Operators &rarr;](008-CHOPRT.md)

# 007. Exams

> [`EXAMCHEF`](https://www.codechef.com/problems/EXAMCHEF) &middot; difficulty **519** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Percentage comparison without division |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

In Chefland, there are $X$ schools, and each school has $Y$ students.
The year end results are in and a total of $Z$ students passed the exams.

Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was **strictly greater** than $50\%$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $X, Y,$ and $Z$, as mentioned in the statement.

**Output**

For each test case, output on a new line, `YES`, if the total number of students who passed in Chefland was strictly greater than $50\%$, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 2\cdot 10^4$
- $1 \leq X \leq 5$
- $1 \leq Y \leq 50$
- $0 \leq Z \leq X\cdot Y$

## Sample

**Sample input**

```
4
2 10 12
2 10 3
1 5 3
3 6 9
```

**Sample output**

```
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** The total number of students appeared were $2\cdot 10 = 20$. The number of students passed were $12$.
Thus, number of students who passed are $60\%$, which is strictly greater than $50\%$.

**Test case $2$:** The total number of students appeared were $2\cdot 10 = 20$. The number of students passed were $3$.
Thus, number of students who passed are $15\%$, which is less than $50\%$.

**Test case $3$:** The total number of students appeared were $1\cdot 5 = 5$. The number of students passed were $3$.
Thus, number of students who passed are $60\%$, which is strictly greater than $50\%$.

**Test case $4$:** The total number of students appeared were $3\cdot 6 = 18$. The number of students passed were $9$.
Thus, number of students who passed are $50\%$, which is equal to $50\%$.

</details>

## Approach

There are $X$ schools of $Y$ students each, so $X \cdot Y$ students sat the exams and $Z$ of them passed. The question is whether the pass rate exceeded $50\%$:

$$\frac{Z}{X \cdot Y} > \frac{1}{2}$$

Cross-multiplying by the positive quantity $2 \cdot X \cdot Y$ turns this into

$$2Z > X \cdot Y$$

which is again pure integer arithmetic. Dividing instead would introduce a float and, worse, invite a rounding mistake exactly at the halfway point that the problem cares most about.

The *strictly* greater wording matters. When $2Z = X \cdot Y$ the pass rate is exactly $50\%$ and the answer is `NO`. Sample case 4 is built on this: $X=3, Y=6, Z=9$ gives $18$ students and $9$ passes, precisely half, so `NO`.

With $T$ up to $2 \cdot 10^4$ it is worth reading all input at once rather than calling `input()` per line; the arithmetic itself is free.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # z / (x * y) > 1 / 2  <=>  2 * z > x * y
        out.append("YES" if 2 * z > x * y else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Exactly half pass**, $2Z = XY$: the rate is $50\%$, not above it, so `NO`. Sample case 4 ($3 \times 6 = 18$ students, $9$ passes) is built on this.
- **$Z = 0$**: nobody passed, so `NO` for any $X, Y$.
- **$Z = XY$**: everybody passed, and $2XY > XY$ holds for all $X, Y \geq 1$, so `YES`.
- **Smallest school** ($X = Y = 1$): $Z = 0$ gives `NO` and $Z = 1$ gives `YES` — a single student is either all or nothing.
- $XY$ is at most $250$, so there is no overflow concern; the reason to multiply out is exactness at the halfway point, not range.

## Dry run

| $X$ | $Y$ | $Z$ | students $XY$ | $2Z$ | $2Z > XY$ | output |
|---:|---:|---:|---:|---:|:---:|---|
| 2 | 10 | 12 | 20 | 24 | yes | `YES` |
| 2 | 10 | 3 | 20 | 6 | no | `NO` |
| 1 | 5 | 3 | 5 | 6 | yes | `YES` |
| 3 | 6 | 9 | 18 | 18 | no | `NO` |

Row 3 shows an odd total handled exactly, and row 4 the $50\%$ tie failing.

---

Same problem grouped by topic: [../docs/basic-math/EXAMCHEF.md](../docs/basic-math/EXAMCHEF.md)
