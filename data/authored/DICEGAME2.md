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
