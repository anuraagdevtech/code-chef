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
