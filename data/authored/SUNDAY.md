---
topic: Sets
subtopic: Union of a fixed set with input values
time: $O(N)$ per test case
space: $O(N)$
---
Day $1$ is a Monday, so within a $30$-day month the Saturdays fall on days $6, 13, 20, 27$ and the Sundays on $7, 14, 21, 28$ — eight weekend days, fixed and independent of the input.

The festivals add more holidays, but the statement warns that a festival **may land on a weekend**, in which case it is already a holiday and must not be counted twice. That makes this a set union rather than a sum:

$$|\,\text{weekends} \cup \text{festivals}\,|$$

Computing it as `len(WEEKEND | set(festivals))` handles the overlap automatically. Adding $8 + N$ would overcount, and sample case 1 catches it immediately: festivals $\{5, 7\}$ include day $7$, a Sunday, so the answer is $9$ rather than $10$. Sample case 3 is the extreme — its single festival on day $13$ is a Saturday, contributing nothing, leaving the bare $8$.

Precomputing the weekend set once, outside the loop, keeps each test case to a single set construction and union.

The $A_i$ are promised distinct, so no duplicates need removing among the festivals themselves — but building a set is the natural way to union them anyway. The note that they arrive unsorted is irrelevant to a set-based solution, though it would matter to one attempting a sorted merge.

## Edge cases

- **A festival falling on a weekend adds nothing.** The third row's single festival is day $13$, already a Saturday, so the answer stays at the eight weekend days. Adding $N$ to $8$ would give $9$.
- **Partial overlap** (the first row has $7$ on a weekend and $5$ not): only the new day counts.
- **The $A_i$ are guaranteed distinct**, so there are no duplicate festivals to collapse — but the union is still needed for weekend collisions.
- **Day $1$ is a Monday**, which fixes the weekend set as $\{6,7,13,14,20,21,27,28\}$ in a $30$-day month. A different starting weekday changes every answer, so that convention is the one assumption to get right.

## Dry run

Weekend days: $6, 7, 13, 14, 20, 21, 27, 28$ — eight of them.

| festivals | already a weekend | new days | total |
|---|---|---:|---:|
| $5, 7$ | $7$ | $5$ | `9` |
| $23, 1, 6$ | $6$ | $23, 1$ | `10` |
| $13$ | $13$ | none | `8` |
