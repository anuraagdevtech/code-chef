---
topic: Dynamic Programming
subtopic: Only the difference of the counters matters, and only within [-2, 2]
time: $O(N + M)$ per test case
space: $O(M)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Every event only compares $a$ with $b$, and a reset sets both to 0, so the state is the difference $d = a - b$. Each minute $d$ changes by $\pm 1$; a type-1 event scores if $d > 0$ and otherwise resets $d$ to 0; a type-2 event scores if $d < 0$ and otherwise resets.

The difference never needs to leave $[-2, 2]$. An excursion that goes from 2 up to 3 and later comes back can be mirrored to go from 2 down to 1 and back: the sign of $d$ is the same at every moment, so every event has the same outcome, and the walk ends at the same value. The same holds on the negative side.

That leaves a DP with five states: `best[d]` is the maximum score with current difference $d$. Each minute shift the states by $\pm 1$ within the range, then apply the event of that minute, if any: add 1 to the states on the scoring side and merge all other states into $d = 0$ (taking the maximum).

## Edge cases

- The increment happens at the start of the minute and the event half a minute later, so the move comes first.
- $d = 0$ at an event never scores, whichever type it is.
- Minutes without an event only move the difference.
- Unreachable states use a large negative sentinel.

## Dry run

`N = 5`, events at minutes 1, 2, 5 with types 1, 2, 1.

- Minute 1: go to $d = 1$; type 1 scores: 1 point.
- Minute 2: the type-2 event needs $d < 0$, but from $d = 1$ only 0 or 2 is reachable: reset to 0, still 1 point. (Starting with $d = -1$ instead would score at minute 2 but not at minute 1 - also 1 point.)
- Minutes 3-5: three moves from 0 can end at $d = 1$; type 1 scores: 2 points.

Answer 2.
