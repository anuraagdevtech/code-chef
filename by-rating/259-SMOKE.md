# 259. Control the Pollution

> [`SMOKE`](https://www.codechef.com/problems/SMOKE) &middot; difficulty **1450** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Searching one variable over a small range |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Constructive`, `Basic Math`, `ad-hoc` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(N/100)$ per test case — at most 11 iterations |
| **Space** | $O(1)$ |

## Question

There are two types of vehicles in Chefland.
- **Bus** which has a capacity of $100$ people.
- **Car** which has a capacity of $4$ people.

There are $N$ people who want to travel from place $A$ to place $B$. You know that a single bus emits $X$ units of smoke while a single car emits $Y$ units of smoke in their journey from $A$ to $B$.

You want to arrange some buses and cars to carry all these $N$ people such that total smoke emitted is minimized. Output the minimized smoke value.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains three integers $N$, $X$, $Y$ - the number of people who want to travel, the units of smoke emitted by a bus and the units of smoke emitted by a car respectively.

**Output**

For each test case, output the minimum units of smoke emitted in transporting the $N$ people.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq X, Y \leq 1000$

## Sample

**Sample input**

```
3
9 40 8
15 20 20
105 80 10
```

**Sample output**

```
24
20
100
```

<details><summary>Explanation</summary>

**Test case-1:** In the optimal case, we will use $3$ cars where the $1$-st and $2$-nd car will carry $4$ people each and the $3$-rd car will carry $1$ person.

Therefore smoke emitted $= 3 \times 8 = 24$ units.

**Test case-2:** In the optimal case, we will use $1$ bus to carry all the $15$ people.

Therefore smoke emitted $= 1 \times 20 = 20$ units.

**Test case-3:** In the optimal case, we will use $1$ bus to carry $100$ people and use $2$ cars to carry the remaining $5$ people.

Therefore smoke emitted $= 1 \times 80 + 2 \times 10 = 100$ units.

</details>

## Approach

Two vehicle types with different capacities and different costs, so the cheaper **per person** is not always the right choice — the last vehicle is usually part-empty, and that waste can flip the comparison.

Since $N \leq 1000$, at most $\lceil N/100 \rceil \leq 10$ buses are ever useful. So fix the bus count $b$ from $0$ upward, carry the rest by car, and take the best:

$$\min_{0 \leq b \leq \lceil N/100 \rceil} \left( bX + \left\lceil \frac{\max(0,\ N - 100b)}{4} \right\rceil Y \right)$$

Eleven evaluations settle it, with no case analysis about which vehicle is better value.

The samples show all three regimes. Case 1 ($N=9$) uses cars only: three cars at $8$ beat one bus at $40$. Case 2 ($N=15$) uses a bus only: one bus at $20$ beats four cars at $20$ each. Case 3 ($N=105$) **mixes**: one bus plus two cars costs $80 + 20 = 100$, beating both two buses ($160$) and twenty-seven cars ($270$).

That mixed case is the reason to search rather than reason. A greedy "fill buses first, then cars" happens to be right here, but "pick whichever is cheaper per seat" is not — cars are cheaper per seat in case 3 ($2.5$ against $0.8$ per person for the bus), yet the answer still uses a bus.

The clamp at zero matters for the last bus, which may carry fewer than $100$ people; without it the car count would go negative.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, y = map(int, data[1 + 3 * i:4 + 3 * i])
        best = None
        # At most ceil(n / 100) buses are ever worth taking.
        for buses in range((n + 99) // 100 + 1):
            rest = max(0, n - 100 * buses)
            cost = buses * x + (rest + 3) // 4 * y
            if best is None or cost < best:
                best = cost
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Only the bus count needs searching.** Once it is fixed, the leftover people must all go by car, so the car count is forced at $\lceil \text{rest}/4 \rceil$ — one variable, not two.
- **The last bus may run under-filled.** The third row puts $100$ of $105$ people on one bus and the other five in two cars, which beats both all-car and two-bus options.
- **More than $\lceil N/100 \rceil$ buses can never help**, which bounds the loop at eleven iterations; `max(0, …)` keeps the remainder non-negative at that last step.
- **Cars round up too**: nine people need three cars, not two and a quarter.
- **Either mode can win outright** — the first row takes no buses at all, the second takes no cars.
- **$N, X, Y \leq 1000$** keeps every candidate cost small, so the brute force is comfortably within budget at $T = 1000$.

## Dry run

Third sample: $N = 105$, bus cost $X = 80$, car cost $Y = 10$.

| buses | carried by bus | rest | cars $\lceil \text{rest}/4 \rceil$ | cost |
|---:|---:|---:|---:|---:|
| 0 | 0 | 105 | 27 | 270 |
| 1 | 100 | 5 | 2 | **100** |
| 2 | 200 | 0 | 0 | 160 |

Output `100`.

---

Same problem grouped by topic: [../docs/brute-force/SMOKE.md](../docs/brute-force/SMOKE.md)
