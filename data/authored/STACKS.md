---
topic: Binary Search
subtopic: Patience stacking with a sorted top list
time: $O(N \log N)$ per test case
space: $O(N)$
---
Mike's rule — place the disk on the stack whose top is the **smallest radius still strictly greater** than it, else start a new stack — is exactly the *patience sorting* deal, and it has a property that makes it cheap to simulate.

Keep the stack tops in a list sorted ascending. For a disk $d$:

- `bisect_right(tops, d)` gives the index of the first top strictly greater than $d$ — precisely the stack Mike chooses;
- if that index exists, overwrite it with $d$;
- otherwise append $d$ as a new stack.

**The list stays sorted automatically.** Replacing `tops[k]` with $d$ is safe because $d \geq \texttt{tops}[k-1]$ (everything before index $k$ is $\leq d$) and $d < \texttt{tops}[k] \leq \texttt{tops}[k+1]$. Appending is safe because $d$ exceeded every existing top. So no re-sorting is ever needed, and each disk costs one binary search.

That invariant is the whole trick — without it one would reach for a heap or a balanced multiset and work much harder.

Tracing the first sample $(3,4,5,1,1,2)$: the tops grow to $[3,4,5]$, then the first $1$ displaces the $3$, the second $1$ displaces the $4$, and the $2$ displaces the $5$, finishing at $[1,1,2]$ — three stacks.

The output is the **stack count first**, then the tops in ascending order, which is just the list's own order. That leading count is easy to miss from the statement.

Note `bisect_right` rather than `bisect_left` is required: the rule says *strictly* greater, so a top equal to $d$ must not be chosen.
