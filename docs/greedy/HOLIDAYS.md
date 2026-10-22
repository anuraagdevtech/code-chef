# 209. Lazy Salesman

> CodeChef problem code [`HOLIDAYS`](https://www.codechef.com/problems/HOLIDAYS) &middot; difficulty **1161** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Take the largest items first |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Ved is a salesman. He needs to earn at least $W$ rupees in $N$ days for his livelihood. However, on a given day $i$ ($1 \le i \le N$), he can only earn $A_i$ rupees by working on that day.

Ved, being a lazy salesman, wants to take as many holidays as possible. It is known that on a **holiday**, Ved does not work and thus does not earn anything. Help **maximize** the number of days on which Ved can take a holiday.

It is guaranteed that Ved can always earn at least $W$ rupees by working on all days.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $W$ - the size of the array $A$ and the money Ved has to earn in those $N$ days.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the money which Ved can earn on each day.

**Output**

For each test case, output the maximum number of holidays Ved can take.

## Constraints

- $1 \le T \le 100$
- $1 \le W \le 10000$
- $1 \le N \le 100$
- $1 \le A_i \le 100$
- It is guaranteed that Ved can always earn at least $W$ rupees by working on all days.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
5 10
3 2 6 1 3
4 15
3 2 4 6
6 8
9 12 6 5 2 2
```

**Sample output**

```
2
0
5
```

<details><summary>Explanation</summary>

**Test case-1:** Ved can work on $2$-nd, $3$-rd and $5$-th day earning $2 + 6 + 3 = 11$ rupees $\ge W$ rupees. Thus he can take $2$ holidays on the $1$-st and the $4$-th day.

**Test case-2:** Ved has to work on all days to earn $\ge W$ rupees. Thus he can not take any holidays.

**Test case-3:** Ved can work on $2$-nd day earning $12$ rupees $\ge W$ rupees. Thus he can take holiday on the remaining days.

</details>

## Approach

Maximising holidays is the same as **minimising days worked** while still earning $W$. Since Ved may work on any subset of days, he should work the most lucrative ones: sort the earnings descending and take them until the running total reaches $W$.

The greedy is optimal by an exchange argument. Suppose an optimal schedule of $m$ days omits one of the $m$ highest-earning days in favour of a lower one; swapping them keeps the day count the same and cannot lower the total. Repeating this turns any optimal schedule into the greedy one, so the greedy uses no more days than any alternative.

Holidays are then $N$ minus the days worked.

The guarantee that working every day earns at least $W$ means the loop always terminates with the target met, so no "impossible" case arises.

Sample case 3 is the striking one: a single day earning $12$ covers the $8$ required, so Ved rests for $5$ of $6$ days. Sorting matters here — taking days in input order would start with $9$, also enough, but on other inputs it would take more days than necessary.

Sample case 2 needs every day: the earnings sum to exactly $15 = W$, leaving zero holidays. That is the boundary where the `>=` comparison must be inclusive.

Sample case 1 takes $6 + 3 + 3 = 12 \geq 10$ in three days, leaving two holidays — note it stops as soon as the threshold is crossed rather than matching $W$ exactly.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, w = int(data[pos]), int(data[pos + 1])
        a = sorted((int(v) for v in data[pos + 2:pos + 2 + n]), reverse=True)
        pos += 2 + n
        earned = 0
        worked = 0
        # Work the best-paying days first to reach W in the fewest days.
        for v in a:
            if earned >= w:
                break
            earned += v
            worked += 1
        out.append(str(n - worked))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **One day suffices** (the third row: a single $12$ covers $W = 8$): five holidays, so the loop must stop as soon as the target is met rather than working every profitable day.
- **Every day is needed** (the second row, which reaches exactly $15$ on the fourth day): zero holidays.
- **Exactly reaching $W$** stops the loop, since the check is `earned >= w` at the top of each iteration.
- **Working the best-paying days first is optimal** by the usual exchange argument: swapping a chosen day for a better-paying unchosen one never increases the day count.
- **The guarantee that all days together reach $W$** means the loop always terminates having met the target, so no "impossible" branch is needed.

## Dry run

First sample: $W = 10$, earnings $3, 2, 6, 1, 3$ sorted descending to $6, 3, 3, 2, 1$.

| day worked | earns | running total | reached $10$? |
|---:|---:|---:|:---:|
| 1 | 6 | 6 | no |
| 2 | 3 | 9 | no |
| 3 | 3 | 12 | **yes** |

Three days worked out of five, so `2` holidays.

---

Same problem in rating order (#174 of 486): [../../by-rating/174-HOLIDAYS.md](../../by-rating/174-HOLIDAYS.md)
