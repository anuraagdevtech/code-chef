---
topic: Strings
subtopic: Substring replacement
time: $O(|S|)$ per test case
space: $O(|S|)$
---
Replace every occurrence of `party` with `pawri`. Python's `str.replace` does exactly this, scanning once and substituting all occurrences:

```python
s.replace("party", "pawri")
```

Two properties make the built-in the right tool rather than a hand-rolled loop.

**It replaces all occurrences, not just the first.** Sample case 2, `partypartiparty`, contains two `party` substrings separated by a near-miss, and both must change. A `find`-and-splice written by hand often handles only the first.

**Replacements cannot cascade.** The pattern and its replacement have the same length and differ in the middle, and crucially `pawri` does not contain `party`, so newly written text can never form a fresh match. That means a single pass is sufficient and there is no risk of the substitution feeding on its own output — the kind of bug that turns repeated `replace` calls into an infinite loop or a wrong answer.

Sample case 1, `part`, is the near-miss: a prefix of the pattern but not the pattern, so the string is returned unchanged. Partial matches must not be rewritten.

With $|S|$ up to $10^5$ the single linear pass is comfortable; the C-implemented `replace` is substantially faster than any character-by-character Python loop.

## Edge cases

- **A partial match stays put**: `part` lacks the trailing `y`, so it is left alone. The whole five-character pattern must appear.
- **A near miss**: `parti` is not a match either, and the second sample row contains one between two real matches.
- **Adjacent occurrences** (`partyparty`): both are replaced in the one pass.
- **No cascading is possible**, because `pawri` does not contain `party` — so a single `replace` is correct and there is no need to loop until the string stabilises.
- **$|S|$ up to $10^5$ across ten cases**, so the replacement should be a single library call rather than a character loop.

## Dry run

| input | matches found | output |
|---|---|---|
| `part` | none | `part` |
| `partypartiparty` | positions $0$ and $10$ | `pawripartipawri` |

In the second row the middle `parti` is skipped, leaving it untouched between the two replacements.
