# 125. Chef and Profits

> CodeChef problem code [`CHFPROFIT`](https://www.codechef.com/problems/CHFPROFIT) &middot; difficulty **889** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Factoring a repeated difference |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Some time ago, Chef bought $X$ stocks at the cost of Rs. $Y$ each. Today, Chef is going to sell **all** these $X$ stocks at Rs. $Z$ each. What is Chef's total profit after he sells them?

Chef's profit equals the total amount he received by selling the stocks, minus the total amount he spent buying them.

**Input**

- The first line of input contains an integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $X, Y$ and $Z$ — the number of stocks, the price they were bought at, and the price they can be sold at, respectively.

**Output**

For each test case print on a new line a single integer — Chef's profit after selling all the stocks he has.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 10^4$
- $Y \leq Z \leq 10^4$

## Sample

**Sample input**

```
3
2 5 20
3 1 2
4 5 6
```

**Sample output**

```
30
3
4
```

<details><summary>Explanation</summary>

**Test Case 1:** Chef bought $X = 2$ stocks for $Y = 5$ each, making the total amount **spent** by Chef $ = 2 \cdot 5 = 10$.

Chef can sell this stock today for $Z = 20$, making the total amount **received** by Chef $ =  2 \cdot 20 = 40$.

The total **profit** is then the amount **received** minus the amount **spent**, which equals $40 - 10 = 30$.

**Test Case 2:** Chef bought $X = 3$ stocks for $Y = 1$ each, making the total amount **spent** by Chef $ = 3 \cdot 1 = 3$.

Chef can sell this stock today for $Z = 2$, making the total amount **received** by Chef $ =  3 \cdot 2 = 6$.

The total **profit** is then the amount **received** minus the amount **spent**, which equals $6 - 3 = 3$.

**Test Case 3:** Chef bought $X = 4$ stocks for $Y = 5$ each, making the total amount **spent** by Chef $ = 4 \cdot 5 = 20$.

Chef can sell this stock today for $Z = 6$, making the total amount **received** by Chef $ =  4 \cdot 6 = 24$.

The total **profit** is then the amount **received** minus the amount **spent**, which equals $24 - 20 = 4$

</details>

## Approach

Chef bought $X$ stocks at $Y$ each and sells all of them at $Z$ each, so

$$\text{profit} = XZ - XY = X(Z - Y)$$

Factoring out $X$ is the small simplification worth making: it computes the per-unit margin once and scales it, rather than forming two large products and subtracting. The two forms agree exactly in integer arithmetic, but the factored version makes the structure obvious — profit is margin times volume.

The constraints guarantee $Y \leq Z$, so the margin is never negative and the answer is never a loss. Without that promise the formula would still be correct, just capable of returning a negative number, and no clamping would be appropriate since a loss is a real outcome.

Sample case 1 is the large-margin case: $2$ stocks bought at $5$ and sold at $20$ gives $2 \times 15 = 30$. Cases 2 and 3 both have a margin of exactly $1$, so the profit is simply the share count.

On magnitudes: $X$ and $Z$ each reach $10^4$, so the product stays at $10^8$ — comfortably inside 32 bits, though worth noting for a C implementation that computes `x * z` before subtracting.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # Per-share margin times volume.
        out.append(str(x * (z - y)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
