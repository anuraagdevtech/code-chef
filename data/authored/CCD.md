---
topic: Prefix Sums
subtopic: The alternating sum of differences is the only invariant
time: $O(N + Q)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $d_i = (B_i - A_i) \bmod 26$ be how much position $i$ still has to be increased. A move adds 1 to two adjacent positions, so it changes $d_i$ and $d_{i+1}$ together and leaves the alternating sum $d_L - d_{L+1} + d_{L+2} - \dots$ unchanged modulo 26. For a substring to become equal to its target this alternating sum must therefore be 0.

The condition is also sufficient: process the substring from the left, applying the move at $(i, i+1)$ exactly $d_i$ times to fix position $i$. Everything is forced, and what remains at the last position is, up to sign, the alternating sum - zero by assumption.

Store prefix sums of $\pm d_i$ with the sign given by the parity of the index. A query $[L, R]$ is Yes exactly when the two prefix values at $R$ and $L - 1$ agree modulo 26; a global sign flip does not affect whether the sum is zero.

## Edge cases

- A single-character query has no move available: the characters must already match.
- Increments are cyclic, so all arithmetic is modulo 26.
- Moves must stay inside the queried substring, which the argument respects.
- The strings are read as bytes; only differences are used.

## Dry run

`A = abcdz`, `B = nbhea`. Differences $d$: `13 0 5 1 1` (the last is `z -> a`).

- `2 2`: $d_2 = 0$ - Yes.
- `1 3`: $13 - 0 + 5 = 18 \not\equiv 0$ - No.
- `4 5`: $1 - 1 = 0$ - Yes (one move on positions 4, 5).
