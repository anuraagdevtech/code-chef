# 322. Chef Restaurant 

> CodeChef problem code [`CHEFRES`](https://www.codechef.com/problems/CHEFRES) &middot; difficulty **1776** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Binary search over disjoint intervals |
| **Time** | $O((N + M) \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Chef is a cook and he has recently opened a restaurant.

The restaurant is open during $N$ time intervals $[L_1, R_1), [L_2, R_2), \dots, [L_N, R_N)$. No two of these intervals overlap — formally, for each valid $i$, $j$ such that $i \neq j$, either $R_i \lt L_j$ or $R_j \lt L_i$.

$M$ people (numbered $1$ through $M$) are planning to eat at the restaurant; let's denote the time when the $i$-th person arrives by $P_i$. If the restaurant is open at that time, this person does not have to wait, but if it is closed, this person will wait until it is open. Note that if this person arrives at an exact time when the restaurant is closing, they have to wait for the next opening time.

For each person, calculate how long they have to wait (possibly $0$ time), or determine that they will wait forever for the restaurant to open.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of the input contains two space-separated integers $N$ and $M$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $L_i$ and $R_i$.
- $M$ lines follow. For each valid $i$, the $i$-th of these lines contains a single integer $P_i$.

**Output**
For each test case, print $M$ lines. For each valid $i$, the $i$-th of these lines should contain a single integer — the time person $i$ has to wait, or $-1$ if person $i$ has to wait forever.

**Constraints**
- $1 \le T \le 100$
- $1 \le N, M \le 10^5$
- $1 \le L_i \lt R_i \le 10^9$ for each valid $i$
- $1 \le P_i \le 10^9$ for each valid $i$
- the intervals are pairwise disjoint
- the sum of $N$ for all test cases does not exceed $3 \cdot 10^5$
- the sum of $M$ for all test cases does not exceed $3 \cdot 10^5$

**Subtasks**
**Subtask #1 (30 points):**
- the sum of $N$ for all test cases does not exceed $1,000$
- the sum of $M$ for all test cases does not exceed $1,000$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N, M \le 10^5$
- $1 \le L_i \lt R_i \le 10^9$ for each valid $i$
- $1 \le P_i \le 10^9$ for each valid $i$
- the intervals are pairwise disjoint
- the sum of $N$ for all test cases does not exceed $3 \cdot 10^5$
- the sum of $M$ for all test cases does not exceed $3 \cdot 10^5$

## Sample

**Sample input**

```
1
4 5
5 7
9 10
2 3
20 30
5
6
7
35
1
```

**Sample output**

```
0
0
2
-1
1
```

<details><summary>Explanation</summary>

**Query $1$:** The person coming at time $5$ does not have to wait as the restaurant is open in $[5,7)$ slot.

**Query $2$:** The person coming at time $6$ does not have to wait as the restaurant is open in $[5,7)$ slot.

**Query $3$:** The person coming at time $7$ has to wait since the restaurant is closed at time $7$. The next slot in which the restaurant opens is $[9,10)$. Thus, the person waits for $2$ units of time.

**Query $4$:** The person coming at time $35$ has to wait forever as the restaurant does not open after time $30$.

</details>

## Approach

The intervals are **pairwise disjoint**, so sorting them by $L$ also sorts them by $R$, and the whole timeline becomes a clean sequence of open windows separated by closed gaps. That makes each query a binary search.

For an arrival at $P$, locate the last interval with $L_i \leq P$:

- if that interval satisfies $P < R_i$, the restaurant is open and the wait is $0$;
- otherwise $P$ falls in a gap (or before the first opening), so the wait is $L_j - P$ for the next interval;
- if no interval starts at or after $P$, the wait is forever: $-1$.

The intervals are **half-open**, $[L, R)$, which the statement spells out: someone arriving exactly at closing time must wait for the next opening. So the open test is the strict $P < R_i$, not $P \leq R_i$.

Sample arrival $P = 7$ is precisely that case. The window $[5,7)$ has just closed, so the answer is not $0$ but the $2$-unit wait until $9$. Arrivals at $5$ and $6$ fall inside and wait nothing.

$P = 1$ precedes every window, so it waits until the earliest opening at $2$. $P = 35$ comes after the last window closes at $30$, with nothing ahead — $-1$.

Python's `bisect_right` on the list of $L$ values gives the insertion point directly: the interval before it is the candidate containing $P$, and the one at it is the next opening. Sorting once per test case and reusing it across all $M$ queries is what keeps this log-time rather than linear per query.

## Solution (Python)

```python
import sys
from bisect import bisect_right


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        intervals = sorted((int(data[pos + 2 * i]), int(data[pos + 2 * i + 1]))
                           for i in range(n))
        pos += 2 * n
        starts = [l for l, _ in intervals]
        for i in range(m):
            p = int(data[pos + i])
            k = bisect_right(starts, p)
            # Intervals are half-open, so arriving exactly at R means waiting.
            if k and p < intervals[k - 1][1]:
                out.append("0")
            elif k < n:
                out.append(str(starts[k] - p))
            else:
                out.append("-1")
        pos += m
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O((N + M) \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The intervals are pairwise disjoint**, so sorting them by start and binary searching gives at most one candidate containing $P$ — the last interval starting at or before it.
- **The intervals are half-open $[L, R)$**, which the statement spells out: someone arriving exactly at closing time must wait for the next opening. So the open test is the strict $P < R$.
- **Arrival at exactly $R$ is the trap.** The sample's $P = 7$ finds the window $[5,7)$ just closed, so the answer is not $0$ but the two-unit wait until $9$.
- **Arriving before every window** waits for the earliest opening, which the search handles with $k = 0$ (the sample's $P = 1$, waiting until $2$).
- **Arriving after the last window closes** gives $-1$, with no interval ahead — the sample's $P = 35$.
- **A wait of $0$ is reported when inside a window**, not the time until it closes.
- **Sum of $N$ and $M$ each up to $3 \cdot 10^5$**: one sort per case and a bisect per query.

## Dry run

Sample: windows $[2,3)$, $[5,7)$, $[9,10)$, $[20,30)$ after sorting.

| $P$ | last window starting $\leq P$ | inside it? | answer |
|---:|---|:---:|---:|
| 5 | $[5,7)$ | yes | `0` |
| 6 | $[5,7)$ | yes | `0` |
| 7 | $[5,7)$ | **no** ($7 \not< 7$) | `2` (wait for $9$) |
| 35 | $[20,30)$ | no | `-1` |
| 1 | none | — | `1` (wait for $2$) |

---

Same problem in rating order (#460 of 486): [../../by-rating/460-CHEFRES.md](../../by-rating/460-CHEFRES.md)
