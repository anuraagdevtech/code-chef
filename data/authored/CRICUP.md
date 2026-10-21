---
topic: Basic Math
subtopic: Absolute difference against a tolerance
time: $O(1)$ per test case
space: $O(1)$
---
The match is interesting when the skill gap is at most $D$:

$$|X - Y| \leq D$$

The absolute value matters because the problem never says which team is stronger. Writing `x - y <= d` would wrongly accept every case where $Y$ exceeds $X$, since a negative difference is always below the threshold — a bug that passes roughly half the tests and so looks almost right.

The comparison is inclusive: "less than or equal to $D$" means a gap of exactly $D$ still counts. Sample case 1 has a gap of $2$ against $D = 4$, comfortably inside; case 2 has the same gap of $2$ against $D = 1$ and fails.

Sample case 3 covers the degenerate end: equal skills give a gap of $0$, and with $D = 0$ the inclusive comparison is what makes it `YES`. Since $D$ may be $0$, a strict `<` would get this wrong.

The same `abs`-against-tolerance shape appears whenever a problem asks whether two quantities are "close enough", and keeping it as one expression avoids reasoning about which value is larger.

## Edge cases

- **Equal strengths with zero tolerance** ($X = Y = 5$, $D = 0$): the gap is $0$, which is within $0$, so `YES`. The sample's third row sits on this boundary.
- **The gap exactly equals $D$**: `YES`, since the comparison is non-strict.
- **Either team may be stronger.** The absolute value is essential — a one-sided $X - Y \leq D$ accepts every case where $X < Y$ regardless of how far apart they are.
- **Off by one** ($X = 5$, $Y = 3$, $D = 1$): a gap of $2$ against a tolerance of $1$, so `NO`. The sample's second row.

## Dry run

| $X$ | $Y$ | $|X - Y|$ | $D$ | within? | output |
|---:|---:|---:|---:|:---:|---|
| 5 | 3 | 2 | 4 | yes | `YES` |
| 5 | 3 | 2 | 1 | no | `NO` |
| 5 | 5 | 0 | 0 | yes (equal) | `YES` |
