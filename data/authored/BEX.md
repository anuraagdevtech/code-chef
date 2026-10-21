---
topic: Stacks
subtopic: Prefix minimum carried alongside a stack
time: $O(1)$ amortised per action, $O(N)$ overall
space: $O(N)$
---
The pile is a stack, but the operation Harry performs is not a plain pop: he reaches *into* the pile for the minimum and discards everything above it. The two tie-breaks in the statement are what pin down the answer — the minimum number of exercises first, and among equal minima the one needing the fewest removals, i.e. the one **closest to the top**.

The insight is that the chosen book is always determined by a **prefix minimum**. Alongside the pile, store for every height $i$ the position of the best book in the pile's bottom $i$ books:

$$\text{best}[i] = \begin{cases} i & v_i \leq v_{\text{best}[i-1]} \\ \text{best}[i-1] & \text{otherwise}\end{cases}$$

The non-strict $\leq$ is exactly the second tie-break: on a tie the newer, higher book wins.

Answering a query is then two lookups. With the pile at height $sz$, the chosen book sits at $j = \text{best}[sz]$, so Harry removes $sz - j$ books, and afterwards the pile is cut back to height $j - 1$ — the book is finished and everything above it went to the floor.

Cutting back to $j - 1$ is why the prefix-minimum array beats the obvious **monotonic stack**. A monotonic stack would discard the books below $j$ as "can never win", but the cut makes exactly those books the pile again, and their minimum is needed for the next query. Keeping every book with its prefix minimum means the cut is a single assignment to $sz$ and all the older information is still intact.

Books arriving with $0$ remaining exercises are never added — Harry only piles up books that still have work left in them.

In the sample, `mathematics` (6) beats `english` (9) and `geography` (8), so one book is removed; the pile is then cut to just `english`, and the new `graphics` (3) immediately becomes the minimum with nothing above it.
