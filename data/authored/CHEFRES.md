---
topic: Sorting
subtopic: Binary search over disjoint intervals
time: $O((N + M) \log N)$ per test case
space: $O(N)$
---
The intervals are **pairwise disjoint**, so sorting them by $L$ also sorts them by $R$, and the whole timeline becomes a clean sequence of open windows separated by closed gaps. That makes each query a binary search.

For an arrival at $P$, locate the last interval with $L_i \leq P$:

- if that interval satisfies $P < R_i$, the restaurant is open and the wait is $0$;
- otherwise $P$ falls in a gap (or before the first opening), so the wait is $L_j - P$ for the next interval;
- if no interval starts at or after $P$, the wait is forever: $-1$.

The intervals are **half-open**, $[L, R)$, which the statement spells out: someone arriving exactly at closing time must wait for the next opening. So the open test is the strict $P < R_i$, not $P \leq R_i$.

Sample arrival $P = 7$ is precisely that case. The window $[5,7)$ has just closed, so the answer is not $0$ but the $2$-unit wait until $9$. Arrivals at $5$ and $6$ fall inside and wait nothing.

$P = 1$ precedes every window, so it waits until the earliest opening at $2$. $P = 35$ comes after the last window closes at $30$, with nothing ahead — $-1$.

Python's `bisect_right` on the list of $L$ values gives the insertion point directly: the interval before it is the candidate containing $P$, and the one at it is the next opening. Sorting once per test case and reusing it across all $M$ queries is what keeps this log-time rather than linear per query.

## Edge cases

- **The intervals are pairwise disjoint**, so sorting them by start and binary searching gives at most one candidate containing $P$ — the last interval starting at or before it.
- **The intervals are half-open $[L, R)$**, which the statement spells out: someone arriving exactly at closing time must wait for the next opening. So the open test is the strict $P < R$.
- **Arrival at exactly $R$ is the trap.** The sample's $P = 7$ finds the window $[5,7)$ just closed, so the answer is not $0$ but the two-unit wait until $9$.
- **Arriving before every window** waits for the earliest opening, which the search handles with $k = 0$ (the sample's $P = 1$, waiting until $2$).
- **Arriving after the last window closes** gives $-1$, with no interval ahead — the sample's $P = 35$.
- **A wait of $0$ is reported when inside a window**, not the time until it closes.
- **Sum of $N$ and $M$ each up to $3 \cdot 10^5$**: one sort per case and a bisect per query.

## Dry run

Sample: windows $[2,3)$, $[5,7)$, $[9,10)$, $[20,30)$ after sorting.

| $P$ | last window starting $\leq P$ | inside it? | answer |
|---:|---|:---:|---:|
| 5 | $[5,7)$ | yes | `0` |
| 6 | $[5,7)$ | yes | `0` |
| 7 | $[5,7)$ | **no** ($7 \not< 7$) | `2` (wait for $9$) |
| 35 | $[20,30)$ | no | `-1` |
| 1 | none | — | `1` (wait for $2$) |
