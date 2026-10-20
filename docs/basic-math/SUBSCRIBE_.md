# 2. Subscriptions

> CodeChef problem code [`SUBSCRIBE_`](https://www.codechef.com/problems/SUBSCRIBE_) &middot; difficulty **504** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of $N$ friends in Chefland want to buy Chef-TV subscriptions. We know that $6$ people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is $X$ rupees.
Determine the minimum total cost that the group of $N$ friends will incur so that everyone in the group is able to use Chef-TV.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N$ and $X$ — the size of the group of friends and the cost of one subscription.

**Output**

For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Chef-TV.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \le X \le 1000$

## Sample

**Sample input**

```
3
1 100
12 250
16 135
```

**Sample output**

```
100
500
405
```

<details><summary>Explanation</summary>

- **Test case 1:** There is only one person in the group. Therefore he will have to buy $1$ subscription. Therefore the total cost incurred is $100$.
- **Test case 2:** There are $12$ people in the group. Therefore they will have to buy $2$ subscriptions. Therefore the total cost incurred is $500$.
- **Test case 3:** There are $16$ people in the group. Therefore they will have to buy $3$ subscriptions. Therefore the total cost incurred is $405$.

</details>

## Approach

One subscription covers $6$ people, so $N$ friends need $\lceil N/6 \rceil$ subscriptions — the leftover group of fewer than six people still needs a whole subscription of its own. The answer is that count multiplied by the unit price $X$.

The only real content here is computing the ceiling without touching floats. `math.ceil(n / 6)` works for these bounds but is the wrong reflex, because `n / 6` is a float and loses exactness once $N$ grows past $2^{53}$. The integer identity

$$\left\lceil \frac{n}{k} \right\rceil = \left\lfloor \frac{n + k - 1}{k} \right\rfloor$$

gives the same value using only `//`. In Python that is `(n + 5) // 6`, and it is exact for arbitrarily large integers.

Checking it against the samples: $N=1$ gives $(1+5)//6 = 1$ subscription, so $1 \times 100 = 100$. $N=12$ gives $(12+5)//6 = 2$, so $2 \times 250 = 500$. $N=16$ gives $(16+5)//6 = 3$, so $3 \times 135 = 405$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # ceil(n / 6) without floats: (n + 6 - 1) // 6
        out.append(str((n + 5) // 6 * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Algorithms`
