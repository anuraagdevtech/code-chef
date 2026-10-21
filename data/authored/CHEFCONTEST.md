---
topic: Basic Math
subtopic: Weighted penalty, then a three-way comparison
time: $O(1)$ per test case
space: $O(1)$
---
Penalty is the solve time plus ten minutes for each wrong submission:

$$\text{Chef} = X + 10P, \qquad \text{Chefina} = Y + 10Q$$

Lower penalty wins, with equality a draw.

Two things to keep straight. **Lower is better** — this is a penalty, not a score, so the comparison runs the opposite way to most "who wins" problems. And the wrong-submission counts are weighted by $10$; comparing $X$ against $Y$ alone, or adding $P$ and $Q$ unweighted, both fail.

Sample case 1 shows why the weighting matters: Chefina solved faster ($8$ against $10$) yet loses, because her three wrong submissions cost $30$ against Chef's $20$. A solution comparing only solve times would answer `Chefina`.

Sample case 3 is the opposite — Chefina's $21$ minutes beat Chef's $40$ by enough that his two wrong submissions are irrelevant.

Sample case 2 is the exact draw at $110$ apiece, so the equality branch is needed rather than folded into one of the inequalities.

The input order is $X, Y, P, Q$ — both times first, then both penalty counts — which is not the pairing the prose suggests, so it is easy to bind $P$ to Chefina by accident.

## Edge cases

- **A draw** ($110$ each): needs its own branch.
- **No wrong answers** ($Q = 0$): no penalty at all, which the third row relies on.
- **Raw time alone gives the wrong winner.** In the first row Chefina is faster on the clock ($8$ against $10$) and still loses, because her three wrong answers cost $30$ against Chef's $20$. Comparing $X$ with $Y$ and ignoring the penalty fails that row.
- **The lower total wins**, because it is a penalty — inverting the comparison flips every answer.
- **Input order is $X, Y, P, Q$**: both times first, then both wrong-answer counts, rather than being grouped per person.

## Dry run

| $X$ | $Y$ | $P$ | $Q$ | Chef $X + 10P$ | Chefina $Y + 10Q$ | lower | output |
|---:|---:|---:|---:|---:|---:|---|---|
| 10 | 8 | 2 | 3 | 30 | 38 | Chef | `Chef` |
| 10 | 10 | 10 | 10 | 110 | 110 | neither | `Draw` |
| 40 | 21 | 2 | 0 | 60 | 21 | Chefina | `Chefina` |

Row 1 is the one where the clock and the result disagree.
