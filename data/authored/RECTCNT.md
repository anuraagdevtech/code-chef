---
topic: Hashing
subtopic: Group vertical sides by their two heights
time: $O(N)$ expected per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
No three points share an $x$ coordinate, so each vertical line has at most one possible vertical side. Record the ordered pair of its two $y$ coordinates. Two vertical sides form an axis-aligned rectangle exactly when these height pairs agree.

When a pair has already appeared $f$ times, its next occurrence contributes $f$ new rectangles. Sum these contributions without enumerating rectangles.

## Edge cases

- Input ends with `0`; there is no leading test-case count.
- A vertical line with one point contributes no side.
- Normalise the two heights so input order does not matter.

## Dry run

The sample has vertical sides at `x=1,3,7`, all with heights `(1,5)`. Their contributions are `0+1+2=3`.
