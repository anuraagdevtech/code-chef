# 082. Presents for Cheffina

> [`PRESENTS`](https://www.codechef.com/problems/PRESENTS) &middot; difficulty **757** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting free items in a repeating group |
| **CodeChef tags** | `math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has fallen in love with Cheffina, and wants to buy $N$ gifts for her. On reaching the gift shop, Chef got to know the following two things:
- The cost of each gift is $1$ coin.
- On the purchase of every $4^{th}$ gift, Chef gets the $5^{th}$ gift free of cost.

What is the minimum number of coins that Chef will require in order to come out of the shop carrying $N$ gifts?

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$, the number of gifts in the shop.

**Output**

For each test case, output on a new line the minimum number of coins that Chef will require to obtain all $N$ gifts.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^9$

## Sample

**Sample input**

```
2
5
4
```

**Sample output**

```
4
4
```

<details><summary>Explanation</summary>

**Test case $1$**: After purchasing $4$ gifts, Chef will get the $5^{th}$ gift free of cost. Hence Chef only requires $4$ coins in order to get $5$ gifts.

**Test case $2$**: Chef will require $4$ coins in order to get $4$ gifts.

</details>

## Approach

Every fifth gift is free: Chef pays for four and the fifth comes at no cost, so the gifts arrive in repeating blocks of five costing four coins each.

Out of $N$ gifts, the number that are free is the number of complete blocks of five, $\lfloor N/5 \rfloor$, so the coins needed are

$$N - \left\lfloor \frac{N}{5} \right\rfloor$$

The two samples pin down the boundary. With $N = 5$ exactly one gift is free, so $5 - 1 = 4$ coins. With $N = 4$ no block is complete, so nothing is free and all $4$ are paid — the same answer by a different route, which is what makes this pair a good test: an off-by-one in the block count makes one of them wrong.

A tempting alternative is $4 \lceil N/5 \rceil$, reasoning that each started block costs four coins. That over-charges a partial block: for $N = 6$ it gives $8$ when the true cost is $6 - 1 = 5$, since Chef pays for the sixth gift but has not reached another free one. Counting the *free* items and subtracting is the formulation that handles partial blocks correctly.

With $N$ up to $10^9$, iterating over the gifts is out of the question — but the closed form is $O(1)$ and Python's integers handle the magnitude without comment.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # One gift is free per complete block of five.
        out.append(str(n - n // 5))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/PRESENTS.md](../docs/basic-math/PRESENTS.md)
