# 136. Chef and IPC Certificates

> [`IPCCERT`](https://www.codechef.com/problems/IPCCERT) &middot; difficulty **922** &middot; time limit **3s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Filtering rows on two independent criteria |
| **CodeChef tags** | `Basic Programming Concepts`, `Algorithms`, `Conditional Statements`, `Implementation` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(N \cdot K)$ |
| **Space** | $O(1)$ |

## Question

There were $N$ students (numbered $1$ through $N$) participating in the Indian Programming Camp (IPC) and they watched a total of $K$ lectures (numbered $1$ through $K$). For each student $i$ and each lecture $j$, the $i$-th student watched the $j$-th lecture for $T_{i, j}$ minutes.

Additionally, for each student $i$, we know that this student asked the question, "What is the criteria for getting a certificate?" $Q_i$ times.

The criteria for getting a certificate is that a student must have watched at least $M$ minutes of lectures in total and they must have asked the question no more than $10$ times.

Find out how many participants are eligible for a certificate.

**Input**
- The first line of the input contains three space-separated integers $N$, $M$ and $K$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains $K+1$ space-separated integers $T_{i, 1}, T_{i, 2}, \ldots, T_{i, K}, Q_i$.

**Output**
Print a single line containing one integer — the number of participants eligible for a certificate.

**Constraints**
- $1 \le N, K \le 1,000$
- $1 \le M \le 10^6$
- $1 \le Q_i \le 10^6$ for each valid $i$
- $1 \le T_{i, j} \le 1,000$ for each valid $i$ and $j$

## Constraints

- $1 \le N, K \le 1,000$
- $1 \le M \le 10^6$
- $1 \le Q_i \le 10^6$ for each valid $i$
- $1 \le T_{i, j} \le 1,000$ for each valid $i$ and $j$

## Sample

**Sample input**

```
4 8 4
1 2 1 2 5
3 5 1 3 4
1 2 4 5 11
1 1 1 3 12
```

**Sample output**

```
1
```

<details><summary>Explanation</summary>

- Participant $1$ watched $1 + 2 + 1 + 2 = 6$ minutes of lectures and asked the question $5$ times. Since $6 \lt M$, this participant does not receive a certificate.
- Participant $2$ watched $3 + 5 + 1 + 3 = 12$ minutes of lectures and asked the question $4$ times. Since $12 \ge M$ and $4 \le 10$, this participant receives a certificate.
- Participant $3$ watched $1 + 2 + 4 + 5 = 12$ minutes of lectures and asked the question $11$ times. Since $12 \ge M$ but $11 \gt 10$, this participant does not receive a certificate.
- Participant $4$ watched $1 + 1 + 1 + 3 = 6$ minutes of lectures and asked the question $12$ times. Since $6 \lt M$ and $12 \gt 10$, this participant does not receive a certificate.

Only participant $2$ receives a certificate.

</details>

## Approach

A student qualifies when **both** conditions hold: total watch time of at least $M$ minutes, and at most $10$ questions asked.

$$\sum_{j=1}^{K} T_{i,j} \geq M \quad\text{and}\quad Q_i \leq 10$$

Each row of input holds $K$ watch times followed by the question count, so the row is read as $K+1$ values with the last one split off. Mis-slicing that boundary — including $Q_i$ in the watch-time sum, or summing only $K-1$ entries — is the main hazard, and it would produce plausible-looking totals.

The threshold $10$ is a **constant in the statement**, not an input. It is easy to look for a fourth input value that does not exist; the first line holds only $N$, $M$ and $K$.

Note there is **no $T$** here: one dataset, one answer.

Sample walkthrough, with $M = 8$:

| Student | Watch total | Questions | Eligible |
|---|---|---|---|
| 1 | $6$ | $5$ | no — too few minutes |
| 2 | $12$ | $4$ | **yes** |
| 3 | $12$ | $11$ | no — one question too many |
| 4 | $6$ | $12$ | no — both fail |

Only one qualifies. Student 3 is the discriminating case: plenty of watch time but $11 > 10$ questions, so a solution checking only the minutes would answer $2$.

Both comparisons are inclusive — exactly $M$ minutes or exactly $10$ questions still qualifies.

## Solution

```python
import sys

MAX_QUESTIONS = 10          # a constant from the statement, not an input


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    pos = 3
    eligible = 0
    for _ in range(n):
        row = data[pos:pos + k + 1]       # k watch times, then the question count
        pos += k + 1
        watched = sum(int(v) for v in row[:k])
        questions = int(row[k])
        if watched >= m and questions <= MAX_QUESTIONS:
            eligible += 1
    print(eligible)


main()
```

---

Same problem grouped by topic: [../docs/arrays/IPCCERT.md](../docs/arrays/IPCCERT.md)
