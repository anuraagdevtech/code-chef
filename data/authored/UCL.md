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

## Edge cases

- **Twelve matches per group**, because four teams each play every other team twice — so the match count is fixed and needs no reading.
- **The literal `vs.` occupies a token**, so each match line is five whitespace-separated tokens and the stride must be five; treating it as four desynchronises the whole case.
- **Goal difference counts home and away goals alike**, as the statement insists, so each match updates both teams symmetrically.
- **A draw awards one point to each**, not zero, which the three-way branch handles.
- **Points come first and goal difference only breaks ties**, which the tuple key $(-\text{points}, -\text{difference})$ encodes in one sort.
- **Teams must be registered before their first result** — the `setdefault` pair — or a team that only ever draws would be missing from the table.
- **Only the top two are printed**, on one line, separated by a space.
- **No further tie-break is specified** beyond goal difference, so two teams level on both are not distinguished by the statement.

## Dry run

First sample group, after all twelve matches:

| team | points | goal difference |
|---|---:|---:|
| manutd | 16 | +13 |
| fcbarca | 8 | +4 |
| arsenal | 5 | $-5$ |
| lyon | 4 | $-12$ |

Sorted by points then difference, the top two are `manutd fcbarca`.
