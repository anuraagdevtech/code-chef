---
topic: Conditionals & Case Work
subtopic: Ranking by priority
time: $O(1)$
space: $O(1)$
---
The child most likely inherits the **more common** of the two parents' eye colours, and the statement fixes the ordering: brown is most common, then blue, with green the rarest.

So assign each colour a rank — `R` $> $ `B` $> $ `G` by commonness — and output whichever parent's colour ranks higher. With a rank map, the answer is a single `max` keyed on it, rather than the nine-case table that two parents over three colours would otherwise suggest.

Equal colours need no special handling: if both parents share a colour, the maximum is that colour, which is also the correct answer.

Turning a verbal ordering into a numeric key is the transferable idea here. The same trick handles any "pick the most X" problem where X is a stated ranking rather than a numeric value — define the key once and let `max` or `sorted` do the work, instead of enumerating pairs.

Note the ordering is by **commonness**, not alphabetical and not by the order the letters appear in the statement. Reading `G` as dominant because green is mentioned as special would invert the rule.

There is **no $T$** here: the input is a single line of two space-separated characters, one test case.

## Edge cases

- **Both alleles the same** (`B B`): that colour, so no tie-break is needed.
- **The ordering is dominance, not alphabetical.** Brown beats blue beats green, so for `B G` the answer is `B` — yet `max('B', 'G')` on the raw characters returns `G`, because alphabetically `B < G < R`. Sorting the letters directly gets this backwards for every blue-green pair.
- **Green only wins when both alleles are green.**
- **Input shape**: two space-separated characters with no test-case count.

## Dry run

Ranking: `R` $= 2$, `B` $= 1$, `G` $= 0$.

| input | ranks | higher | output |
|---|---|---|---|
| `R B` | $2, 1$ | `R` | `R` |
| `B B` | $1, 1$ | either | `B` |

For `B G` the ranks are $1, 0$, so `B` — the case where alphabetical order would mislead.
