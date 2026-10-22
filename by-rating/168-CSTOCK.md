[&larr; 167. Devu and friendship testing](167-CFRTEST.md) &middot; [Index](README.md) &middot; [169. Motivation &rarr;](169-IMDB.md)

# 168. Chef and Stock Prices 

> [`CSTOCK`](https://www.codechef.com/problems/CSTOCK) &middot; difficulty **1069** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Percentage change without floating point |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef wants to buy a stock whose price was $S$ rupees when the market opened. He will buy the stock if and only if its price is in the range $[A, B]$. The price of the stock has changed by $C\%$ by the time he was trying to buy the stock. Will he be able to buy the stock?

**Input**

- First line of the input contains $T$, the number of testcases. Then the test cases follow.
- Each test case contains $4$ space-separated integers $S, A, B, C$ in a single line.

**Output**

For each test case, if Chef buys the stock print `YES`, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq S \leq 10^6$
- $0 \leq A \leq B \leq 10^6$
- $-100 \leq C \leq 100$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
100 93 108 7
100 94 100 -7
183 152 172 -17
```

**Sample output**

```
Yes
No
No
```

<details><summary>Explanation</summary>

- **Test Case $1$:** The price of the stock after gaining $7\%$ will become $107$, which is in Chef's range of $[93, 108]$. Hence, Chef will buy the stock.
- **Test Case $2$:** The price of the stock after falling $7\%$ will become $93$, which is not in Chef's range of $[94, 100]$. Hence, Chef will not buy the stock.
- **Test Case $3$:** The price of the stock after falling $17\%$ will become $151.89$, which is not in Chef's range of $[152, 172]$. Hence, Chef will not buy the stock.

</details>

## Approach

A change of $C\%$ takes the price from $S$ to

$$S \cdot \left(1 + \frac{C}{100}\right) = \frac{S(100 + C)}{100}$$

and Chef buys when that lands in $[A, B]$.

The right way to test this is to **avoid the division entirely**. Multiply the whole comparison through by $100$:

$$100A \leq S(100 + C) \leq 100B$$

Now everything is an integer and the test is exact. Computing the new price as a float and comparing is where this problem is lost: the result is frequently non-integral, and rounding it — in either direction — changes the answer at the boundaries.

Sample case 3 is built precisely on that. $183$ dropping $17\%$ gives $183 \times 83 = 15189$, against a lower bound of $152 \times 100 = 15200$. The true price is $151.89$, just **below** the range, so the answer is `No`. A solution that rounded to $152$ would answer `Yes`.

Note $C$ may be negative, which the formula handles naturally — $100 + C$ simply shrinks. Sample case 2 is a $7\%$ drop to exactly $93$, falling one rupee short of the range.

The range comparison is inclusive at both ends, and Python's chained comparison expresses it in one line.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s, a, b, c = map(int, data[1 + 4 * i:5 + 4 * i])
        # Scale the whole comparison by 100 so no division or float is needed.
        price100 = s * (100 + c)
        out.append("Yes" if 100 * a <= price100 <= 100 * b else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A negative change** (the last two rows): the price falls, and the formula handles it because $100 + C$ stays non-negative for $C \geq -100$. At $C = -100$ exactly the new price is $0$.
- **Scaling by $100$ removes the division entirely.** Computing $S(1 + C/100)$ as a float risks a rounding error at precisely the boundary cases the problem is built around; multiplying both sides by $100$ keeps everything in integers.
- **Exactly at $A$ or $B$**: inside the range, so the comparisons are non-strict.
- **$S = 0$**: the new price is $0$, and since $A$ may also be $0$ the answer can still be `Yes`.
- **$A \leq B$ is guaranteed**, so the range is never empty.

## Dry run

| $S$ | $C$ | $S(100+C)$ | $100A$ | $100B$ | inside? | output |
|---:|---:|---:|---:|---:|:---:|---|
| 100 | 7 | 10700 | 9300 | 10800 | yes | `Yes` |
| 100 | $-7$ | 9300 | 9400 | 10000 | no | `No` |
| 183 | $-17$ | 15189 | 15200 | 17200 | no | `No` |

Row 3 misses by $11$ hundredths of a rupee, which is exactly why the comparison must stay exact.

---

Same problem grouped by topic: [../docs/basic-math/CSTOCK.md](../docs/basic-math/CSTOCK.md)
