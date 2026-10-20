# 53. Valentine is Coming

> CodeChef problem code [`VALENTINE`](https://www.codechef.com/problems/VALENTINE) &middot; difficulty **691** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Floor division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.

Chef has a total of $X$ rupees and one chocolate costs $Y$ rupees. What is the **maximum** number of chocolates Chef can buy?

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $X, Y$ - the amount Chef has and the cost of one chocolate respectively.

**Output**

For each test case, output the **maximum** number of chocolates Chef can buy.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X,Y \leq 100$

## Sample

**Sample input**

```
4
5 10
16 5
35 7
100 1
```

**Sample output**

```
0
3
5
100
```

<details><summary>Explanation</summary>

**Test case-1:** Chef has $5$ rupees but the cost of one chocolate is $10$ rupees. Therefore Chef can not buy any chocolates.

**Test case-2:** Chef has $16$ rupees and the cost of one chocolate is $5$ rupees. Therefore Chef can buy at max $3$ chocolates since buying $4$ chocolates would cost $20$ rupees.

**Test case-3:** Chef has $35$ rupees and the cost of one chocolate is $7$ rupees. Therefore Chef can buy at max $5$ chocolates for $35$ rupees.

**Test case-4:** Chef has $100$ rupees and the cost of one chocolate is $1$ rupee. Therefore Chef can buy at max $100$ chocolates for $100$ rupees.

</details>

## Approach

Chef has $X$ rupees and each chocolate costs $Y$, so he can afford

$$\left\lfloor \frac{X}{Y} \right\rfloor$$

chocolates. Leftover change buys nothing, so the division rounds **down**.

This is the canonical "how many whole things fit in a fixed budget" question, and it is the floor counterpart to the ceiling problems elsewhere in this set. The distinguishing phrase is *maximum number obtainable from a fixed supply*, as against *minimum number of containers needed to hold everything*. One wastes the remainder; the other pays for it.

Python's `//` is floor division on non-negative integers, so `x // y` is the whole solution. Avoid `int(x / y)` — it routes through a float and begins to misreport once the operands exceed $2^{53}$, even though it happens to agree here.

Sample case 1 is the can't-afford-one case: $5$ rupees against a $10$-rupee chocolate gives $0$, not an error and not $1$. Case 4 is the other extreme, where a unit price of $1$ means the budget is spent exactly.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Change left over buys nothing, so round down.
        out.append(str(x // y))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
