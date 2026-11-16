---
topic: Dynamic Programming
subtopic: Subset-sum reachability as an integer bitset
time: $O(NM/w)$ word operations per test case
space: $O(M/w)$ machine words
complexity_note: Auxiliary space excludes the buffered input and output.
---
Bit $s$ of an integer records whether a subset of processed notes sums to $s$. Initially only bit zero is set. For a note of value $v$, shifting the old bitset by $v$ represents taking that note; OR with the old bitset represents either taking or skipping it.

Mask out sums above the demand, since all values are positive and such sums can never become useful. Test the target bit after processing every note. Python's arbitrary-precision bit operations process many sum states at once; $w$ denotes its fixed-size integer limb width.

## Edge cases

- Each note can be used at most once.
- Equal-valued notes are separate items.
- Read all notes even after the target becomes reachable.

## Dry run

For three notes `[1,1,1]`, reachable sums evolve from `{0}` to `{0,1}`, then `{0,1,2}`, then `{0,1,2,3}`. Demand three is achievable.
