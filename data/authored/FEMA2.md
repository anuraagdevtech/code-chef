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

## Edge cases

- **The attraction condition is a sliding window in a shifted coordinate.** Setting $w = \text{index} + (\text{sheets so far})$ makes $w_j - w_i$ exactly $|j-i| + S_{i,j}$, so a pair works iff their $w$ values differ by at most $K$ — a sheet costs two, because it occupies a cell *and* adds to $S$.
- **A blocked cell cuts the row**, so both queues are cleared at an `X` — no pair may span it, whatever the distance.
- **Matching the oldest waiting partner is optimal**, because its window expires soonest; saving it for later can only lose a match. That is the standard interval-matching exchange argument.
- **Expired candidates must be dropped from the front** before matching, which is what keeps each queue a valid window.
- **A magnet with no iron in range waits**, joining its own queue in case a later iron arrives — so both queues are needed, not just one.
- **Each piece of iron serves at most one magnet**, which the pop enforces.
- **Empty cells advance the index but nothing else**, while sheets advance both the index and the sheet count.
- **Sum of $N$ up to $5 \cdot 10^6$**, so the byte codes are compared directly and each cell is touched a constant number of times.

## Dry run

First sample: $N = 4$, $K = 5$, $S = $ `I::M`.

| cell | content | sheets so far | $w$ |
|---:|---|---:|---:|
| 1 | `I` | 0 | 1 |
| 2 | `:` | 1 | — |
| 3 | `:` | 2 | — |
| 4 | `M` | 2 | 6 |

The magnet's $w$ is $6$ and the iron's is $1$, a difference of $5 \leq K$ — so they match. Attraction power $= 5 + 1 - 3 - 2 = 1 > 0$ ✓ Output `1`.
