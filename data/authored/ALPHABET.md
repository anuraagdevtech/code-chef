---
topic: Sets
subtopic: Subset containment
time: $O(|W|)$ per word
space: $O(1)$
---
Jeff can read a word exactly when every letter in it is one he knows:

$$\text{set}(W_i) \subseteq \text{set}(S)$$

Building the known letters into a `set` once, outside the loop, makes each word a single subset test with $O(1)$ lookups per character. Rebuilding the set per word, or scanning the string `S` for each character, would turn a linear solution into a quadratic one for no reason.

Python spells the subset test directly as `set(w) <= known`, which reads exactly like the mathematics.

Two things do **not** matter, and noticing that avoids wasted work. Letter **repetition** is irrelevant — a word may use a known letter many times, which is why sets rather than counts are the right structure. And **order** is irrelevant too; sample case 1 has Jeff knowing `act` and reading `cat`, a different arrangement of the same letters.

The guarantee that each letter appears in $S$ at most once means $S$ is already effectively a set, so no deduplication is needed — though converting to a set does it for free.

Sample case 2, `dog`, fails on the very first letter, and the `<=` short-circuits there.

Note the input shape: there is **no $T$**. The first line is the known-letter string, the second is $N$, and then come $N$ words — each producing one `Yes` or `No`.

## Edge cases

- **Repetition in the word is irrelevant**: `cat` and `catt` both need only $\{a, c, t\}$, which is why a set comparison is right and counting is not needed.
- **Order is irrelevant** too — `act` and `cat` are the same requirement.
- **One unknown letter is enough to fail**: `dog` shares nothing with $\{a,c,t\}$, but `cad` would fail just as surely on the single `d`.
- **All 26 letters known**: every word answers `Yes`.
- **Input shape**: no test-case count — the first token is the known-letters string, then the word count, then the words.

## Dry run

Known letters $\{a, c, t\}$.

| word | letters used | subset? | output |
|---|---|:---:|---|
| `cat` | $\{c, a, t\}$ | yes | `Yes` |
| `dog` | $\{d, o, g\}$ | no | `No` |
