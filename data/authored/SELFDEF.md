---
topic: Arrays
subtopic: Counting values inside a closed range
time: $O(N)$ per test case
space: $O(1)$
---
A woman qualifies when her age lies between $10$ and $60$ **inclusive of both ends**, so the answer is a single pass counting the values satisfying

$$10 \leq A_i \leq 60$$

Python's chained comparison writes this exactly as the mathematics does — `10 <= a <= 60` — which is both clearer and less error-prone than `a >= 10 and a <= 60`, where it is easy to flip one of the operators.

Inclusivity is the whole trap, and the samples are built around the boundaries rather than the middle. Case 1 contains $65$, just outside the upper limit; case 2 contains $62$, also outside; case 3 contains $9$, one below the lower limit. An age of exactly $10$ or exactly $60$ must count, so both comparisons need the `=`.

As with the other counting problems in this set, nothing needs to be stored: the ages stream past a counter in $O(N)$ time and $O(1)$ space. The per-test-case $N$ varies, so a cursor walks the flat token stream rather than reading line by line.

## Edge cases

- **Both ends of the range are eligible.** Ages of exactly $10$ and exactly $60$ qualify, so the test is closed on both sides; a strict comparison loses them.
- **Just outside** — the sample covers both directions: $9$ is too young (third case) and $62$, $65$ too old (first and second).
- **Nobody eligible**: the count is $0$.
- **Everybody eligible**: the count is $N$.
- Only a tally is needed, so the ages need not be stored or sorted.

## Dry run

| ages | inside $[10, 60]$ | output |
|---|---|---:|
| $15, 23, 65$ | $15, 23$ | `2` |
| $15, 62, 16$ | $15, 16$ | `2` |
| $35, 9$ | $35$ | `1` |

Each row excludes someone for a different reason: too old in rows 1 and 2, too young in row 3.
