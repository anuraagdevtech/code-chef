---
topic: Hashing
subtopic: Equal prefix states (A-B, A-C) mark balanced substrings
time: $O(N)$ expected
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $a_i, b_i, c_i$ be the numbers of each letter in the first $i$ characters. The substring $(i, j]$ has equally many of each letter exactly when

$$a_j - b_j = a_i - b_i \quad\text{and}\quad a_j - c_j = a_i - c_i,$$

i.e. the pair $(a - b,\; a - c)$ is the same at both ends.

So scan the string keeping this pair as the current state, with a dictionary counting how many earlier prefixes had each state (the empty prefix has state $(0, 0)$). For every position add the number of earlier prefixes with the same state to the answer, then record the current state.

## Edge cases

- The empty prefix must be counted, otherwise balanced substrings starting at the first character are lost.
- The answer can be about $N^2 / 6$ and needs 64 bits.
- A string missing one of the letters has no balanced substring.
- The input is a single line; trailing whitespace is stripped.

## Dry run

`S = ABACABA`. States after each prefix:

`(0,0)` -> A `(1,1)` -> B `(0,1)` -> A `(1,2)` -> C `(1,1)` -> A `(2,2)` -> B `(1,2)` -> A `(2,3)`.

`(1,1)` occurs at prefixes 1 and 4 (substring `BAC`), and `(1,2)` at prefixes 3 and 6 (substring `CAB`).

Answer 2.
