# 283. Admins and Shopping

> CodeChef problem code [`ADMINSHOP`](https://www.codechef.com/problems/ADMINSHOP) &middot; difficulty **1529** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | The larger of two independent lower bounds |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

CodeChef admins went on shopping at a shopping mall.

There are $N$ shops in the mall where the $i^{th}$ shop has a capacity of $A_i$ people. In other words, at any point in time, there can be **at most** $A_i$ number of people in the $i^{th}$ shop.

There are $X$ admins. Each admin wants to visit each of the $N$ shops **exactly once**. It is known that an admin takes exactly **one** hour for shopping at any particular shop. Find the **minimum** time (in hours) in which all the admins can complete their shopping.

**Note:**
1. An admin can visit the shops in any order.
2. It is possible that at some point in time, an admin sits idle and does not visit any shop while others are shopping.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $X$ - the number of shops and the number of admins.
- The second line of each test case contains $N$ integers $A_1, A_2, \ldots, A_N$ - the capacity of the shops.

**Output**

For each test case, output in a single line the **minimum** time (in hours) in which all the admins can complete their shopping.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq X, A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
3
2 3
3 3
4 2
1 2 3 4
1 6
2
```

**Sample output**

```
2
4
3
```

<details><summary>Explanation</summary>

**Test case $1$:** Minimum time required to complete the shopping is two hours. A possible way to complete shopping in $2$ hours is :
- **$1^{st}$ hour:** All $3$ admins visit shop $1$. This is possible as the capacity of the shop is $3 \geq 3$.
- **$2^{nd}$ hour:** All $3$ admins visit shop $2$. This is possible as the capacity of the shop is $3 \geq 3$.

**Test case $2$:** Minimum time required to complete the shopping is $4$ hours. A possible way to complete shopping in $4$ hours is :
- **$1^{st}$ hour:** Admin $1$ visits shop $1$ and admin $2$ visits shop $4$.
- **$2^{nd}$ hour:** Admin $1$ visits shop $2$ and admin $2$ visits shop $3$.
- **$3^{rd}$ hour:** Admin $1$ visits shop $3$ and admin $2$ visits shop $2$.
- **$4^{th}$ hour:** Admin $1$ visits shop $4$ and admin $2$ visits shop $1$.

**Test case $3$:** Minimum time required to complete the shopping is $3$ hours. A possible way to complete shopping in $3$ hours is :
- **$1^{st}$ hour:** Admins $1$ and $2$ visits shop $1$. All other admins sit idle.
- **$2^{nd}$ hour:** Admins $3$ and $4$ visits shop $1$. All other admins sit idle.
- **$3^{rd}$ hour:** Admins $5$ and $6$ visits shop $1$. All other admins sit idle.
Note that, since the capacity of shop is $2$, maximum $2$ admins visit the shop at once.

</details>

## Approach

Two constraints act independently, and the answer is simply the larger.

**Each admin needs $N$ hours.** Every admin must visit all $N$ shops, one hour apiece, and cannot be in two shops at once. So no schedule finishes before hour $N$.

**Each shop needs $\lceil X / A_i \rceil$ hours.** Shop $i$ must serve all $X$ admins and holds at most $A_i$ at a time, so it needs that many hours of throughput. The binding shop is the tightest one.

Hence

$$\text{answer} = \max\left(N,\ \max_i \left\lceil \frac{X}{A_i} \right\rceil\right)$$

Both bounds are simultaneously achievable, which is the part worth believing. Admins can be staggered — think of a round-robin where admin $j$ starts at shop $(j \bmod N)$ and rotates — so each shop sees a steady, evenly spread stream and nobody collides. The freedom to idle, which the statement grants explicitly, is what lets a schedule absorb whichever bound is slack.

Sample case 2 is bound by the admin count: four shops means at least four hours, even though the tightest shop ($A = 1$ with $X = 2$) needs only two. Sample case 3 is the reverse: a single shop of capacity $2$ serving six admins takes three hours, far more than the $N = 1$ lower bound.

Sample case 1 has both bounds met at $2$ and $1$, giving $2$.

The ceiling is computed as `(x + a - 1) // a` to stay in integers at $X, A_i$ up to $10^9$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        # Each admin needs n hours; each shop needs ceil(x / a) hours.
        worst = max((x + int(v) - 1) // int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        out.append(str(max(n, worst)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Two independent lower bounds, and the answer is the larger.** Every admin must spend $N$ hours (one per shop), and every shop must absorb $X$ visits at $A_i$ at a time, needing $\lceil X / A_i \rceil$ hours. Both are achievable simultaneously, so the maximum of the two is exact.
- **Either bound can dominate.** The second row is limited by the shop count ($N = 4$ against a worst shop needing $2$), while the third is limited by a single tight shop ($N = 1$ against $\lceil 6/2 \rceil = 3$).
- **Only the tightest shop matters**, so the per-shop bound collapses to a maximum over $\lceil X / A_i \rceil$.
- **The ceiling must be integer**: `(x + a - 1) // a` rather than a float division, since $X$ and $A_i$ reach $10^9$ and a float divide can round the wrong way near an exact multiple.
- **$A_i \geq X$ makes a shop free** — its bound is $1$ — which the first row shows with capacity $3$ for $3$ admins.
- **Admins may visit shops in any order**, which is what makes the two bounds simultaneously satisfiable; a fixed order would be a scheduling problem instead.

## Dry run

| $N$ | $X$ | capacities | per-shop $\lceil X/A_i \rceil$ | worst | $\max(N, \text{worst})$ |
|---:|---:|---|---|---:|---:|
| 2 | 3 | $3, 3$ | $1, 1$ | 1 | `2` |
| 4 | 2 | $1,2,3,4$ | $2,1,1,1$ | 2 | `4` |
| 1 | 6 | $2$ | $3$ | 3 | `3` |

Row 3: one shop holding two at a time must serve six admins, so three hours even though each admin needs only one.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#313 of 486): [../../by-rating/313-ADMINSHOP.md](../../by-rating/313-ADMINSHOP.md)
