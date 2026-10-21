---
topic: Conditionals & Case Work
subtopic: Monotonic quantities
time: $O(1)$ per test case
space: $O(1)$
---
The key property is one the statement never says outright: **goals are never taken away**. A football score only ever increases, independently for each team.

That single observation settles the problem. The score $A:B$ can later become $C:D$ precisely when neither team would have to lose a goal:

$$C \geq A \quad\text{and}\quad D \geq B$$

Nothing else is required. There is no need to reason about how many goals were scored in between, in what order, or whether the totals are reachable in some number of moves — because each team's count moves independently and in steps of one, every pair satisfying the two inequalities is reachable.

This is worth dwelling on because the instinct is to look for a harder invariant, perhaps involving $C - A$ versus $D - B$. There is none. Recognising that a quantity is *monotonic* and that its components are *independent* is what turns a seemingly stateful question into two comparisons.

Equality is allowed in both inequalities: a score can stay where it is, so $A:B \to A:B$ is `POSSIBLE`, as sample case 3 confirms.

Note the input layout — each test case spans **two** lines, $A\;B$ then $C\;D$. Reading the whole stream as a flat token list makes the line structure irrelevant.

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
