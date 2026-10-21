# 947 &middot; Janmansh at Fruit Market

> CodeChef problem code [`JMARKET`](https://www.codechef.com/problems/JMARKET) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Cheapest choice under a diversity constraint |
| **CodeChef tags** | `Algorithms`, `Greedy` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/greedy/JMARKET.md](../docs/greedy/JMARKET.md)

## Question

Janmansh is at the fruit market to buy fruits for Chingari. There is an infinite supply of three different kinds of fruits with prices $A$, $B$ and $C$.

He needs to buy a total of $X$ fruits having at least $2$ different kinds of fruits. What is the least amount of money he can spend to buy fruits?

**Input**

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space separated integers $X$, $A$, $B$, $C$ - the number of fruits to buy and the prices of the three different types of fruits respectively.

**Output**

For each test case, output the least amount of money he can spend to buy fruits.

## Constraints

- $1 \le T \le 10^5$
- $2 \le X \le 1000$
- $1 \le A, B, C \le 100$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
2
2 1 1 1
3 4 3 2
```

**Sample output**

```
2
7
```

<details><summary>Explanation</summary>

**Test case-1:** He can buy any two fruits of different kinds for a total price of $2$.

**Test case-2:** He can buy $1$ fruit of price $3$ and $2$ fruits of price $2$ for a total price of $7$.

</details>

## Approach

Without the diversity rule, Janmansh would buy $X$ of the cheapest fruit. The rule forces **at least two different kinds**, so exactly one unit must be sacrificed to a second variety — and that sacrifice should be as cheap as possible.

Sort the three prices to get $a \leq b \leq c$. Buy $X - 1$ of the cheapest and $1$ of the second cheapest:

$$(X-1)\,a + b$$

Two greedy decisions sit behind this. First, the constraint is satisfied by exactly **two** kinds — bringing in a third would only replace a unit of $a$ with something at least as expensive, never cheaper. Second, among the non-cheapest options the second cheapest $b$ is the best filler, so the surcharge over the unconstrained cost is exactly $b - a$, the smallest possible.

The constraint $X \geq 2$ guarantees there are at least two fruits to buy, so $X - 1 \geq 1$ and the arrangement is always feasible.

Sample case 1 shows the surcharge vanishing when prices tie: all three fruits cost $1$, so $b - a = 0$ and the answer is simply $2$. A solution that always added a premium would get this wrong.

Sample case 2 sorts $[4,3,2]$ into $[2,3,4]$, giving $2 \cdot 2 + 3 = 7$ — two of the cheapest plus one of the next. Buying three of the cheapest would cost $6$ but is disallowed.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, a, b, c = map(int, data[1 + 4 * i:5 + 4 * i])
        lo, mid, _ = sorted((a, b, c))
        # Exactly one unit must be a second kind; make it the cheapest such.
        out.append(str((x - 1) * lo + mid))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
