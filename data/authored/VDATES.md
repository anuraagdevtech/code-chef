---
topic: Conditionals & Case Work
subtopic: Classifying a value against an interval
time: $O(1)$ per test case
space: $O(1)$
---
The valid window for the second dose is $[L, R]$ days after the first, and $D$ days have passed. Three outcomes:

- $D < L$ — the window has not opened: `Too Early`
- $D > R$ — the window has closed: `Too Late`
- otherwise — `Take second dose now`

Testing the two extremes first and letting the middle fall through to the `else` keeps the in-range case free of a two-sided comparison.

Both endpoints are **inclusive**, which is the detail the samples check. Case 4 has $D = L = 8$, exactly on the opening day, and the correct answer is `Take second dose now` rather than `Too Early`. A strict `<=` in the wrong place would flip it.

The output strings must match exactly, including the capitalisation and the spaces in `Take second dose now` — the problem does not say the checker is case-insensitive here, unlike many of its neighbours.

The constraint $L \leq R$ guarantees the window is never empty, so every input falls into exactly one of the three cases.

With $T$ up to $10^5$ and values to $10^9$, the only performance consideration is bulk input reading; the comparisons themselves are trivial.
