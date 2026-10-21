# 316. Minimum Number of Pizzas

> [`MINPIZZAS`](https://www.codechef.com/problems/MINPIZZAS) &middot; difficulty **1532** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Smallest multiplier for divisibility |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log \min(N,K))$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is throwing a party for his $N$ friends. There is a pizza store nearby and he wants to buy pizza for his friends. Each pizza has exactly $K$ slices. Chef's friends get sad if one gets more slices than the other. Also, Chef gets sad if there are some pizza slices left. More formally, suppose Chef buys $P$ pizzas, then everyone is happy if and only if there is a way to distribute $K \cdot P$ slices between $N$ friends.

You need to find the minimum number of pizzas Chef has to buy to share all the slices among his friends so that none of his friends gets sad. Note that Chef hates pizza and doesn't take any slices.

**Input**

- First line of input contains $T$, the number of test cases. Then the test cases follow.
- Each test case contains two space-separated integers $N$ and $K$, where $N$ is the number of friends of chef and $K$ is the number of slices in a pizza.

**Output**

For each test case, print the minimum number of pizzas chef has to buy to share among his friends so that none of his friends gets sad.

## Constraints

- $1 \leq T \leq 2 \cdot 10^5$
- $1 \leq N, K \leq 10^9$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
3
2 2
2 3
4 2
```

**Sample output**

```
1
2
2
```

<details><summary>Explanation</summary>

- **Test case $1$:** One pizza has $2$ slices. And there are $2$ friends. So chef can just buy one pizza and give one slice to one friend and another slice to another friend.
- **Test case $2$:** One pizza has $3$ slices. And there are $2$ friends. So chef can't share one pizza without being left out with a slice. So he needs to buy at least $2$ pizzas. And if he buys $2$ pizzas, he can give $3$ slices to one friend and $3$ to another. So the minimum number of pizzas chef needs to buy is equal to $2$.
- **Test case $3$:** One pizza has $2$ slices. And there are $4$ friends. So chef can't share one pizza among the $4$ friends. So he needs to buy at least $2$ pizzas. And if he buys $2$ pizzas, he can give $1$ slice to each of his friends. So the minimum number of pizzas chef needs to buy is equal to $2$.

</details>

## Approach

Buying $P$ pizzas yields $KP$ slices, and sharing them equally among $N$ friends with none left over means

$$N \mid KP$$

So we need the smallest positive $P$ making $KP$ a multiple of $N$.

Write $g = \gcd(N, K)$. Then $K$ already supplies the factor $g$ of $N$, and what remains to be covered is $N/g$ — which shares no factor with $K/g$. So $P$ must be a multiple of $N/g$, and the smallest choice is

$$P = \frac{N}{\gcd(N, K)}$$

Framing it through the gcd is what makes this immediate; searching for the smallest $P$ directly would be hopeless with $N, K$ up to $10^9$.

Sample case 1 has $N = K = 2$: the gcd is $2$, so a single pizza's two slices split one apiece. Sample case 2 has $N = 2, K = 3$ with gcd $1$, so $P = 2$ — two pizzas give six slices, three each. Sample case 3 has $N = 4, K = 2$ with gcd $2$, giving $P = 2$ and one slice per friend.

Note the answer never exceeds $N$ and equals it exactly when $K$ and $N$ are coprime. It is also the reason $K > N$ does not automatically mean one pizza: with $N = 4$ and $K = 6$ the gcd is $2$, so two pizzas are still needed.

Both `math.gcd` and the division stay in integers, so there is nothing to watch numerically.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # K already supplies gcd(n, k) of the factor n, so P covers the rest.
        out.append(str(n // gcd(n, k)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The condition is $N \mid KP$**, so the smallest $P$ is $N / \gcd(N, K)$: the pizza size already supplies $\gcd(N,K)$ of the factor $N$, and $P$ must cover the rest.
- **$K$ a multiple of $N$** → one pizza suffices, which the first row shows with $N = K = 2$.
- **$N$ and $K$ coprime** → $P = N$, the worst case; the second row needs two pizzas for two friends with three slices each.
- **A partial overlap** (the third row, $N = 4$ and $K = 2$) needs $4/2 = 2$ pizzas.
- **$N = 1$** → one friend takes everything, and $\gcd(1, K) = 1$ gives $P = 1$.
- **Chef's own share is not counted** — only the $N$ friends — so there is no $N+1$ anywhere.
- **$N, K$ up to $10^9$ with $T$ up to $2 \cdot 10^5$**: one gcd per case, and no search over $P$.

## Dry run

| $N$ | $K$ | $\gcd(N,K)$ | $P = N/\gcd$ | slices $KP$ | each friend gets |
|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 2 | `1` | 2 | 1 |
| 2 | 3 | 1 | `2` | 6 | 3 |
| 4 | 2 | 2 | `2` | 4 | 1 |

---

Same problem grouped by topic: [../docs/number-theory/MINPIZZAS.md](../docs/number-theory/MINPIZZAS.md)
