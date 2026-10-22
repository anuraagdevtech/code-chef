[&larr; 024. Car or Bike](024-TRAVELFAST.md) &middot; [Index](README.md) &middot; [026. The Three Topics &rarr;](026-THREETOPICS.md)

# 025. Is the Score Consistent

> [`TRUESCORE`](https://www.codechef.com/problems/TRUESCORE) &middot; difficulty **572** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Monotonic quantities |
| **CodeChef tags** | `Basic Programming Concepts`, `Conditional Statements` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is watching a football match. The current score is $A:B$, that is, team $1$ has scored $A$ goals and team $2$ has scored $B$ goals. Chef wonders if it is possible for the score to become $C:D$ at a later point in the game (i.e. team $1$ has scored $C$ goals and team $2$ has scored $D$ goals). Can you help Chef by answering his question?

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $A$ and $B$ - the intial number of goals team $1$ and team $2$ have scored respectively.
- The second line of each test case contains two integers $C$ and $D$ - the final number of goals team $1$ and team $2$ must be able to score respectively.

**Output**

For each testcase, output `POSSIBLE` if it is possible for the score to become $C:D$ at a later point in the game, `IMPOSSIBLE` otherwise.

You may print each character of `POSSIBLE` and `IMPOSSIBLE` in uppercase or lowercase (for example, `possible`, `pOSsiBLe`, `Possible` will be considered identical).

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq A,B,C,D \leq 10$

## Sample

**Sample input**

```
3
1 5
3 5
3 4
2 6
2 2
2 2
```

**Sample output**

```
POSSIBLE
IMPOSSIBLE
POSSIBLE
```

<details><summary>Explanation</summary>

**Test case 1:** The current score is $1:5$. If team $1$ scores $2$ more goals, the score will become $3:5$. Thus $3:5$ is a possible score.

**Test case 2:** The current score is $3:4$. It can be proven that no non-negative pair of integers $(x, y)$ exists such that if team $1$ scores $x$ more goals and team $2$ scores $y$ more goals the score becomes $2:6$ from $3:4$. Thus in this case $2:6$ is an impossible score.

**Test case 3:** The current score is already $2:2$. Hence it is a possible score.

</details>

## Approach

The key property is one the statement never says outright: **goals are never taken away**. A football score only ever increases, independently for each team.

That single observation settles the problem. The score $A:B$ can later become $C:D$ precisely when neither team would have to lose a goal:

$$C \geq A \quad\text{and}\quad D \geq B$$

Nothing else is required. There is no need to reason about how many goals were scored in between, in what order, or whether the totals are reachable in some number of moves — because each team's count moves independently and in steps of one, every pair satisfying the two inequalities is reachable.

This is worth dwelling on because the instinct is to look for a harder invariant, perhaps involving $C - A$ versus $D - B$. There is none. Recognising that a quantity is *monotonic* and that its components are *independent* is what turns a seemingly stateful question into two comparisons.

Equality is allowed in both inequalities: a score can stay where it is, so $A:B \to A:B$ is `POSSIBLE`, as sample case 3 confirms.

Note the input layout — each test case spans **two** lines, $A\;B$ then $C\;D$. Reading the whole stream as a flat token list makes the line structure irrelevant.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # Goals never decrease, and the two teams move independently.
        out.append("POSSIBLE" if c >= a and d >= b else "IMPOSSIBLE")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Nothing changed** ($2\,2$ then $2\,2$): goals need not increase, so this is `POSSIBLE`. A solution demanding strict growth fails here, and the sample includes it.
- **One team's score falls** ($3\,4$ then $2\,6$): the first team drops from $3$ to $2$, which no amount of play can do, so `IMPOSSIBLE` — even though the second team's score rose.
- **Both zero throughout** ($0\,0$ then $0\,0$): `POSSIBLE`, and the lower bound of $0$ means the all-zero case is real input.
- **The two teams are independent.** One may rise while the other stands still; the only rule is that neither may fall, so both comparisons must be checked and ANDed.

## Dry run

Each test case is two lines, "before" then "after".

| before $A\,B$ | after $C\,D$ | $C \geq A$ | $D \geq B$ | output |
|---|---|:---:|:---:|---|
| $1\,5$ | $3\,5$ | yes | yes (equal) | `POSSIBLE` |
| $3\,4$ | $2\,6$ | **no** | yes | `IMPOSSIBLE` |
| $2\,2$ | $2\,2$ | yes (equal) | yes (equal) | `POSSIBLE` |

Row 2 fails on the first team alone, which is enough.

---

Same problem grouped by topic: [../docs/conditionals-case-work/TRUESCORE.md](../docs/conditionals-case-work/TRUESCORE.md)
