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

## Edge cases

- **Feasibility is a divisibility check.** All positions sharing a frequency $f$ must group into complete blocks of exactly $f$ equal values, so the count of such positions must be a multiple of $f$ — the fourth row fails because one position claims frequency $2$.
- **Lexicographic smallness comes from opening a fresh label only when needed.** The group for a frequency stays open until it has $f$ members; a new label is minted only when no open group of that frequency exists, and since labels are minted in increasing order, that is always the smallest usable value.
- **$f = 1$ closes immediately**, so a run of ones yields $1, 2, 3, \dots$ — the second row.
- **A single group covering everything** gives all the same label, as in the third row where five positions each claim frequency $5$.
- **Groups of different frequencies interleave freely**, which is why the open groups are tracked per frequency rather than as one pointer — the last row alternates between frequencies $2$ and $3$.
- **A group must be closed once full**, or later positions would wrongly join it and overshoot their claimed frequency.
- **$B_i \leq 10^5$ and the labels stay within $10^5$**, since at most $N$ labels are ever minted.

## Dry run

Last sample: $B = 1, 3, 2, 3, 2, 2, 2, 3$.

| position | $f$ | open group for $f$? | label | group now |
|---:|---:|---|---:|---|
| 1 | 1 | no → mint 1 | 1 | full, closed |
| 2 | 3 | no → mint 2 | 2 | 1 of 3 |
| 3 | 2 | no → mint 3 | 3 | 1 of 2 |
| 4 | 3 | yes (2) | 2 | 2 of 3 |
| 5 | 2 | yes (3) | 3 | full, closed |
| 6 | 2 | no → mint 4 | 4 | 1 of 2 |
| 7 | 2 | yes (4) | 4 | full, closed |
| 8 | 3 | yes (2) | 2 | full, closed |

Output `1 2 3 2 3 4 4 2`.
