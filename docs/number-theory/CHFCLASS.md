# 139. Akash and Missing Class

> CodeChef problem code [`CHFCLASS`](https://www.codechef.com/problems/CHFCLASS) &middot; difficulty **931** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Counting residues in a range |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Akash loves going to school, but not on weekends.

A week consists of $7$ days (Monday to Sunday). Akash takes a leave every **Saturday**.

If a month consists of $N$ days and the **first-day** of the month is **Monday**, find the number of days Akash would take a leave in the whole month.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, one integer $N$ - the number of days in the month.

**Output**

For each test case, output in a single line, the number of days Akash would take a leave in the whole month.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^9$

**Subtasks**

- **Subtask 1 (30 points) :** $1 \leq N \leq 100$
- **Subtask 2 (70 points) :** Original Constraints

## Sample

**Sample input**

```
4
5
6
8
22
```

**Sample output**

```
0
1
1
3
```

<details><summary>Explanation</summary>

**Test case $1$:** The month consists of $5$ days (Monday, Tuesday, Wednesday, Thursday, and Friday). Since there are no Saturdays, Akash would go to school every day. Thus, he takes a leave for $0$ days.

**Test case $2$:** The month consists of $6$ days (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday). Akash takes a leave only on Saturday. Thus, he takes a leave for $1$ day.

**Test case $3$:** The month consists of $8$ days (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday). Akash takes a leave only on Saturday. Thus, he takes a leave for $1$ day.

</details>

## Approach

Day $1$ is a Monday, so Saturdays fall on days $6, 13, 20, 27, \ldots$ — that is, the days $d$ with

$$d \equiv 6 \pmod 7$$

Counting them in $[1, N]$ gives $\lfloor (N-6)/7 \rfloor + 1$ when $N \geq 6$, and $0$ otherwise. Both branches collapse into the single expression

$$\left\lfloor \frac{N + 1}{7} \right\rfloor$$

which returns $0$ for $N < 6$ with no guard needed.

This is the same counting pattern as the Dracula problem, with the general form: the number of integers in $[1, N]$ congruent to $r$ modulo $m$ is $\lfloor (N + m - r)/m \rfloor$. Here $m = 7$ and $r = 6$, giving the $+1$.

The samples pin the boundary down precisely. $N = 5$ gives $0$ — the month ends the day before the first Saturday. $N = 6$ gives $1$, catching that Saturday exactly. $N = 8$ still gives $1$, since the second Saturday is day $13$. And $N = 22$ gives $3$, counting days $6, 13, 20$ but not $27$.

With $N$ up to $10^9$ a loop over the days is out of the question, so the closed form is not merely tidier — it is the only workable approach.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Day 1 is Monday, so Saturdays are the days d = 6 (mod 7).
        out.append(str((n + 1) // 7))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Basic Math`
