# 003. Subscriptions

> [`SUBSCRIBE_`](https://www.codechef.com/problems/SUBSCRIBE_) &middot; difficulty **504** &middot; complexity class **Constant time** $O(1)$

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Implementation` |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Problem

A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of $N$ friends in Chefland want to buy Chef-TV subscriptions. We know that $6$ people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is $X$ rupees.
Determine the minimum total cost that the group of $N$ friends will incur so that everyone in the group is able to use Chef-TV.

## Problem constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \le X \le 1000$

## Approach

One subscription covers $6$ people, so $N$ friends need $\lceil N/6 \rceil$ subscriptions — the leftover group of fewer than six people still needs a whole subscription of its own. The answer is that count multiplied by the unit price $X$.

The only real content here is computing the ceiling without touching floats. `math.ceil(n / 6)` works for these bounds but is the wrong reflex, because `n / 6` is a float and loses exactness once $N$ grows past $2^{53}$. The integer identity

$$\left\lceil \frac{n}{k} \right\rceil = \left\lfloor \frac{n + k - 1}{k} \right\rfloor$$

gives the same value using only `//`. In Python that is `(n + 5) // 6`, and it is exact for arbitrarily large integers.

Checking it against the samples: $N=1$ gives $(1+5)//6 = 1$ subscription, so $1 \times 100 = 100$. $N=12$ gives $(12+5)//6 = 2$, so $2 \times 250 = 500$. $N=16$ gives $(16+5)//6 = 3$, so $3 \times 135 = 405$.

## Solution

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

## Edge cases

- **$N = 1$**: one person still needs a whole subscription, so the cost is $X$, not $X/6$.
- **$N$ an exact multiple of $6$** ($N = 12$): no leftover group, so the $+5$ must not add a spurious subscription — $(12+5)//6 = 2$, not $3$.
- **$N = 6k + 1$** ($N = 13 \to 3$): the single extra person forces one more subscription, which is the whole point of the ceiling.
- **Largest input** ($N = 100$, $X = 1000$): $\lceil 100/6 \rceil = 17$ subscriptions for $17000$ — well inside integer range.

## Dry run

| $N$ | $X$ | $N + 5$ | $(N+5) // 6$ | cost | output |
|---:|---:|---:|---:|---:|---|
| 1 | 100 | 6 | 1 | $1 \times 100$ | `100` |
| 12 | 250 | 17 | 2 | $2 \times 250$ | `500` |
| 16 | 135 | 21 | 3 | $3 \times 135$ | `405` |

The middle row shows the exact-multiple case landing on $2$ rather than $3$.

---

Same problem grouped by topic: [../docs/basic-math/SUBSCRIBE_.md](../docs/basic-math/SUBSCRIBE_.md)
