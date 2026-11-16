---
topic: Dynamic Programming
subtopic: Run compression and a bit-parallel longest common subsequence
time: $O(N+M+AB/w)$ word operations per test case for compressed lengths $A,B$
space: $O(B/w)$ machine words for a fixed alphabet
complexity_note: Auxiliary space excludes the buffered input and output.
---
Replace each maximal run in both strings by its character. Any merged output's run labels must contain both compressed strings as subsequences. Conversely, a shortest common supersequence of these run labels can be expanded into a valid merge of the original runs. Thus the answer is the shortest common supersequence length, $A+B-LCS$.

Compute the LCS length with a bit-parallel row representation. Build a position bitmask for each character of the second string. A row bit marks where the LCS value rises across that row. For a new character, let `x = row | positions[character]`; the update `x & ~(x - ((row << 1) | 1))` implements the ordinary LCS row transitions through bitwise subtraction and borrow propagation. The number of set row bits is the final LCS length.

## Edge cases

- Compress runs before the LCS calculation.
- Relative order within each original string must be preserved.
- Identical compressed strings need only their own number of runs.
- Python integer operations work over many LCS columns at once.

## Dry run

For `abab` and `baba`, both already have four runs. Their LCS length is three, so the minimum merged run count is `4+4-3=5`.
