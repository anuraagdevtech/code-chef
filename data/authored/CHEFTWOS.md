---
topic: Dynamic Programming
subtopic: Three-state automaton for good strings, run on both strings at once
time: $O(N)$ per test case
space: $O(1)$ - at most nine states
complexity_note: Auxiliary space excludes the buffered input and output.
---
First characterise a good string. Reading left to right, a `1` simply steps forward. A `2` at position $i$ jumps to $i+2$; position $i+1$ is then still unvisited and can only be picked up by going $i \to i+2 \to i+1 \to i+3$, which forces the pattern `2 2 1` on positions $i, i+1, i+2$. So everything before the final character must be a concatenation of the blocks `1` and `221`; the last character itself is never used for a move, so it may be either digit.

That is a three-state automaton: state 0 between blocks, state 1 after the first `2`, state 2 after `22` (only `1` allowed next). Run a DP over pairs of states, one per string. At each position there are two choices - keep or swap - which feed the characters to the two automata in either order. After the first $N-1$ positions both automata must be in state 0, and the last position contributes a free factor of 2.

## Edge cases

- $N = 1$: the walk is already finished, so both subsets (swap or not) work and the answer is 2.
- When $a_i = b_i$ both choices lead to the same state pair and are counted twice, as they should be - they are different subsets.
- A block `221` cut off by the end of the prefix leaves a non-zero state and is rejected.
- Characters arrive as bytes, hence the keys 49 and 50 in the transition table.

## Dry run

`a = 1111`, `b = 2211`.

Positions 1-2 offer (1,2) and (1,2). The second string needs `22` there to start a `221` block, so the two positions must be either both kept or both swapped - 2 ways; the mixed choices die because a lone `2` is followed by a `1`.

Position 3 is (1,1): both choices keep both automata valid and bring them back to state 0 - 4 ways. The last position doubles it.

Answer 8.
