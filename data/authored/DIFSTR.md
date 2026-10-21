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
