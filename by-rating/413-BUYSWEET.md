# 413. Buying Sweets

> [`BUYSWEET`](https://www.codechef.com/problems/BUYSWEET) &middot; difficulty **1706** &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Batching purchases of the cheapest net-cost sweet |
| **CodeChef tags** | `math` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

There are $N$ sweets in the store. The cost of the $i^{th}$ sweet is $A_i$ rupees. Chef is a regular customer, so **after** buying the $i^{th}$ sweet, he gets a **cashback** of $B_i$ rupees.

Chef has $R$ rupees. He is fond of all the sweets, so he wants you to calculate the maximum number of sweets he can buy. Note that he can buy the same type of sweet multiple times, as long as he has the money to do so.

**Input**

- The first line of input will contain $T$, the number of test cases.
- Each test case consists of three lines of input.
- The first line of each test case contains two space-separated integers $N$ and $R$ — the number of sweets in the shop and the amount of money Chef has.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

**Output**

For each query, print on a new line the maximum number of sweets Chef can buy.

## Constraints

- $1 \le T \le 2 \cdot 10^5$
- $1 \le N \le 2 \cdot 10^5$
- $1 \le B_i < A_i \le 10^9$
- $1 \le R \leq 10^9$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
3
3 3
2 3 4
1 1 1
2 4
5 4
1 2
4 10
4 4 5 5
1 2 4 2
```

**Sample output**

```
2
1
7
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef buys the first sweet, which costs $2$ rupees and has a cashback of $1$ rupee. He now has $3 - 2 + 1 = 2$ rupees remaining. He once again buys the first sweet, which leaves him with $1$ rupee, at which point no more sweets can be bought.

**Test case $2$:** Chef buys the second sweet once.

</details>

## Approach

Each purchase of sweet $i$ needs $A_i$ in hand but burns only $A_i - B_i$ net. So two numbers matter per sweet: the **affordability** $A_i$ and the **burn rate** $n_i = A_i - B_i \geq 1$.

At any moment the affordable sweets are those with $A_i \leq R$, and among them the right choice is the smallest burn rate — buying a cheaper-to-burn sweet now never costs a purchase later. And crucially, once that sweet becomes unaffordable, the affordable set has shrunk, so the best available burn rate can only get **worse**. So the current best is worth exhausting completely before reconsidering.

Sort by $A$ and take prefix minima of $n$: the affordable set is a prefix, and its best burn rate and that sweet's price $a$ are then immediate. Buying it $k$ times keeps $R - (t-1)n \geq a$ through $t = k$, so

$$k = \left\lfloor \frac{R - a}{n} \right\rfloor + 1$$

After that batch $R < a$, so the prefix strictly shrinks and the loop runs at most $N$ times — a per-purchase simulation would run up to $R = 10^9$ times.

The third sample shows the batching and the switch. With $R = 10$ and prices $4,4,5,5$ at burn rates $3,2,1,3$, the best burn rate is $1$ (price $5$), bought six times down to $R = 4$. That price is now unaffordable, so the prefix drops to the two sweets priced $4$, whose best burn rate is $2$, giving one more purchase and $7$ in total.

Note the last purchase of a batch may leave less than its own price in hand — the cashback arrives after the sale, so only the *first* $A_i$ has to be covered up front.

## Solution

```python
import sys
from bisect import bisect_right


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, money = int(data[pos]), int(data[pos + 1])
        price = [int(x) for x in data[pos + 2:pos + 2 + n]]
        back = [int(x) for x in data[pos + 2 + n:pos + 2 + 2 * n]]
        pos += 2 + 2 * n
        order = sorted(range(n), key=price.__getitem__)
        prices = [price[i] for i in order]
        # Prefix minima of the burn rate, with the price that achieves it.
        best_burn, best_price = [], []
        burn = cheap = None
        for i in order:
            b = price[i] - back[i]
            if burn is None or b < burn:
                burn, cheap = b, price[i]
            best_burn.append(burn)
            best_price.append(cheap)

        bought = 0
        while True:
            j = bisect_right(prices, money) - 1
            if j < 0:
                break
            b, a = best_burn[j], best_price[j]
            k = (money - a) // b + 1
            bought += k
            money -= k * b          # now below a, so the prefix must shrink
        out.append(str(bought))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/BUYSWEET.md](../docs/greedy/BUYSWEET.md)
