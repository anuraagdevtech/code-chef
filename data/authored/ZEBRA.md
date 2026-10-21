---
topic: Greedy
subtopic: Earliest hops, then one long final leap
time: $O(N)$ per test case
space: $O(N)$
---
Colours must alternate, so after $j$ jumps Chef stands on colour $S_1 \oplus (j \bmod 2)$ — the required colour at every step is fixed in advance and does not depend on the route.

That makes the greedy clean: take the **first $K-1$ jumps as early as possible**, then make the last jump as far as possible. Landing earlier is never worse, because the set of legal landing spots for a later jump is a suffix of the blocks, and a suffix only grows as the current position moves left. So

- for $j = 1, \ldots, K-1$: move to the smallest index beyond the current one with the required colour;
- for the last jump: move to the **largest** index beyond the current one with the required colour.

If any step finds no such index, exactly $K$ jumps are impossible and the answer is $-1$. Note the problem insists on *exactly* $K$ jumps, so stopping early is not allowed even when Chef has already gone far.

The samples cover the three behaviours. In `100101` with $K = 2$, Chef starts on white at block $1$, hops minimally to the black block $2$, then leaps to the last white block, $6$. In `10111` with $K = 1$ the single jump must land on black, and the only black block is $2$ — so the answer is $2$ even though blocks $3, 4, 5$ lie further on. And `000000` offers no colour change at all, so even one jump is impossible.

Greedily minimising the early jumps is what makes the one-leap-at-the-end optimal; doing it the other way round — jumping far immediately — would strand Chef with no room left.

## Edge cases

- **The first $K-1$ jumps should land as early as possible**, which keeps the most blocks in reach for the ones that follow — and the earliest legal landing from block $i$ is the end of $i$'s own colour run.
- **The final jump should go as far as possible**, to the *last* block of the opposite colour. Splitting the strategy this way is the whole solution: greedy-early for all but the last jump, greedy-far for the last.
- **Running out of blocks mid-way gives $-1$** (the `at == n` break), which is how an all-one-colour crossing fails.
- **A single colour throughout** (the third row, all zeros) admits no jump at all, so even $K = 1$ answers $-1$.
- **Exactly $K$ jumps are required**, not at most $K$ — so a crossing that allows fewer is a failure, not a partial success.
- **The run-end table is built right to left**, with `nxt[i] = i + 1` when the colours differ and inherited otherwise, which gives every start its earliest landing in one pass.
- **The last-occurrence map is also built right to left** with `setdefault`, so each colour records its final position.
- **$S_i \neq S_j$ is the only colour rule**, so the alternation follows automatically from jumping to a different colour each time.

## Dry run

First sample: $N = 6$, $K = 2$, $S = $ `100101`.

| step | at block | colour | action |
|---|---:|---|---|
| start | 1 | white | — |
| jump 1 (early) | 2 | black | earliest differing block |
| jump 2 (far) | 6 | white | last white block |

Output `6`. Jumping far on the first move instead would land on block $4$ or $6$ and leave no legal second jump to a black block beyond.
