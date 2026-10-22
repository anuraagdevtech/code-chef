[&larr; 15. Count the Notebooks](NOTEBOOK.md) &middot; [Index](../../README.md) &middot; [20. Monopoly &rarr;](MONOPOLY2.md)

# 16. Chef and Candies

> CodeChef problem code [`CHEFCAND`](https://www.codechef.com/problems/CHEFCAND) &middot; difficulty **570** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Clamping before a ceiling division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There are $N$ children and Chef wants to give them $1$ candy each. Chef already has $X$ candies with him. To buy the rest, he visits a candy shop. In the shop, packets containing **exactly** $4$ candies are available.

Determine the **minimum** number of candy packets Chef must buy so that he is able to give $1$ candy to each of the $N$ children.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two integers $N$ and $X$ — the number of children and the number of candies Chef already has.

**Output**

For each test case, output the **minimum** number of candy packets Chef must buy so that he is able to give $1$ candy to each of the $N$ children.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, X \leq 100$

## Sample

**Sample input**

```
4
20 12
10 100
10 9
20 9
```

**Sample output**

```
2
0
1
3
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef must buy $2$ more packets after which he will have $20$ candies which will be enough to distribute $1$ candy to each of the $20$ children.

**Test Case $2$:** Chef does not need to buy more packets since he already has $100$ candies which are enough to distribute $1$ candy to each of the $10$ children.

**Test Case $3$:** Chef must buy $1$ more packet after which he will have $13$ candies which will be enough to distribute $1$ candy to each of the $10$ children.

**Test Case $4$:** Chef must buy $3$ more packets after which he will have $21$ candies which will be enough to distribute $1$ candy to each of the $20$ children.

</details>

## Approach

Chef needs one candy per child, so he needs $N$ candies and already holds $X$. The shortfall is $N - X$, and packets contain exactly $4$ candies, so the number of packets is

$$\left\lceil \frac{N - X}{4} \right\rceil$$

The trap is that $X$ may **exceed** $N$ — Chef can already have more candies than children. Sample case 2 ($N = 10$, $X = 100$) is exactly that, and the answer must be $0$. A bare ceiling division would produce a negative number there, so the shortfall has to be clamped at zero first:

$$\text{need} = \max(0,\; N - X)$$

Only then is the ceiling applied, as `(need + 3) // 4`.

The clamp and the ceiling must happen in that order. Applying `(n - x + 3) // 4` directly looks like a shortcut but is wrong whenever $X > N$: with $N = 10, X = 100$ it gives $(-90 + 3) // 4 = -22$, because Python's `//` floors toward negative infinity rather than truncating toward zero. Guarding the subtraction is what keeps the identity valid.

Walking the samples: $20, 12$ needs $8$ candies and so $2$ packets; $10, 9$ needs $1$ candy, which still costs a whole packet; $20, 9$ needs $11$, giving $3$ packets with one candy spare.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Chef may already hold more candies than children, so clamp first.
        need = max(0, n - x)
        out.append(str((need + 3) // 4))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Chef already has enough** ($N = 10$ children, $X = 100$ candies): the shortfall is negative, so the answer is $0$ packets. **The clamp is essential** — without `max(0, ...)` the expression $(-90 + 3) // 4$ evaluates to $-22$ in Python, because floor division rounds negatives *down*, and the answer would be badly wrong rather than merely off by one.
- **Exactly enough** ($N = X$): shortfall $0$, so $0$ packets.
- **Shortfall not a multiple of $4$** ($N = 10$, $X = 9$: one candy short): one whole packet.
- **Shortfall an exact multiple** ($N = 20$, $X = 12$: eight short): two packets, and the $+3$ must not make it three.

## Dry run

| $N$ | $X$ | shortfall $N - X$ | clamped | $(\text{need}+3)//4$ | output |
|---:|---:|---:|---:|---:|---|
| 20 | 12 | 8 | 8 | 2 | `2` |
| 10 | 100 | $-90$ | 0 | 0 | `0` |
| 10 | 9 | 1 | 1 | 1 | `1` |
| 20 | 9 | 11 | 11 | 3 | `3` |

Row 2 is the one the clamp exists for.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#23 of 486): [../../by-rating/023-CHEFCAND.md](../../by-rating/023-CHEFCAND.md)
