# 62. Cup Finals

> CodeChef problem code [`CRICUP`](https://www.codechef.com/problems/CRICUP) &middot; difficulty **716** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Absolute difference against a tolerance |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

It is the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing teams is *less than or equal to* $D$.

Given that the skills of the teams competing in the final are $X$ and $Y$ respectively, determine whether Chef will find the game interesting or not.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- Each testcase consists of a single line of input containing three space-separated integers $X$, $Y$, and $D$ — the skill levels of the teams and the maximum skill difference.

**Output**

For each testcase, output "YES" if Chef will find the game interesting, else output "NO" (without the quotes). The checker is case-insensitive, so "YeS" and "nO" etc. are also acceptable.

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq X, Y \leq 100$
- $0 \leq D \leq 100$

## Sample

**Sample input**

```
3
5 3 4
5 3 1
5 5 0
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** The skill difference between the teams is $2$, which is less than the maximum allowed difference of $4$.

**Test case $2$:** The skill difference between the teams is $2$, which is more than the maximum allowed difference of $1$.

</details>

## Approach

The match is interesting when the skill gap is at most $D$:

$$|X - Y| \leq D$$

The absolute value matters because the problem never says which team is stronger. Writing `x - y <= d` would wrongly accept every case where $Y$ exceeds $X$, since a negative difference is always below the threshold — a bug that passes roughly half the tests and so looks almost right.

The comparison is inclusive: "less than or equal to $D$" means a gap of exactly $D$ still counts. Sample case 1 has a gap of $2$ against $D = 4$, comfortably inside; case 2 has the same gap of $2$ against $D = 1$ and fails.

Sample case 3 covers the degenerate end: equal skills give a gap of $0$, and with $D = 0$ the inclusive comparison is what makes it `YES`. Since $D$ may be $0$, a strict `<` would get this wrong.

The same `abs`-against-tolerance shape appears whenever a problem asks whether two quantities are "close enough", and keeping it as one expression avoids reasoning about which value is larger.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, d = map(int, data[1 + 3 * i:4 + 3 * i])
        # Either team may be the stronger one, so compare the magnitude.
        out.append("YES" if abs(x - y) <= d else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Equal strengths with zero tolerance** ($X = Y = 5$, $D = 0$): the gap is $0$, which is within $0$, so `YES`. The sample's third row sits on this boundary.
- **The gap exactly equals $D$**: `YES`, since the comparison is non-strict.
- **Either team may be stronger.** The absolute value is essential — a one-sided $X - Y \leq D$ accepts every case where $X < Y$ regardless of how far apart they are.
- **Off by one** ($X = 5$, $Y = 3$, $D = 1$): a gap of $2$ against a tolerance of $1$, so `NO`. The sample's second row.

## Dry run

| $X$ | $Y$ | $|X - Y|$ | $D$ | within? | output |
|---:|---:|---:|---:|:---:|---|
| 5 | 3 | 2 | 4 | yes | `YES` |
| 5 | 3 | 2 | 1 | no | `NO` |
| 5 | 5 | 0 | 0 | yes (equal) | `YES` |

> CodeChef tags: `Basic Programming Concepts`

---

Same problem in rating order (#67 of 486): [../../by-rating/067-CRICUP.md](../../by-rating/067-CRICUP.md)
