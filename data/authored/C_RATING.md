---
topic: Basic Math
subtopic: Ceiling division with a clamp
time: $O(1)$ per test case
space: $O(1)$
---
Each win adds $8$ rating, so after $w$ wins Alice sits at $X + 8w$. She needs this to reach $Y$:

$$X + 8w \geq Y \quad\Longleftrightarrow\quad w \geq \frac{Y - X}{8}$$

Since $w$ must be a whole number of games, the answer is the ceiling of that bound:

$$w = \left\lceil \frac{Y - X}{8} \right\rceil$$

computed in integers as `(gap + 7) // 8`.

The constraints promise $X \leq Y$, so the gap is never negative — but writing `max(0, y - x)` costs nothing and makes the intent explicit. Sample case 1 is the zero-gap case: Alice is already at the target, so no wins are needed.

The three cases $Y = 17, 18, 19$ against $X = 10$ are a precise test of the ceiling. A gap of $7$ needs $1$ game (overshooting to $18$), a gap of exactly $8$ also needs $1$ (landing precisely on $18$), and a gap of $9$ tips over into $2$. A floor division would answer $0, 1, 1$ and fail the first and third.

Note that "greater than or **equal** to $Y$" is what lets the exact-multiple case stay at one game rather than two.

## Edge cases

- **Already at the target** ($X = Y$): zero wins needed, and the sample's first row checks it.
- **A gap of exactly $8$** ($10 \to 18$): one win, and the $+7$ must not make it two.
- **A gap of $9$** ($10 \to 19$): two wins, since one win still leaves a point short. Together with the previous row this is the boundary pair, and the sample has both.
- **A gap of $7$** ($10 \to 17$): one win overshoots, which is fine — the rating only has to reach the target, not land on it.
- $X \leq Y$ is guaranteed, so the clamp is belt and braces, but it keeps the expression correct if that bound ever loosened.

## Dry run

| $X$ | $Y$ | gap | gap $+ 7$ | $//\,8$ | output |
|---:|---:|---:|---:|---:|---|
| 10 | 10 | 0 | 7 | 0 | `0` |
| 10 | 17 | 7 | 14 | 1 | `1` |
| 10 | 18 | 8 | 15 | 1 | `1` |
| 10 | 19 | 9 | 16 | 2 | `2` |

Rows 3 and 4 are one rating point apart and differ by a whole win.
