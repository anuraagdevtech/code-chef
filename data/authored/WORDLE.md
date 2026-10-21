---
topic: Strings
subtopic: Position-wise comparison
time: $O(L)$ per test case with $L = 5$
space: $O(L)$
---
This is the simplified Wordle: each position is judged **only against the same position** in the hidden word. Character $i$ of the mask is `G` when $S_i = T_i$ and `B` otherwise.

`zip(s, t)` walks the two strings in lockstep, and a generator expression inside `"".join` builds the mask in one pass:

```python
"".join("G" if a == b else "B" for a, b in zip(s, t))
```

The thing to notice is what this problem deliberately leaves out. Real Wordle has a third state — a letter present in the word but in the wrong place — which requires counting letter multiplicities and is substantially trickier, because a repeated guess letter must not be credited more times than it occurs in the answer. Here there is no yellow, so no cross-position bookkeeping is needed at all and each index is independent.

Sample case 1 makes that concrete: `ABCDE` against `EDCBA` shares every letter, yet only the middle `C` sits in the right place, so the mask is `BBGBB` rather than all green. An implementation that checked membership with `in` instead of comparing positions would wrongly report five matches.

Both strings are guaranteed to be length $5$ and uppercase, so no validation or case folding is needed. Each test case spans two lines, read as two consecutive tokens.

## Edge cases

- **Nothing in common** (`ABCDE` against `EDCBA`): only the middle letter aligns, giving `BBGBB` — note that `A` and `E` both *appear* in the other word, yet score black, because this variant has no "right letter, wrong place" state.
- **Repeated letters** (`START` against `STUNT`): the `T` at index $1$ matches and the `T` at index $4$ matches, each judged on its own. Because there is no yellow state, duplicates need no tallying — the usual Wordle difficulty disappears.
- **Identical words**: all `G`.
- **No match anywhere**: all `B`.
- Both strings are exactly five characters, so no length handling is needed.

## Dry run

`START` against the guess `STUNT`, index by index:

| index | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| answer | `S` | `T` | `A` | `R` | `T` |
| guess | `S` | `T` | `U` | `N` | `T` |
| result | `G` | `G` | `B` | `B` | `G` |

Output `GGBBG`.
