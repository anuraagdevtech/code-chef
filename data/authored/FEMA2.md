---
topic: Greedy
subtopic: Interval bipartite matching with two queues
time: $O(N)$ per test case
space: $O(N)$
---
The attraction condition $P_{i,j} = K + 1 - |j - i| - S_{i,j} > 0$ rearranges to a budget:

$$|j - i| + S_{i,j} \leq K$$

Both terms depend on the pair, which looks awkward — but they collapse into a single coordinate. Let $\mathrm{pre}[i]$ count the sheets in cells $1 \ldots i$ and define

$$w(i) = i + \mathrm{pre}[i]$$

For a magnet at $i$ and iron at $j > i$, neither of which is a sheet, $w(j) - w(i) = (j - i) + (\mathrm{pre}[j-1] - \mathrm{pre}[i])$, and that second bracket is exactly the sheet count strictly between them. So the condition is just

$$|w(j) - w(i)| \leq K$$

Each sheet costs the same as a cell of distance, so folding it into the coordinate makes the problem one-dimensional. Blocked cells are a hard cut rather than a cost, so they split the row into independent **blocks**, solved separately and summed.

Within a block, every magnet can serve any iron whose $w$ lies in a window of radius $K$ around it. Scanning left to right, $w$ only increases, so an unmatched piece that has fallen out of the current window can never come back and is discarded for good. That makes a two-queue greedy optimal: hold pending magnets and pending irons in FIFO order, and on reaching a new piece, drop the stale opposite-type entries and then match the **oldest** survivor. The oldest is the one with the smallest $w$, hence the one whose window expires soonest — the earliest-deadline-first exchange: if an optimal matching pairs the new piece with a later partner while an older one goes unused, swapping them keeps the matching valid and the same size.

In `I::M` with $K = 5$ the two sheets make $w(1) = 1$ and $w(4) = 6$, a gap of exactly $5$, so the single magnet just reaches its iron. In `MIM_XII:M` the `X` cuts the row in two; each half yields one pair, so the answer is $2$ — note the left block has two magnets but only one iron, and the right block two irons but only one magnet, so the surplus is wasted on both sides.
