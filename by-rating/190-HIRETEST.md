# 190. Hiring Test

> [`HIRETEST`](https://www.codechef.com/problems/HIRETEST) &middot; difficulty **1260** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Counting characters, then a two-branch rule |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(N \cdot M)$ per test case |
| **Space** | $O(N)$ |

## Question

A company conducted a coding test to hire candidates. $N$ candidates appeared for the test, and each of them faced $M$ problems. Each problem was either unsolved by a candidate (denoted by 'U'), solved partially (denoted by 'P'), or solved completely (denoted by 'F').

To pass the test, each candidate needs to either solve $X$ or more problems completely, or solve $(X-1)$ problems completely, and $Y$ or more problems partially.

Given the above specifications as input, print a line containing $N$ integers. The $i^{th}$ integer should be $1$ if the $i^{th}$ candidate has passed the test, else it should be $0$.

**Input:**
- The first line of the input contains an integer $T$, denoting the number of test cases.
- The first line of each test case contains two space-separated integers, $N$ and $M$, denoting the number of candidates who appeared for the test, and the number of problems in the test, respectively.
- The second line of each test case contains two space-separated integers, $X$ and $Y$, as described above, respectively.
- The next $N$ lines contain $M$ characters each. The $j^{th}$ character of the $i^{th}$ line denotes the result of the $i^{th}$ candidate in the $j^{th}$ problem. 'F' denotes that the problem was solved completely, 'P' denotes partial solve, and 'U' denotes that the problem was not solved by the candidate.

**Output:**
For each test case, print a single line containing $N$ integers. The $i^{th}$  integer denotes the result of the $i^{th}$ candidate. $1$ denotes that the candidate passed the test, while $0$ denotes that he/she failed the test.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 100$
- $2 \le M \le 100$
- $1 \le X, Y \le M$
- $1 \le (X-1)+Y \le M$

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 100$
- $2 \le M \le 100$
- $1 \le X, Y \le M$
- $1 \le (X-1)+Y \le M$

## Sample

**Sample input**

```
3
4 5
3 2
FUFFP
PFPFU
UPFFU
PPPFP
3 4
1 3
PUPP
UUUU
UFUU
1 3
2 2
PPP
```

**Sample output**

```
1100
101
0
```

<details><summary>Explanation</summary>

- **Sample Test 1:** There are $4$ candidates and $5$ problems. Each candidate needs to solve $3$ or more problems completely, or $2$ problems completely and $2$ or more problems partially. Only the first and the second candidates satisfy this.

- **Sample Test 2:** The candidates need to either solve at least one problem completely, or they need to solve three or more problems partially. Only candidates $1$ and $3$ satisfy this.

- **Sample Test 3:** The candidate needs to either solve two or more problems completely, or solve at least one problems completely and two problems partially. The candidate does not satisfy this.

</details>

## Approach

For each candidate, count the full solves $F$ and the partial solves $P$ in their result string. The pass rule has two independent routes:

$$F \geq X \quad\text{or}\quad \bigl(F = X - 1 \text{ and } P \geq Y\bigr)$$

The second branch is narrow and precise: it applies at **exactly** $X-1$ full solves, not at "fewer than $X$". A candidate with $X-2$ full solves cannot compensate with any number of partials. Sample case 3 is built on this — one candidate with $X = 2$, zero full solves and three partials fails, because $0 \neq X - 1 = 1$.

Within the first test case, candidates 2 and 3 both have $F = 2 = X - 1$ and differ only in partials: $P = 2$ passes against $Y = 2$, while $P = 1$ does not. Those two rows isolate the second branch exactly.

The `U` characters never enter the rule, so they can be ignored entirely rather than counted.

Output formatting is the other thing to get right: the $N$ results are printed as a single line of digits with **no separators** — `1100`, not `1 1 0 0`. Joining the per-candidate characters and emitting one line per test case does it.

The constraint $1 \leq (X-1) + Y \leq M$ guarantees the second route is always attainable in principle, so neither branch is vacuous.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        x, y = int(data[pos + 2]), int(data[pos + 3])
        rows = data[pos + 4:pos + 4 + n]
        pos += 4 + n
        res = []
        for row in rows:
            full, partial = row.count(b"F"), row.count(b"P")
            # The fallback needs exactly x - 1 full solves, not merely fewer.
            ok = full >= x or (full == x - 1 and partial >= y)
            res.append("1" if ok else "0")
        out.append("".join(res))        # one line of digits, no separators
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The fallback needs *exactly* $X - 1$ full solves, not merely fewer.** The first case's fourth candidate `PPPFP` has one full and four partial solves against $X = 3$, and fails despite having far more than $Y = 2$ partials. Writing the condition as `full < x and partial >= y` accepts this row wrongly.
- **$X$ may be $1$**, which makes the fallback need zero full solves — the second case's `PUPP` qualifies on partials alone.
- **Nothing solved at all** (the second case's `UUUU`): a $0$.
- **Meeting the primary bar makes the partials irrelevant.** `FUFFP` has three full solves and is accepted without its partial count ever being consulted.
- **The output is one line of $N$ digits with no separators**, not $N$ separate lines — `1100`, not four lines.
- **$(X-1) + Y \leq M$ is guaranteed**, so the fallback is always attainable by some candidate in principle.

## Dry run

First sample: $N = 4$, $M = 5$, $X = 3$, $Y = 2$.

| candidate | full `F` | partial `P` | $\geq X$? | $= X{-}1$ and $\geq Y$? | digit |
|---|---:|---:|:---:|:---:|:---:|
| `FUFFP` | 3 | 1 | **yes** | — | 1 |
| `PFPFU` | 2 | 2 | no | yes ($2 = 2$, $2 \geq 2$) | 1 |
| `UPFFU` | 2 | 1 | no | no ($1 < 2$ partials) | 0 |
| `PPPFP` | 1 | 4 | no | no ($1 \neq 2$ full) | 0 |

Output `1100`. Rows 3 and 4 fail for different reasons: too few partials, and the wrong number of full solves.

---

Same problem grouped by topic: [../docs/strings/HIRETEST.md](../docs/strings/HIRETEST.md)
