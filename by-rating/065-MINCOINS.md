# 065. Minimum number of coins

> [`MINCOINS`](https://www.codechef.com/problems/MINCOINS) &middot; difficulty **711** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Largest denomination first |
| **CodeChef tags** | `Mathematics`, `Modular Arithmetic`, `Basic Math`, `Divisibility`, `Integer Division` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has infinite coins in denominations of rupees $5$ and rupees $10$.

Find the **minimum** number of coins Chef needs, to pay **exactly** $X$ rupees. If it is impossible to pay $X$ rupees in denominations of rupees $5$ and $10$ only, print $-1$.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single integer $X$.

**Output**

For each test case, print a single integer - the **minimum** number of coins Chef needs, to pay **exactly** $X$ rupees. If it is impossible to pay $X$ rupees in denominations of rupees $5$ and $10$ only, print $-1$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 1000$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints.

## Sample

**Sample input**

```
3
50
15
8
```

**Sample output**

```
5
2
-1
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef would require at least $5$ coins to pay $50$ rupees. All these coins would be of rupees $10$.

**Test Case $2$:** Chef would require at least $2$ coins to pay $15$ rupees. Out of these, $1$ coin would be of rupees $10$ and $1$ coin would be of rupees $5$.

**Test Case $3$:** Chef cannot pay exactly $8$ rupees in denominations of rupees $5$ and $10$ only.

</details>

## Approach

Only $5$- and $10$-rupee coins exist, so every payable amount is a multiple of $5$. If $X \bmod 5 \neq 0$ the amount is impossible and the answer is $-1$ — sample case 3 covers this with $X = 8$.

Once divisibility holds, minimising the coin count means preferring the larger denomination: a $10$ replaces two $5$s, halving the count. So take $\lfloor X/10 \rfloor$ tens and then, if $5$ rupees remain, a single five:

$$\left\lfloor \frac{X}{10} \right\rfloor + \begin{cases} 1 & X \bmod 10 = 5 \\ 0 & \text{otherwise} \end{cases}$$

The greedy is safe here because the denominations are **nested** — $10$ is an exact multiple of $5$ — so taking a large coin never strands the remainder in a worse state. That property is what licenses the greedy, and it is not universal: with denominations $\{1, 3, 4\}$, greedily paying $6$ takes $4+1+1$ (three coins) when $3+3$ (two) is better. The general case needs dynamic programming; this one does not.

After removing all the tens the remainder is either $0$ or $5$, never anything else, precisely because divisibility by $5$ was already established. That is why a single conditional suffices rather than a second division.

Sample case 2: $X = 15$ gives one ten and one five, so $2$ coins — fewer than the three fives that also sum correctly.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        if x % 5:
            out.append("-1")          # only multiples of 5 are payable
        else:
            # 10s are nested multiples of 5, so greedy is safe here.
            out.append(str(x // 10 + (1 if x % 10 else 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/MINCOINS.md](../docs/greedy/MINCOINS.md)
