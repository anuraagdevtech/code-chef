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
