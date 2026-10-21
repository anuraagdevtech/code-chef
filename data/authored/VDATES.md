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

## Edge cases

- **$D$ exactly at the lower edge** ($D = L = 8$): inside the window, so `Take second dose now`. The sample's last row tests it, and both ends are inclusive.
- **$D$ exactly at the upper edge** ($D = R$): also inside.
- **Past the window** ($D = 14$ against $R = 10$): `Too Late`.
- **Before the window** ($D = 4444$ against $L = 5555$): `Too Early`.
- **The output strings are exact**, including capitalisation and spacing — `Take second dose now`, `Too Early`, `Too Late`.
- $L \leq R$ is guaranteed, so the window is never empty and the three branches are exhaustive.

## Dry run

| $D$ | $L$ | $R$ | position | output |
|---:|---:|---:|---|---|
| 10 | 8 | 12 | inside | `Take second dose now` |
| 14 | 2 | 10 | past $R$ | `Too Late` |
| 4444 | 5555 | 6666 | before $L$ | `Too Early` |
| 8 | 8 | 12 | on $L$ | `Take second dose now` |
