[&larr; 673. Chef and Queries](673-CHEFQUE.md) &middot; [Index](README.md) &middot; [675. Chef and Subarray Queries &rarr;](675-CSUBQ.md)

# 674. Candies

> [`CANDIES3`](https://www.codechef.com/problems/CANDIES3) &middot; difficulty **2329** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Sum of floors as a harmonic sum over multiples |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Simple Algos`, `Frequency Arrays`, `Mathematics`, `Prefix Sum` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N + M \log M)$ per test case |
| **Space** | $O(M)$ |

## Question

Chef gave you an infinite number of candies to sell. There are $N$ customers, and the budget of the $i^{th}$ customer is $A_i$ rupees, where $1 \leq A_i \leq M$.

You have to choose a price $P$, to sell the candies, where $1 \leq P \leq M$.
The $i^{th}$ customer will buy **exactly** $\lfloor{\frac{A_i}{P}} \rfloor$ candies.
Chef informed you that, for each candy you sell, he will reward you with $C_P$ rupees, as a bonus. Find the **maximum** amount of bonus you can get.

Note:
- We are not interested in the profit from selling the candies (as it goes to Chef), but only the amount of bonus. Refer the samples and their explanations for better understanding.
- $\lfloor x \rfloor$ denotes the largest integer which is not greater than $x$. For example, $\lfloor 2.75 \rfloor = 2$ and $\lfloor 4 \rfloor = 4$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$, the number of customers and the upper limit on budget/price.
    - The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$, the budget of $i^{th}$ person.
    - The third line contains $M$ integers - $C_1, C_2, \ldots, C_M$, the bonus you get per candy, if you set the price as $i$.

**Output**

For each test case, output on a new line, the maximum amount of bonus you can get.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, M \leq 10^5$
- $1 \leq A_i \leq M$
- $1 \leq C_j \leq 10^6$
- The elements of array $C$ are not necessarily non-decreasing.
- The sum of $N$ and $M$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
2
5 6
3 1 4 1 5
1 4 5 5 8 99
1 2
1
4 1
```

**Sample output**

```
20
4
```

<details><summary>Explanation</summary>

**Test case $1$:**
- If we choose $P = 1$, the number of candies bought by each person is $[\lfloor{\frac{3}{1}} \rfloor, \lfloor{\frac{1}{1}} \rfloor, \lfloor{\frac{4}{1}} \rfloor, \lfloor{\frac{1}{1}} \rfloor, \lfloor{\frac{5}{1}} \rfloor]$. Thus, our bonus is $(3 + 1 + 4 + 1 + 5) \cdot 1 = 14$.
- If we choose $P = 2$, the number of candies bought by each person is $[\lfloor{\frac{3}{2}} \rfloor, \lfloor{\frac{1}{2}} \rfloor, \lfloor{\frac{4}{2}} \rfloor, \lfloor{\frac{1}{2}} \rfloor, \lfloor{\frac{5}{2}} \rfloor]$. Thus our bonus is $(1 + 0 + 2 + 0 + 2) \cdot 4 = 20$.
- If we choose $P = 3$, the number of candies bought by each person is $[\lfloor{\frac{3}{3}} \rfloor, \lfloor{\frac{1}{3}} \rfloor, \lfloor{\frac{4}{3}} \rfloor, \lfloor{\frac{1}{3}} \rfloor, \lfloor{\frac{5}{3}} \rfloor]$. Thus our bonus is $(1 + 0 + 1 + 0 + 1) \cdot 5 = 15$.
- If we choose $P = 4$, the number of candies bought by each person is $[\lfloor{\frac{3}{4}} \rfloor, \lfloor{\frac{1}{4}} \rfloor, \lfloor{\frac{4}{4}} \rfloor, \lfloor{\frac{1}{4}} \rfloor, \lfloor{\frac{5}{4}} \rfloor]$. Thus our bonus is $(0 + 0 + 1 + 0 + 1) \cdot5 = 10$.
- If we choose $P = 5$, the number of candies bought by each person is $[\lfloor{\frac{3}{5}} \rfloor, \lfloor{\frac{1}{5}} \rfloor, \lfloor{\frac{4}{5}} \rfloor, \lfloor{\frac{1}{5}} \rfloor, \lfloor{\frac{5}{5}} \rfloor]$. Thus our bonus is $(0 + 0 + 0 + 0 + 1) \cdot 8 = 8$.
- If we choose $P = 6$, the number of candies bought by each person is $[\lfloor{\frac{3}{6}} \rfloor, \lfloor{\frac{1}{6}} \rfloor, \lfloor{\frac{4}{6}} \rfloor, \lfloor{\frac{1}{6}} \rfloor, \lfloor{\frac{5}{6}} \rfloor]$. Thus our bonus is $(0 + 0 + 0 + 0 + 0) \cdot 99 = 0$.

Thus, the answer is $20$.

**Test case $2$:**
- If we choose $P = 1$, the number of candies bought by each person is $[\lfloor{\frac{1}{1}} \rfloor]$. Thus, our bonus is $1 \cdot 4 = 4$.
- If we choose $P = 2$, the number of candies bought by each person is $[\lfloor{\frac{1}{2}} \rfloor]$. Thus, our bonus is $0 \cdot 1 = 0$.

Thus, the answer is $4$.

</details>

## Approach

For a price $P$ the number of candies sold is $\sum_i \lfloor A_i / P \rfloor$. Rewrite one floor as a count of thresholds:

$$\Bigl\lfloor \frac{a}{P} \Bigr\rfloor = \#\{\, j \ge 1 : jP \le a \,\},$$

so the total is $\sum_{j \ge 1} \text{cnt}(jP)$, where $\text{cnt}(x)$ is the number of customers with budget at least $x$.

Build `at_least` as a suffix sum of the budget frequencies. Then the sales for price $P$ are the sum of `at_least` over the multiples of $P$ up to $M$, which takes $M / P$ steps; over all prices this is the harmonic sum $M (1 + 1/2 + \dots) = O(M \log M)$. Multiply by the bonus $C_P$ and keep the maximum.

## Solution

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    at_least = [0] * (m + 2)
    for _ in range(n):
        at_least[next(tokens)] += 1
    bonus = [next(tokens) for _ in range(m)]
    for i in range(m - 1, -1, -1):
        at_least[i] += at_least[i + 1]
    return str(max((bonus[price - 1] * sum((at_least[j] for j in range(price, m + 1, price))) for price in range(1, m + 1))))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- The bonuses are not monotone, so every price has to be evaluated.
- A price above every budget sells nothing.
- The bonus can reach $10^6 \cdot$ (number of candies), exceeding 32 bits.
- Only the bonus matters, not the revenue.

## Dry run

`A = [3, 1, 4, 1, 5]`, `C = [1, 4, 5, 5, 8, 99]`.

Customers with budget at least $x$, for $x = 1 \dots 6$: `5 3 3 2 1 0`.

- $P = 1$: $5 + 3 + 3 + 2 + 1 = 14$ candies, bonus 14.
- $P = 2$: multiples 2, 4, 6 give $3 + 2 + 0 = 5$ candies, bonus $5 \cdot 4 = 20$.
- $P = 3$: $3 + 0 = 3$ candies, bonus 15. $P = 4$: 10. $P = 5$: 8. $P = 6$: 0.

Answer 20.

---

Same problem grouped by topic: [../docs/number-theory/CANDIES3.md](../docs/number-theory/CANDIES3.md)
