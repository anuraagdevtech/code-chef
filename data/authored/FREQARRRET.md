---
topic: Greedy
subtopic: Lexicographic labelling of equal-frequency groups
time: $O(N)$ per test case
space: $O(N)$
---
Elements sharing a value form a **group** whose size is that value's frequency, so every index with $B_i = f$ belongs to a group of exactly $f$ indices, all with the same $B$ value. Feasibility is therefore a divisibility check per frequency:

$$f \mid \#\{\,i : B_i = f\,\} \quad \text{for every } f$$

and if any class fails, print $-1$. (Sample 4 has a single index with $B_i = 2$, which cannot fill a group of two.)

For the lexicographically smallest array, note that only the *partition* into groups matters — the labels can then be renamed, and the smallest renaming assigns $1, 2, 3, \ldots$ in order of first appearance. So sweep left to right and, for each index, take the **smallest value available**: join the currently open group of its frequency if there is one, otherwise open a new group with the next unused label. Joining is always better, because it reuses an already-smaller label and a smaller value at the earliest differing position settles the comparison.

This never strands a partial group: within one frequency class, indices fill group after group in order, so each closes exactly when it reaches $f$ members. At most one group per frequency is open at a time, so the bookkeeping is a counter and a label per frequency.

Labels stay within bounds: the number of groups is at most $N \leq 10^5$, matching the $A_i \leq 10^5$ limit.

Sample 5, $B = [1,3,2,3,2,2,2,3]$, shows the interleaving: the lone $B_i = 1$ takes label $1$ and closes at once; the three $3$s share label $2$ across positions $2, 4, 8$; and the four $2$s split into label $3$ (positions $3, 5$) and label $4$ (positions $6, 7$), giving `1 2 3 2 3 4 4 2`.
