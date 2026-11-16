---
topic: Bit Manipulation
subtopic: Each streak is a power of two minus one - search the number of streaks
time: $O(\log^2 (Y / X))$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A streak of $a$ minutes eats $X (1 + 2 + \dots + 2^{a-1}) = X (2^a - 1)$ burgers, so $Y$ must be a multiple of $X$; let $Z = Y / X$. With $k$ streaks of lengths $a_1, \dots, a_k$, which have to be pairwise distinct,

$$Z = \sum_{i} (2^{a_i} - 1) \iff Z + k = \sum_i 2^{a_i}.$$

The right-hand side is a number whose binary representation has exactly $k$ ones, none of them at bit 0 (every streak lasts at least a minute). So for each $k$ from 1 to 60 check whether $Z + k$ is even and has popcount $k$. If it does, the streak lengths are the positions of its set bits and the time is their sum plus $k - 1$ minutes of breaks.

The weights $2^a - 1$ are super-increasing - each exceeds the sum of all smaller ones - so a number has at most one representation as a sum of distinct weights. The first $k$ that works is therefore the only one, and its time is the answer; if none works the answer is $-1$.

## Edge cases

- $Y$ not divisible by $X$: impossible.
- $Z + k$ odd would need a streak of length 0.
- The breaks cost $k - 1$ minutes, not $k$.
- Trying up to 60 streaks covers every input that fits in 64 bits.

## Dry run

`X = 1, Y = 4`, so $Z = 4$.

- $k = 1$: $Z + 1 = 5$ is odd - no.
- $k = 2$: $Z + 2 = 6 = 110_2$, even with two set bits at positions 1 and 2 - yes.

Streaks of 1 and 2 minutes eat $1 + 3 = 4$ burgers; time $1 + 2 + 1 = 4$.
