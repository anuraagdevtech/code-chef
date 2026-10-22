# 462. Bon Appetit

> CodeChef problem code [`FGFS`](https://www.codechef.com/problems/FGFS) &middot; difficulty **1734** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Independent activity selection per compartment |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Our chef has recently opened a new restaurant with a unique style. The restaurant is divided into **K** compartments (numbered from **1** to **K**) and each compartment can be occupied by at most one customer.

 Each customer that visits the restaurant has a strongly preferred compartment **p** (**1 ≤ p ≤ K**), and if that compartment is already occupied, then the customer simply leaves. Now obviously, the chef wants to maximize the total number of customers that dine at his restaurant and so he allows (or disallows) certain customers so as to achieve this task. You are to help him with this.

 Given a list of **N** customers with their arrival time, departure time and the preferred compartment, you need to calculate the maximum number of customers that can dine at the restaurant.

**Input**

 The first line contains an integer **T** denoting the number of test cases. Each of the next **T** lines contains two integers **N** and ** K **, the number of customers that plan to visit the chef's restaurant and the number of compartments the restaurant is divided into respectively. Each of the next **N** lines contains three integers **s_i**, **f_i** and **p_i** , the arrival time, departure time and the strongly preferred compartment of the **i^th** customer respectively.

Note that the **i^th** customer wants to occupy the **p_i^th** compartment from **[s_i, f_i) ** i.e the **i^th** customer leaves just before  ** f_i** so that another customer can occupy that compartment from  ** f_i** onwards.

**Output**

 For every test case, print in a single line the maximum number of customers that dine at the restaurant.

**Constraints**

- ** 1 **≤  **T** ≤ **  30 **

- ** 0 ** ≤ **N**  ≤ ** 10^5**

- ** 1 ** ≤ ** K**  ≤ ** 10^9**

- ** 0 ** ≤  **s_i** < **f_i** ≤ **  10^9**

- ** 1 ** ≤ ** p_i** ≤ ** K **

## Constraints

-  1 ≤  T ≤   30
-  0  ≤ N  ≤  10^5
-  1  ≤  K  ≤  10^9
-  0  ≤  s_i < f_i ≤   10^9
-  1  ≤  p_i  ≤  K

## Sample

**Sample input**

```
2
3 3
1 3 1
4 6 2
7 10 3
4 2
10 100 1
100 200 2
150 500 2
200 300 2
```

**Sample output**

```
3
3
```

<details><summary>Explanation</summary>

**Example case 1.**

All three customers want different compartments and hence all 3 can be accommodated.

**Example case 2.**

If we serve the **1^st**, **2^nd** and **4^th** customers, then we can get a maximum of 3.

</details>

## Approach

Each customer insists on one compartment, so the compartments never interact: the problem **decomposes** into $K$ independent instances, and only the compartments that actually appear matter — which is what makes $K$ up to $10^9$ harmless.

Within a compartment, a customer occupies the half-open interval $[s_i, f_i)$, and two customers are compatible when their intervals do not overlap. Maximising the count is the classic **activity-selection** problem, solved by sorting on finishing time and taking each interval whose start is at or after the last accepted finish:

$$\text{accept } i \iff s_i \geq f_{\text{last}}$$

The exchange argument: among any optimal solution's intervals, replacing the first by the globally earliest-finishing one keeps it feasible, since that one ends no later and so blocks no more of the future. Induction does the rest.

Half-open intervals are the detail to get right — a customer leaving at $f$ frees the compartment *at* $f$, so the comparison is $\geq$, not $>$. The second sample turns on it: in compartment $2$, the customer $[100,200)$ is followed by $[200,300)$, which fits exactly, while $[150,500)$ would collide.

Grouping by compartment with a dictionary and sorting each group gives $O(N \log N)$ overall. Note $N$ may be $0$, in which case the answer is $0$ and no groups exist.

The first sample has three customers in three different compartments, so all three dine. The second has one in compartment $1$ and three in compartment $2$, of which two are compatible — total $3$.

## Solution (Python)

```python
import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 2                       # K itself is never needed
        rooms = defaultdict(list)
        for _ in range(n):
            s, f, p = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            rooms[p].append((f, s))
        served = 0
        for intervals in rooms.values():
            intervals.sort()           # by finishing time
            free_at = -1
            for f, s in intervals:
                # Intervals are half-open, so starting exactly at f is fine.
                if s >= free_at:
                    served += 1
                    free_at = f
        out.append(str(served))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The compartments are completely independent**, since a customer insists on exactly one of them — so the problem splits into $K$ separate activity-selection instances.
- **Earliest finishing time first is the classic optimum** for each compartment, and sorting the tuples as $(f, s)$ makes that the natural order.
- **The intervals are half-open $[s, f)$**, so a customer may start exactly when the previous one leaves — which is why the test is `s >= free_at` rather than a strict inequality. The second sample row relies on it.
- **$K$ is read but never used**: only the compartments that actually appear matter, so a dictionary beats an array of size $K$ at $K \leq 10^9$.
- **$N$ may be $0$**, giving an answer of $0$ with no intervals to read.
- **A customer who finds the compartment busy simply leaves**, which is why rejecting one is free — the chef may disallow customers at will.
- **$s_i < f_i$ is guaranteed**, so no zero-length visit needs special thought.

## Dry run

Second sample: $N = 4$ customers.

| compartment | intervals (sorted by finish) | accepted |
|---:|---|---:|
| 1 | $[10, 100)$ | 1 |
| 2 | $[100, 200)$, $[200, 300)$, $[150, 500)$ | 2 |

In compartment $2$, the first two chain exactly at time $200$; the third starts at $150$, which is already busy. Total `3`.

> CodeChef tags: `Algorithms`, `Greedy`

---

Same problem in rating order (#434 of 486): [../../by-rating/434-FGFS.md](../../by-rating/434-FGFS.md)
