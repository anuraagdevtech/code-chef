# 143. Chef and Price Control

> [`PRICECON`](https://www.codechef.com/problems/PRICECON) &middot; difficulty **931** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Summing a clamped excess |
| **CodeChef tags** | `Algorithms`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has $N$ items in his shop (numbered $1$ through $N$); for each valid $i$, the price of the $i$-th item is $P_i$. Since Chef has very loyal customers, all $N$ items are guaranteed to be sold regardless of their price.

However, the government introduced a *price ceiling* $K$, which means that for each item $i$ such that $P_i \gt K$, its price should be reduced from $P_i$ to $K$.

Chef's *revenue* is the sum of prices of all the items he sells. Find the amount of revenue which Chef loses because of this price ceiling.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

**Output**
For each test case, print a single line containing one integer ― the amount of lost revenue.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $1 \le P_i \le 1,000$ for each valid $i$
- $1 \le K \le 1,000$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $1 \le P_i \le 1,000$ for each valid $i$
- $1 \le K \le 1,000$

## Sample

**Sample input**

```
3
5 4
10 2 3 4 5
7 15
1 2 3 4 5 6 7
5 5
10 9 8 7 6
```

**Sample output**

```
7
0
15
```

<details><summary>Explanation</summary>

**Test Case 1**: The initial revenue is $10 + 2 + 3 + 4 + 5 = 24$. Because of the price ceiling, $P_1$ decreases from $10$ to $4$ and $P_5$ decreases from $5$ to $4$. The revenue afterwards is $4 + 2 + 3 + 4 + 4 = 17$ and the lost revenue is $24 - 17 = 7$.

**Test Case 2**: The initial revenue is $1 + 2 + 3 + 4 + 5 + 6 + 7 = 28$. For each valid $i$, $P_i \le 15$, so there are no changes, the revenue after introduction of the price ceiling is the same and there is zero lost revenue.

**Test Case 3**: The initial revenue is $10 + 9 + 8 + 7 + 6 = 40$. Since $P_i \gt 5$ for each valid $i$, the prices of all items decrease to $5$. The revenue afterwards is $5 \cdot 5 = 25$ and the lost revenue is $40 - 25 = 15$.

</details>

## Approach

An item priced above the ceiling $K$ is sold at $K$ instead, losing $P_i - K$. An item already at or below $K$ is unaffected and loses nothing. So the total lost revenue is

$$\sum_{i=1}^{N} \max(0,\ P_i - K)$$

The clamp is what makes this one expression rather than a filter plus a sum. Items priced below the ceiling would otherwise contribute a **negative** loss, which would wrongly cancel out real losses from expensive items. Sample case 1 is built to catch exactly that: prices $[10, 2, 3, 4, 5]$ against $K = 4$ lose $6$ and $1$ for a total of $7$, whereas an unclamped sum would give $10 + 2 + 3 + 4 + 5 - 20 = 4$.

Sample case 2 has every price below the ceiling, so the answer is $0$ — a good check that the clamp never produces a negative total.

One pass with a running sum is enough; nothing needs sorting or storing. In Python the whole computation is a generator expression inside `sum`, which keeps it to $O(1)$ extra space even for $N = 10{,}000$.

Note that the ceiling only ever lowers a price — the government rule never raises a cheap item to $K$ — which is why the loss is one-sided and the clamp is at zero rather than symmetric.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        prices = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Cheap items lose nothing, so the excess must clamp at zero.
        out.append(str(sum(max(0, int(p) - k) for p in prices)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Every price below the cap** (the second row): the answer is $0$.
- **A price exactly at the cap**: contributes nothing, so the boundary is harmless either way.
- **The clamp is essential.** Without `max(0, ...)` the cheap items subtract: the first row would evaluate to $6 - 2 - 1 + 0 + 1 = 4$ instead of $7$. This is not an off-by-one but a wrong answer.
- **Every price above the cap** (the third row): all five items contribute, summing to $15$.
- **Largest inputs** ($N = 10^4$ with prices up to $1000$): the total stays under $10^7$.

## Dry run

First sample, cap $K = 4$:

| price | excess $\max(0, P-K)$ |
|---:|---:|
| 10 | 6 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 1 |

Total $7$, so the output is `7`. Note the $2$ and $3$ contribute zero rather than $-2$ and $-1$.

---

Same problem grouped by topic: [../docs/arrays/PRICECON.md](../docs/arrays/PRICECON.md)
