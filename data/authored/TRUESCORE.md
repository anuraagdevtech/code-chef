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
