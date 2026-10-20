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
