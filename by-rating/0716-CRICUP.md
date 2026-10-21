# 716 &middot; Cup Finals

> CodeChef problem code [`CRICUP`](https://www.codechef.com/problems/CRICUP) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Absolute difference against a tolerance |
| **CodeChef tags** | `Basic Programming Concepts`, `Conditional Statements`, `Inbuilt functions` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/CRICUP.md](../docs/basic-math/CRICUP.md)

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
