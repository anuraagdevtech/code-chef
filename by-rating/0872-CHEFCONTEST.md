# 872 &middot; Chef and Contest

> CodeChef problem code [`CHEFCONTEST`](https://www.codechef.com/problems/CHEFCONTEST) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Weighted penalty, then a three-way comparison |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Conditional Statements`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/CHEFCONTEST.md](../docs/basic-math/CHEFCONTEST.md)

## Question

Chef and Chefina are competing against each other in a programming contest. They were both able to solve all the problems in the contest, so the winner between them must be decided by time penalty. Chef solved all the problems in $X$ minutes and made $P$ wrong submissions, while Chefina solved all the problems in $Y$ minutes and made $Q$ wrong submissions. Who won the competition (or was it a draw)?

**Note:** The time penalty is calculated as follows:
- The base time penalty is the time at which the final problem was solved (so, $X$ for Chef and $Y$ for Chefina)
- Each wrong submission adds a penalty of $10$ minutes
- The winner is the person with less penalty time. If they both have the same penalty, it is considered a draw.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers — $X,Y,P$, and $Q$ respectively.

**Output**

For each test case, output a single line containing one string — the name of the winner ("Chef" or "Chefina"), or "Draw" if the match was a draw. Print each string without the quotes.

Each character of the answer can be printed in either uppercase or lowercase, i.e, the strings "Chef", "chEf", "cHeF", etc. are treated as equivalent.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X,Y \leq 100$
- $0 \leq P,Q \leq 100$

## Sample

**Sample input**

```
3
10 8 2 3
10 10 10 10
40 21 2 0
```

**Sample output**

```
Chef
Draw
Chefina
```

<details><summary>Explanation</summary>

**Test Case $1$:**
- Chef solved the problems in $10$ minutes and made $2$ wrong submissions, thus his total penalty is $10 + 2 \cdot 10 = 30$ minutes.
- Chefina solved the problems in $8$ minutes and made $3$ wrong submissions, thus her total penalty is $8 + 3 \cdot 10 = 38$ minutes.

Chef took less time, so he is the winner.

**Test Case $2$:**
- Chef solved the problems in $10$ minutes and made $10$ wrong submissions, thus his total penalty is $10 + 10 \cdot 10 = 110$ minutes.
- Chefina solved the problems in $10$ minutes and made $3$ wrong submissions, thus her total penalty is $10 + 10 \cdot 10 = 110$ minutes.

Chef and Chefina took the same time, so the match is a draw.

**Test Case $3$:**
- Chef solved the problems in $40$ minutes and made $2$ wrong submissions, thus his total penalty is $40 + 2 \cdot 10 = 60$ minutes.
- Chefina solved the problems in $21$ minutes and made $0$ wrong submissions, thus her total penalty is $21 + 0 \cdot 10 = 21$ minutes.

Chefina took less time, so she is the winner.

</details>

## Approach

Penalty is the solve time plus ten minutes for each wrong submission:

$$\text{Chef} = X + 10P, \qquad \text{Chefina} = Y + 10Q$$

Lower penalty wins, with equality a draw.

Two things to keep straight. **Lower is better** — this is a penalty, not a score, so the comparison runs the opposite way to most "who wins" problems. And the wrong-submission counts are weighted by $10$; comparing $X$ against $Y$ alone, or adding $P$ and $Q$ unweighted, both fail.

Sample case 1 shows why the weighting matters: Chefina solved faster ($8$ against $10$) yet loses, because her three wrong submissions cost $30$ against Chef's $20$. A solution comparing only solve times would answer `Chefina`.

Sample case 3 is the opposite — Chefina's $21$ minutes beat Chef's $40$ by enough that his two wrong submissions are irrelevant.

Sample case 2 is the exact draw at $110$ apiece, so the equality branch is needed rather than folded into one of the inequalities.

The input order is $X, Y, P, Q$ — both times first, then both penalty counts — which is not the pairing the prose suggests, so it is easy to bind $P$ to Chefina by accident.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # Input order is X, Y, P, Q: both times, then both wrong counts.
        x, y, p, q = map(int, data[1 + 4 * i:5 + 4 * i])
        chef, chefina = x + 10 * p, y + 10 * q
        # Penalty, so the lower value wins.
        out.append("Chef" if chef < chefina else "Chefina" if chefina < chef else "Draw")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
