# 872 &middot; Group Assignment

> CodeChef problem code [`GROUPASSGN`](https://www.codechef.com/problems/GROUPASSGN) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Pairing by reflection |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Arithmetic` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/GROUPASSGN.md](../docs/basic-math/GROUPASSGN.md)

## Question

Chef's professor is planning to give his class a group assignment. There are $2N$ students in the class, with distinct roll numbers ranging from $1$ to $2N$. Chef's roll number is $X$.

The professor decided to create $N$ groups of $2$ students each. The groups were created as follows: the first group consists of roll numbers $1$ and $2N$, the second group of roll numbers $2$ and $2N - 1$, and so on, with the final group consisting of roll numbers $N$ and $N+1$.

Chef wonders who his partner will be. Can you help Chef by telling him the roll number of his partner?

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $N$ and $X$, denoting the number of groups that will be formed, and Chef's roll number.

**Output**

For each test case, output the roll number of the student that will be Chef's partner.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^8$
- $1 \leq X \leq 2N$

## Sample

**Sample input**

```
3
2 2
3 1
3 4
```

**Sample output**

```
3
6
3
```

<details><summary>Explanation</summary>

**Test case $1$**: The groups will be $\{(1, 4), (2, 3)\}$. Chef's roll number is $2$, so his partner's roll number will be $3$.

**Test case $2$**: The groups will be $\{(1, 6), (2, 5), (3, 4)\}$. Chef's roll number is $1$, so his partner's roll number will be $6$.

**Test case $3$**: The groups will be $\{(1, 6), (2, 5), (3, 4)\}$. Chef's roll number is $4$, so his partner's roll number will be $3$.

</details>

## Approach

The groups pair $1$ with $2N$, $2$ with $2N-1$, and so on. Every such pair sums to the same constant:

$$1 + 2N = 2 + (2N - 1) = \cdots = 2N + 1$$

So a student with roll number $X$ is partnered with

$$2N + 1 - X$$

Recognising the **constant sum** is what turns this from a case analysis into one subtraction. There is no need to work out which group $X$ falls into, nor whether $X$ sits in the first half or the second — the formula is symmetric and handles both. Sample case 2 has $X = 1$ in the first half giving $6$, and sample case 3 has $X = 4$ in the second half giving $3$; the same expression covers each.

This "reflect about the midpoint" pattern appears constantly: reversing an array maps index $i$ to $n - 1 - i$, and the arithmetic is identical once the indexing base is accounted for. Here the roll numbers start at $1$, which is why the constant is $2N + 1$ rather than $2N$.

A useful sanity check is that applying the formula twice returns the original roll number, as a pairing must — partnership is symmetric.

With $N$ up to $10^8$ there are up to $2 \times 10^8$ students, so constructing the groups explicitly is out of the question; the closed form is the only workable approach.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every pair sums to 2n + 1, so the partner is the reflection of x.
        out.append(str(2 * n + 1 - x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
