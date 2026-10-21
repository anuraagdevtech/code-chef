---
topic: Basic Math
subtopic: Total minus the extremum, then compare
time: $O(1)$ per test case
space: $O(1)$
---
Each player's score is the sum of their **two highest** of three rolls, which is the same as dropping the lowest:

$$\text{score} = A_1 + A_2 + A_3 - \min(A_1, A_2, A_3)$$

Computing it this way avoids sorting or a top-two scan, and it handles ties for the lowest roll correctly — only one copy is dropped. Sample case 3 relies on that: Alice rolls $6,6,6$ and scores $12$, discarding exactly one six rather than all of them.

With both scores in hand the result is a three-way comparison: `Alice`, `Bob`, or `Tie`. The equality branch is required — sample case 3 ends level at $12$ apiece.

The input packs both players onto one line as six integers, with Alice's three first. Splitting them in the wrong place is the main hazard; sample case 2 would otherwise look winnable for Alice.

Working through case 2: Alice has $4,4,5$ for $13 - 4 = 9$; Bob has $6,4,1$ for $11 - 1 = 10$. Bob wins, even though his rolls include the lowest single die on the table — dropping it is exactly what the scoring rule lets him do.

## Edge cases

- **The totals mislead.** In the sample's second row Alice rolls $4, 4, 5$ for a total of $13$ against Bob's $6, 4, 1$ totalling $11$ — yet **Bob wins**, because dropping each player's lowest roll leaves $9$ against $10$. Comparing raw totals gives the wrong winner here, which is the whole point of the row.
- **A tie** ($12$ each in the third row): needs its own branch.
- **All three rolls equal** ($6, 6, 6$): one of the tied minima is dropped, giving $12$.
- **The lowest roll is discarded, not the highest** — inverting that flips most answers.
- With exactly three dice, "best two" is simply the total minus the single minimum, so no sorting is needed.

## Dry run

| Alice | total | $-\min$ | Bob | total | $-\min$ | output |
|---|---:|---:|---|---:|---:|---|
| $3, 2, 5$ | 10 | 8 | $6, 1, 1$ | 8 | 7 | `Alice` |
| $4, 4, 5$ | 13 | 9 | $6, 4, 1$ | 11 | 10 | `Bob` |
| $6, 6, 6$ | 18 | 12 | $6, 6, 1$ | 13 | 12 | `Tie` |

Row 2 reverses on the discard; row 3 ties despite very different totals.
