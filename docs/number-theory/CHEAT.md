# 77. Dracula Eats

> CodeChef problem code [`CHEAT`](https://www.codechef.com/problems/CHEAT) &middot; difficulty **763** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Counting residues in a range |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

*Eat, drink, and be scary*

There are $N$ spooky days left until Halloween.
Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys what they serve on Tuesday.

Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the next $N$ days **(including today)** before Halloween.

Note that Dracula follows the standard $7$-day calendar, with Tuesday immediately following Monday.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains a single integer $N$, denoting the number of spooky days.

**Output**

For each test case, output on a new line the number of times Dracula would have had his favorite meal after $N$ days.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
4
1
10
15
16
```

**Sample output**

```
0
2
2
3
```

<details><summary>Explanation</summary>

**Test case $1$:** The first day is Monday, and Dracula has only one day. So, no Tuesdays are encountered, and the answer is $0$.

**Test case $2$:** The first day is Monday, so the second and ninth days are Tuesdays.
Dracula can eat his favorite meal twice.

**Test case $3$:** Once again, the second and ninth days are Tuesday, so in $15$ days, Dracula still gets to eat his favorite meal only twice.

**Test case $4$:** After the ninth day, the $16$-th day is also a Tuesday. So, this time Dracula gets to eat his favorite meal three times - on days $2, 9, 16$.

</details>

## Approach

Today is Monday and that counts as day $1$, so day $d$ is a Tuesday exactly when

$$d \equiv 2 \pmod 7$$

The question becomes: how many integers in $[1, N]$ leave remainder $2$ on division by $7$? Those are $2, 9, 16, 23, \ldots$, and counting them up to $N$ gives

$$\left\lfloor \frac{N - 2}{7} \right\rfloor + 1 \quad\text{for } N \geq 2,\qquad 0 \text{ otherwise}$$

which collapses neatly into the single expression

$$\left\lfloor \frac{N + 5}{7} \right\rfloor$$

with no special case. The shift by $5$ works because it slides the first Tuesday down to the multiple-of-seven boundary, and it returns $0$ for $N = 1$ automatically — sample case 1.

The general form is worth remembering: the count of integers in $[1, N]$ congruent to $r$ modulo $m$ is $\lfloor (N + m - r)/m \rfloor$. Here $m = 7$ and $r = 2$, giving the $+5$.

Samples 3 and 4 fix the boundary precisely. $N = 15$ still gives $2$, because day $16$ — the third Tuesday — has not arrived; $N = 16$ includes it and gives $3$. An off-by-one would shift both.

The phrase "including today" is what makes Monday day $1$ rather than day $0$; reading it the other way moves every Tuesday by one and breaks all four samples.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Today (Monday) is day 1, so Tuesdays are the days d = 2 (mod 7).
        out.append(str((n + 5) // 7))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$N = 1$**: today is Monday, so no Tuesday has arrived yet and the answer is $0$. The sample's first row.
- **$N = 2$**: the first Tuesday, giving $1$.
- **$N = 15$ against $N = 16$**: $2$ then $3$. The sample has both, and they straddle the third Tuesday on day $16$ — an off-by-one in the offset moves this step by a day.
- **Largest input** ($N = 1000$): $143$ Tuesdays.
- **The convention that day $1$ is Monday is what fixes the $+5$.** Tuesdays are the days congruent to $2 \bmod 7$, so the count is $\lfloor (N + 5)/7 \rfloor$; starting the week anywhere else shifts every answer.

## Dry run

| $N$ | $N + 5$ | $//\,7$ | Tuesdays (days $2, 9, 16, \ldots$) | output |
|---:|---:|---:|---|---|
| 1 | 6 | 0 | none yet | `0` |
| 10 | 15 | 2 | $2, 9$ | `2` |
| 15 | 20 | 2 | $2, 9$ | `2` |
| 16 | 21 | 3 | $2, 9, 16$ | `3` |

Rows 3 and 4 are consecutive days either side of the third Tuesday.

---

Same problem in rating order (#83 of 486): [../../by-rating/083-CHEAT.md](../../by-rating/083-CHEAT.md)
