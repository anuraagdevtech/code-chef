# 12. Expert Setter

> CodeChef problem code [`EXPERT`](https://www.codechef.com/problems/EXPERT) &middot; difficulty **561** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Percentage comparison without division |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

A problem setter is called an *expert* if **at least** $50 \%$ of their problems are approved by Chef.

Munchy submitted $X$ problems for approval. If $Y$ problems out of those were approved, find whether Munchy is an *expert* or not.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a two space-separated integers $X$ and $Y$ - the number of problems submitted and the number of problems that were approved by Chef.

**Output**

For each test case, output on a new line `YES`, if Munchy is an *expert*. Otherwise, print `NO`.

The output is case-insensitive. Thus, the strings `YES`, `yes`, `yeS`, and `Yes` are all considered the same.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq Y \le X \leq 10^6$

## Sample

**Sample input**

```
4
5 3
1 1
4 1
2 1
```

**Sample output**

```
YES
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** We are given that $3$ out of $5$ problems were approved. Thus, $60 \%$ of the problems were approved. Since at least $50 \%$ of the problems were approved, Munchy is an *expert*.

**Test case $2$:** We are given that $1$ out of $1$ problems were approved. Thus, $100 \%$ of the problems were approved. Since at least $50 \%$ of the problems were approved, Munchy is an *expert*.

**Test case $3$:** We are given that $1$ out of $4$ problems were approved. Thus, $25 \%$ of the problems were approved. Since at least $50 \%$ of the problems were not approved, Munchy is not an *expert*.

**Test case $4$:** We are given that $1$ out of $2$ problems were approved. Thus, $50 \%$ of the problems were approved. Since at least $50 \%$ of the problems were approved, Munchy is an *expert*.

</details>

## Approach

Munchy is an expert when the approval rate reaches half:

$$\frac{Y}{X} \geq \frac{1}{2}$$

Multiplying through by $2X$ — positive, since $X \geq 1$ — gives the integer test

$$2Y \geq X$$

This is the same cross-multiplication used in the Exams problem, but with one important difference: here the bar is **at least** $50\%$, not *strictly greater*. So the comparison is `>=` and the exact-half case answers `YES`. Sample case 4 ($X = 2$, $Y = 1$) is exactly half and answers `YES`, whereas the corresponding tie in Exams answered `NO`.

That contrast is the real lesson. Two problems can share identical arithmetic and differ only in whether the boundary is inclusive, so the phrase "at least" versus "strictly greater" deserves as much attention as the formula itself.

The constraint $Y \le X$ is guaranteed, so there is no need to handle an approval count exceeding the submission count.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # y / x >= 1 / 2  <=>  2 * y >= x   ("at least", so not strict)
        out.append("YES" if 2 * y >= x else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Exactly half approved** ($X = 2$, $Y = 1$): $2Y = X$, and the requirement is "at least half", so the answer is `YES`. The comparison must be `>=` — this is the opposite convention to the strictly-greater percentage problems, and the sample tests it.
- **Everything approved** ($Y = X$): $2X \geq X$ holds for every $X \geq 1$, so always `YES`.
- **Just under half** ($X = 4$, $Y = 1$): $2 \geq 4$ fails, so `NO`.
- **Smallest input** ($X = Y = 1$): $2 \geq 1$, so `YES`.
- $Y \leq X$ is guaranteed, so there is no need to guard against more approvals than submissions.
- $X \leq 10^6$ makes $2Y$ at most $2 \times 10^6$, so nothing overflows even in fixed-width arithmetic.

## Dry run

| $X$ | $Y$ | $2Y$ | $2Y \geq X$ | output |
|---:|---:|---:|:---:|---|
| 5 | 3 | 6 | yes | `YES` |
| 1 | 1 | 2 | yes | `YES` |
| 4 | 1 | 2 | no | `NO` |
| 2 | 1 | 2 | yes (equality) | `YES` |

The last row is the tight case: exactly half still counts.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#19 of 486): [../../by-rating/019-EXPERT.md](../../by-rating/019-EXPERT.md)
