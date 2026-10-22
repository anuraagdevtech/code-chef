---
topic: Strings
subtopic: Placing a block and its mirror, costed in O(1)
time: $O(|S|)$ per test case for the cost scan, plus $O(|S|)$ per tied placement
space: $O(|S|)$
---
The target is a palindrome of the same length containing `lucky`. Placing `lucky` at position $p$ forces, by the palindrome condition, its reverse `ykcul` at the mirrored position $q = |S| - p - 4$ (0-indexed $q = |S|-5-p$). So a placement is a **pair of forced blocks**, and it is only legal when they do not contradict each other.

Checking the overlaps settles which $p$ are legal. With the two blocks $\delta$ apart, the shared characters must agree; working through $\delta = 0, 1, 2, 3$ gives a clash every time (`lucky` against `ykcul`), while $\delta = 4$ agrees on the single shared letter (`y`, or `l` the other way round) and $\delta \geq 5$ is disjoint. So

$$\text{legal} \iff |p - q| \geq 4$$

which is empty exactly when $|S| < 9$ — hence `unlucky` for the sample's eight `a`s. The shortest lucky palindrome is `luckykcul`, of length $9$.

Everything outside the blocks splits into mirror pairs $(i, |S|-1-i)$, and those pairs are **the same for every placement**: a pair whose two characters already agree is kept as is at no cost, and a disagreeing pair costs one change and takes the smaller of the two letters, which is both cheapest and lexicographically best. An unforced centre keeps its own character.

That makes each placement's cost $O(1)$: ten character comparisons for the blocks, minus the double-counted shared position when $|p-q| = 4$, plus a prefix-sum lookup for the untouched mirror pairs. One pass finds the minimum cost; a second builds the string only for the tied placements and keeps the smallest.

`laubcdkey` ties at $8$ between `luckykcul` and `ykculucky`, and the lexicographic rule picks the former. `luckycodechef` costs $6$: the prefix `lucky` is free, the mirror `ykcul` costs $5$, and the pair $(\texttt{c}, \texttt{d})$ costs one more, resolving to `c`.

## Edge cases

- **Placing `lucky` forces its mirror image too.** A palindrome containing `lucky` at position $p$ must contain `ykcul` at the mirrored position $n-5-p$, so both five-character blocks are fixed together.
- **The two blocks can overlap, and then the shared cell must not be charged twice.** When $|p - q| = 4$ exactly one position belongs to both blocks, and the duplicate cost is subtracted; when they are closer than that the letters conflict outright and the placement is skipped.
- **Positions outside the blocks cost by mirror pair, not by character.** A pair already matching is free; a mismatched pair costs one edit. The prefix array of pair mismatches lets each placement be priced in constant time rather than by rescanning.
- **A string shorter than five characters can never work** → `unlucky`, which the empty candidate loop produces.
- **`aaaaaaaa` is `unlucky` for a different reason**: at length $8$ the two blocks would have to overlap by two, which conflicts — so no placement exists at all.
- **Ties are broken lexicographically**, which is why every minimal-cost placement is rebuilt and the smallest string chosen; free pairs take the smaller of the two letters.
- **An odd length leaves a centre character** that is its own mirror and costs nothing to keep.

## Dry run

Second sample: `luckycodechef`, length $13$, so the mirror of a block at $p$ sits at $q = 8 - p$.

| $p$ | $q$ | blocks | cost |
|---:|---:|---|---:|
| 0 | 8 | `lucky` already at $0$; `ykcul` needs writing at $8$ | 6 |

With $p = 0$ the first block is free and the second costs five edits, plus one more from the remaining mirror pairs — $6$ in total, giving `luckycocykcul`.
