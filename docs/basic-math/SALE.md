[&larr; 81. Reach fast](REACHFAST.md) &middot; [Index](../../README.md) &middot; [85. Binary Battles &rarr;](BIN_BAT.md)

# 83. Get Lowest Free

> CodeChef problem code [`SALE`](https://www.codechef.com/problems/SALE) &middot; difficulty **778** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Total minus the extremum |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef goes to the supermarket to buy some items. Luckily there's a sale going on under which Chef gets the following offer:

- If Chef buys $3$ items then he gets the item (out of those $3$ items) having the lowest price as free.

For e.g. if Chef bought $3$ items with the cost $6$, $2$ and $4$, then he would get the item with cost $2$ as free. So he would only have to pay the cost of the other two items which will be $6 + 4 = 10$.

Chef buys $3$ items having prices $A$, $B$ and $C$ respectively. What is the amount of money Chef needs to pay?

**Input**

- The first line will contain an integer $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $A, B, C$ - the prices of the items bought by Chef.

**Output**

For each test case, output the price paid by Chef.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A, B, C \leq 10$

## Sample

**Sample input**

```
3
6 2 4
3 3 3
8 4 4
```

**Sample output**

```
10
6
12
```

<details><summary>Explanation</summary>

**Test case-1:** Explained in the problem statement.

**Test case-2:** Since all the three items have the same price, Chef will get one of them free and will have to pay the cost of the other two items which will be $3 + 3 = 6$.

**Test case-3:** Chef will get one of the items having price $4$ as free and will have to pay the cost of the other two items which will be $8 + 4 = 12$.

</details>

## Approach

Three items are bought and the cheapest is free, so Chef pays for the other two:

$$A + B + C - \min(A, B, C)$$

Expressing it as "total minus the minimum" rather than "sum of the two largest" is the move worth internalising. Both are correct, but the subtraction form needs only two passes over the values — one to add, one to find the minimum — and it extends unchanged to $n$ items with the cheapest free, whereas "add the two largest" would need a sort or a running top-two.

Ties are handled correctly without any special case. Sample case 2 has three items priced $3$; exactly one of them is free, so the answer is $6$ rather than $3$ or $9$. `min` returns the value, not every element equal to it, so only one copy is deducted. The same applies to sample case 3, where two items share the lowest price of $4$ and only one is discounted, giving $8 + 4 = 12$.

That subtlety — *one* free item, even when several are tied for cheapest — is where an approach built on filtering out the minimum value would go wrong, since it would remove both $4$s and answer $8$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        prices = list(map(int, data[1 + 3 * i:4 + 3 * i]))
        # Exactly one item is free, even if several tie for cheapest.
        out.append(str(sum(prices) - min(prices)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Several items tie for cheapest** ($3, 3, 3$ and $8, 4, 4$): **exactly one** item is free, so only a single minimum is subtracted. Removing every tied minimum would give $3$ and $8$ instead of $6$ and $12$, and both sample rows test this.
- **All three prices equal**: the answer is twice the price.
- **The cheapest item in any position** — first, middle or last — must be found, so a hard-coded position fails.
- The answer is the total minus one extremum, which is why no sorting is needed.

## Dry run

| prices | total | cheapest | total $-$ min | output |
|---|---:|---:|---:|---|
| $6, 2, 4$ | 12 | 2 | 10 | `10` |
| $3, 3, 3$ | 9 | 3 | 6 | `6` |
| $8, 4, 4$ | 16 | 4 | 12 | `12` |

Rows 2 and 3 have ties for cheapest, and only one copy is discounted.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#88 of 486): [../../by-rating/088-SALE.md](../../by-rating/088-SALE.md)
