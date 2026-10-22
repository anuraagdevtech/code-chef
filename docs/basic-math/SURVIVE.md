[&larr; 390. Chef and Bulb Invention](CHFINVNT.md) &middot; [Index](../../README.md) &middot; [414. Three Numbers &rarr;](THREENUMBERS.md)

# 396. Survive in ChocoLand

> CodeChef problem code [`SURVIVE`](https://www.codechef.com/problems/SURVIVE) &middot; difficulty **1616** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Ceiling division with a running feasibility check |
| **Time** | $O(S)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are a poor person in ChocoLand. Here, people eat chocolates daily instead of normal food. There is only one shop near your home; this shop is closed on Sunday, but open on all other days of the week. You may buy **at most one** box of **N** chocolates from this shop on each day when it is open.

Currently, it's Monday, and you need to survive for the next **S** days (including the current day). You have to eat **K** chocolates everyday (including the current day) to survive. Do note that you are allowed to buy the a chocolate box and eat from it on the same day.

Compute the minimum number of days on which you need to buy from the shop so that you can survive the next **S** days, or determine that it isn't possible to survive.

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains 3 integers **N**, **K** and **S** denoting the number of chocolates in a box, the number of chocolates you have to eat everyday to survive and the number of days you need to survive.

**Output**

For each test case, print a single line containing one integer — the minimum number of days on which you need to buy from the shop to survive, or -1 if you will not be able to survive **S** days.

**Constraints**

- 1 ≤ **T** ≤ 100

- 1 ≤ **N** ≤ 100

- 1 ≤ **K** ≤ 100

- 1 ≤ **S** ≤ 1000

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 100
- 1 ≤ K ≤ 100
- 1 ≤ S ≤ 1000

## Sample

**Sample input**

```
2
16 2 10
50 48 7
```

**Sample output**

```
2
-1
```

<details><summary>Explanation</summary>

**Example case 1:** One possible solution is to buy a box on day 1 (Monday); it's sufficient to eat from this box up to day 8 (Monday) inclusive. Now, on day 9 (Tuesday), you buy another box and use the chocolates in it to survive days 9 and 10.

**Example case 2:** You will not be able to survive even if you buy from the shop everyday except every 7-th day.

</details>

## Approach

Two separate questions: *how few* purchases suffice, and *whether* any schedule works at all.

The count is pure arithmetic. Surviving $S$ days costs $SK$ chocolates and every purchase yields $N$, so

$$\text{purchases} = \left\lceil \frac{SK}{N} \right\rceil$$

and boxes keep, so leftovers carry forward and nothing is wasted beyond the final box.

Feasibility is the Sunday constraint. Day $1$ is Monday, so Sundays fall on days $7, 14, \ldots$, and by day $d$ the shop has been open on $d - \lfloor d/7 \rfloor$ days. Since you cannot eat what you have not bought, every prefix must balance:

$$\left(d - \left\lfloor \frac{d}{7} \right\rfloor\right) N \;\geq\; dK \qquad \text{for all } 1 \leq d \leq S$$

Checking only $d = S$ is not obviously enough, so with $S \leq 1000$ the honest thing is to check every prefix. (It happens that $\lfloor d/7 \rfloor / d$ peaks at $1/7$ on multiples of $7$, so for $S \geq 7$ the condition reduces to $6N \geq 7K$ — but the loop needs no such reasoning.)

Buying as early as possible is optimal and needs no scheduling logic: if the prefix condition holds everywhere, buying on the first $\lceil SK/N \rceil$ open days both meets the daily demand and uses the minimum number of purchases.

The samples sit on either side. With $N = 16$, $K = 2$, $S = 10$ the need is $20$ chocolates, so $2$ boxes, and supply never lags. With $N = 50$, $K = 48$, $S = 7$ the week has only $6$ open days, giving at most $300$ chocolates against a need of $336$ — the single Sunday is what makes it impossible, so $-1$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k, days = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        # You can never have eaten more than the open days so far supplied.
        ok = all((d - d // 7) * n >= d * k for d in range(1, days + 1))
        out.append(str(-(-days * k // n)) if ok else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(S)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Sundays make the supply uneven, so a total count is not enough.** By day $d$ only $d - \lfloor d/7 \rfloor$ open days have passed, capping the chocolates available at $(d - \lfloor d/7 \rfloor) N$ against the $dK$ eaten — and this must hold for *every* prefix, not just for $S$.
- **Checking only the final day is wrong**, because a shortfall can occur mid-way and be hidden by later open days. The feasibility test is a running one.
- **The count starts on Monday**, so the Sundays among the first $d$ days number exactly $\lfloor d/7 \rfloor$ — day $7$ is the first.
- **Buying and eating on the same day is allowed**, which is what makes day $1$ survivable whenever $N \geq K$.
- **The answer is $\lceil SK/N \rceil$** when feasible, computed as `-(-s * k // n)` to stay in exact integers.
- **The second sample fails on day $7$**: six open days supply $300$ chocolates against $336$ needed, so `-1` — even though days $1$ through $6$ are each fine.
- **$S \leq 1000$** makes the day-by-day check trivially cheap.

## Dry run

First sample: $N = 16$ per box, $K = 2$ per day, $S = 10$ days.

| day $d$ | open days so far | chocolates available | eaten by then | ok? |
|---:|---:|---:|---:|:---:|
| 1 | 1 | 16 | 2 | ✓ |
| 6 | 6 | 96 | 12 | ✓ |
| 7 | 6 | 96 | 14 | ✓ |
| 10 | 9 | 144 | 20 | ✓ |

Feasible, so the answer is $\lceil 10 \cdot 2 / 16 \rceil = $ `2` buying days.

> CodeChef tags: `Mathematics`, `Algorithms`

---

Same problem in rating order (#357 of 486): [../../by-rating/357-SURVIVE.md](../../by-rating/357-SURVIVE.md)
