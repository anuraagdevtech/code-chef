---
topic: Simulation
subtopic: Building a league table and sorting by two keys
time: $O(1)$ per test case (12 fixed matches)
space: $O(1)$
---
Pure bookkeeping, but with three details that decide correctness.

**Parsing.** Each line is `Home G vs. G Away`, so splitting on whitespace gives five tokens and the literal `vs.` is simply discarded. Reading the goals as the second and fourth tokens avoids any dependence on team-name length.

**Points.** A win is $3$, a draw $1$ each, a loss $0$ — not the $2$-for-a-win of older formats. Both teams are updated from the same line.

**Goal difference.** Scored minus received, pooled across home and away matches. The statement stresses this: there is no separate home/away tally and no away-goals tie-break.

Ranking is then a lexicographic sort by $(\text{points}, \text{goal difference})$, both descending, and the first two names are the answer. The problem guarantees no tie for these two places, so no third criterion is needed — which is why the standard real-world tie-breaks (head-to-head, goals scored) can be skipped.

In the first sample, `manutd` is unbeaten with $4$ wins and $2$ draws, and `fcbarca` edges the rest on goal difference. The second sample is the reason the goal-difference key matters: `d` tops the group on it, which a points-only sort would get wrong.

The group always has exactly four teams and twelve matches — each ordered pair plays once — so the sizes are fixed and no validation of the schedule is needed. A dictionary keyed by name collects both tallies in a single pass over the twelve lines.
