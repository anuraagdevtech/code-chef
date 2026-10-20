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
