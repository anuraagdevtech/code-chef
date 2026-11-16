[&larr; 581. Count palindromes](COUNTPAL.md) &middot; [Index](../../README.md) &middot; [585. Trip &rarr;](TRIP.md)

# 583. Pizza Delivery

> CodeChef problem code [`DBOY`](https://www.codechef.com/problems/DBOY) &middot; difficulty **1666** &middot; time limit **7s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Unbounded minimum-coin DP for each exact round trip |
| **Time** | $O(KU+N)$ per test case for $U=2\max H$ and $K$ distinct fuel amounts |
| **Space** | $O(U+N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef Po had recently started home delivery service for pizzas. Po has only a single delivery boy that delivers the orders by riding his motorcycle. The motorcycle has an unlimited capacity of fuel tank. However, it is too old and can only ride 1 km for each 1 liter of fuel.

There are $N$ fuel stations near the restaurant. The $i^{th}$ fuel station can fill a fuel tank exactly $K_{i}$ litres; not more and not less. Filling a fuel tank with any amount of fuel in those stations tends to take a long time. Since the fuel stations are placed near the restaurant, no fuel is needed to go to a fuel station.

Today Chef Po received $N$ pizza orders, which is the same number of fuel stations fortuitously. The house of the person that ordered the $i^{th}$ order is $H_{i}$ km away from the restaurant. The delivery boy cannot deliver more than one order at a time. Therefore, after delivering an order, he must return back to the restaurant to take the next order.

The delivery boy is an efficient person and thus he wants to fill the fuel tank with the exact amount of fuel required to deliver an order and return back. He also does not want to spends much time filling the tank, so he wants to minimize the number of times he fills the tank. Help him determine the minimum number of times he must fill the tank to deliver all orders.

**Input**

- The first line contains a single integer $T$ denoting the number test cases. The description of $T$ test cases follows.
- For each test case, the first line contains a single integer $N$.
- The second line contains $N$ space-separated integers $H_{i}$.
- The third line contains $N$ space-separated integers $K_{i}$.

**Output**

For each test case, output a single line containing the minimum number of times the delivery boy must fill the tank.

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N \leq 500$
- $1 \leq H_{i} \leq 500$
- $1 \leq K_{i} \leq 500$
- There is at least one way for completing the deliveries. That is, the delivery boy  always can fill a fuel tank exactly $2 * H_{i}$ litres for $1 \leq i \leq N.$

## Sample

**Sample input**

```
1
4
1 2 3 4
1 4 5 3
```

**Sample output**

```
7
```

<details><summary>Explanation</summary>

Here is one possible solution.

For the first order, the delivery boy must ride 1 + 1 = 2 km long. Fill the tank twice in the first fuel station.

For the second order, the delivery boy must ride 2 + 2 = 4 km long. Fill the tank once in the second fuel station.

For the third order, the delivery boy must ride 3 + 3 = 6 km long. Fill the tank twice in the fourth fuel station.

For the fourth order, the delivery boy must ride 4 + 4 = 8 km long. Fill the tank in the third and fourth fuel stations.

In total, the delivery boy must fill the tank 7 times. There is no way to fill the tank less than 7 times.

</details>

## Approach

A delivery to distance $H_i$ needs exactly $2H_i$ litres, and fuel cannot be shared between orders under the stated exact-trip policy. Each station is an unlimited coin denomination: using it fills exactly its offered amount once.

Compute the minimum number of fills for every fuel total up to the largest round-trip distance using unbounded coin-change DP. Process each distinct denomination with totals in ascending order, allowing repeated use. Sum the optimal fill counts for all orders.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        h = [int(next(tokens)) for _ in range(n)]
        coins = set(int(next(tokens)) for _ in range(n))
        limit = 2*max(h)
        dp = [limit+1]*(limit+1)
        dp[0] = 0
        for coin in coins:
            for total in range(coin,limit+1):
                dp[total] = min(dp[total],dp[total-coin]+1)
        out.append(str(sum(dp[2*v] for v in h)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(KU+N)$ per test case for $U=2\max H$ and $K$ distinct fuel amounts
- **Space:** $O(U+N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Use the round-trip distance, not the one-way distance.
- Duplicate station capacities do not create new options.
- An exact fill is required; overshooting is not allowed.
- The input guarantees each requested total is reachable.

## Dry run

For distances `[1,2,3,4]` and capacities `[1,4,5,3]`, round-trip totals `[2,4,6,8]` need `[2,1,2,2]` fills, summing to seven.

---

Same problem in rating order (#405 of 735): [../../by-rating/405-DBOY.md](../../by-rating/405-DBOY.md)
