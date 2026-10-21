---
topic: Greedy
subtopic: Pairing adjacent elements after sorting
time: $O(N \log N)$
space: $O(N)$
---
Sort the lengths, then sweep left to right: if the current stick and the next differ by at most $D$, pair them and skip both; otherwise discard the current one and move on.

Two facts make this greedy optimal.

**An optimal pairing can always be taken between sorted neighbours.** If sticks $a < b$ are paired and some unpaired $c$ lies between them, then $c$ is within $D$ of both, so re-pairing to use $c$ costs nothing. Repeating this argument pushes every pair onto adjacent positions.

**Pairing the smallest available stick with its immediate successor is never worse.** The smallest stick is the hardest to place — only larger sticks are left, and the next one is the closest. If it cannot pair with its neighbour it cannot pair with anything, so discarding it loses nothing.

Together these justify the single sweep. Sorting is the dominant cost at $O(N \log N)$, and the sweep is linear.

Tracing the sample, $[1,3,3,4,9]$ with $D = 2$: $1$ pairs with $3$ (gap $2$), then $3$ pairs with $4$ (gap $1$), and $9$ is left alone — $2$ pairs. Note the greedy does *not* pair the two identical $3$s; doing so would still give $2$ pairs here, but the sweep's choice is what the proof covers.

Note there is **no $T$**: the first line holds $N$ and $D$, then $N$ lengths follow one per line. $D$ may be $0$, in which case only exactly equal sticks pair.

## Edge cases

- **No test-case count**: the first line holds $N$ and $D$ together, then $N$ lines of lengths — reading a leading $T$ consumes the first stick.
- **The smallest remaining stick pairs with its nearest neighbour or not at all.** Any stick it could pair with is at least as far away as its immediate successor, so pairing it with the successor never forecloses a better option — the exchange argument behind the greedy.
- **$D = 0$**: only exactly equal lengths pair, which still works — the two $3$s in the sample would pair at $D = 0$.
- **An unpairable stick advances the index by one, not two**, so the next stick keeps its chance: with $D = 2$ on $1, 9, 10$, skipping the $1$ lets $9$ and $10$ pair.
- **$N = 1$**: the loop never runs and the answer is $0$.
- **Odd $N$** always leaves at least one stick over, which falls out of the two-step walk without a special case.
- Lengths and $D$ up to $10^9$; differences stay well inside the integer range.

## Dry run

$N = 5$, $D = 2$, lengths $1, 3, 3, 9, 4$ sorted to $1, 3, 3, 4, 9$.

| $i$ | pair considered | difference | $\leq D$? | pairs | next $i$ |
|---:|---|---:|:---:|---:|---:|
| 0 | $1, 3$ | 2 | yes | 1 | 2 |
| 2 | $3, 4$ | 1 | yes | 2 | 4 |
| 4 | — | — | — | 2 | stop |

The $9$ is left unpaired. Output `2`.
