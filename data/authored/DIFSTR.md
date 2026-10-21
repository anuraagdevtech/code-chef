---
topic: Constructive
subtopic: Cantor diagonalisation
time: $O(N)$ per test case
space: $O(N)$
---
The input is deliberately square — $N$ strings of length $N$ — which is exactly the setting for **diagonalisation**. Build the answer by flipping the diagonal:

$$R_i = 1 - S_i[i]$$

Then $R$ differs from $S_i$ at position $i$, for every $i$. One position per string, each string handled by a different position, and there are just enough positions to go around. This is Cantor's argument from the proof that the reals are uncountable, run on a finite square.

No search is needed, and the construction is $O(N)$ rather than the $O(N^2)$ of reading the input — it touches only one character per string, so it would even work on a stream where each string is read and discarded.

A counting sanity check: there are $2^N$ binary strings of length $N$ and only $N$ are forbidden, so for $N \geq 1$ an answer always exists (and for $N \geq 5$ the vast majority of strings work). The diagonal construction is just a way to name one without searching.

Many answers are accepted. For the first sample — `101`, `110`, `100` — the diagonal is $1, 1, 0$, so we print `001`, while the sample prints `111`; both differ from all three. For the second sample the diagonal of `1100`, `1010`, `0100`, `0010` is $1, 0, 0, 0$, giving `0111` against the sample's `1101`.

Note the problem counts strings of different lengths as different too, but since every candidate must have length $N$ that clause never comes into play.

## Edge cases

- **Cantor's diagonal argument gives the answer outright.** Flipping the $i$-th character of the $i$-th string produces a string that differs from row $i$ at position $i$ — so it differs from every row, and only the $N$ diagonal characters need reading.
- **The strings are square** ($N$ strings of length $N$), which is exactly what makes a diagonal exist; a rectangular input would need a different approach.
- **Only $N$ of the $N^2$ characters are examined**, so the whole thing is linear rather than quadratic.
- **$N = 1$**: one string of one character, and flipping it gives the only other option.
- **Duplicate input strings are harmless** — the construction differs from each row independently, so repeated rows cost nothing.
- **This answer differs from the sample's** (`001` against `111` for the first case); any string differing from all $N$ is accepted, so a special judge checks it.
- **Bytes are compared against the literal `0x30`** rather than decoded, keeping the scan allocation-free.

## Dry run

First sample: three strings of length $3$.

| $i$ | string | character at position $i$ | flipped |
|---:|---|---:|---:|
| 0 | `101` | `1` | `0` |
| 1 | `110` | `1` | `0` |
| 2 | `100` | `0` | `1` |

Result `001`, which differs from `101` at position $0$, from `110` at position $0$, and from `100` at position $2$.
