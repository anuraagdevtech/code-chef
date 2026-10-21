---
topic: Geometry
subtopic: Pursuit curve by relative closing speed
time: $O(1)$ per test case
space: $O(1)$
---
This is the classic **three-dog (or mice) pursuit problem**. By symmetry the configuration stays an equilateral triangle at every instant — it merely shrinks and rotates — so the whole spiral can be analysed without touching the trajectory itself.

Consider one dog chasing its target. The chaser moves at speed $v$ straight toward the target, closing the gap at rate $v$. Meanwhile the target also moves at speed $v$, but along a direction making a $120°$ angle with the line joining them, so its motion changes the separation at rate $v\cos 120° = -v/2$ — it recedes at only half speed.

The net closing rate is therefore constant:

$$v - v\cos 120° = v\left(1 + \tfrac{1}{2}\right) = \tfrac{3}{2}v$$

Starting from separation $s$, the dogs meet after

$$t = \frac{s}{\tfrac{3}{2}v} = \frac{2s}{3v}$$

The spiral paths never need to be integrated — reducing the chase to a one-dimensional closing rate is the entire trick, and it works because the symmetry keeps that angle fixed at $120°$ forever.

Checking the first sample: $s=2, v=5$ gives $4/15 = 0.2666\overline{6}$.

The answer is judged with a tolerance of $10^{-6}$ absolute **or** relative, not by exact text. The second sample makes that visible: $s=1, v=10^9$ gives roughly $6.7 \times 10^{-10}$, and the published expected output is written as `0.0000001` — a different numeral entirely, but well inside the absolute tolerance. The repository therefore checks this one numerically rather than by string comparison.

## Edge cases

- **The symmetry is what makes this constant.** Three dogs at the corners of an equilateral triangle, each chasing the next, keep the configuration equilateral forever — so the chase angle stays at $120^\circ$ and the closing speed never changes.
- **The closing rate is $v - v\cos 120^\circ = 1.5v$**, giving a meeting time of $s / 1.5v = 2s/(3v)$ — no integration of the pursuit curve is needed.
- **The answer can be minute.** With $s = 1$ and $v = 10^9$ it is about $6.7 \times 10^{-10}$, so plenty of decimal places must be printed rather than a default six.
- **The sample's second answer is $10^{-7}$ while this prints $6.7 \times 10^{-10}$**, and both are accepted: the checker allows an absolute error of $10^{-6}$, and at this magnitude everything under the tolerance passes. That is why this problem needs a special judge rather than exact matching.
- **The division must be floating point** — integer division would floor to $0$ for every case where $2s < 3v$.
- **$s, v$ up to $10^9$** put the answer anywhere from $\sim\!10^{-9}$ to $\sim\!6.7 \times 10^8$.

## Dry run

| $s$ | $v$ | $2s/(3v)$ | printed |
|---:|---:|---|---|
| 2 | 5 | $4/15$ | `0.266666667` |
| 1 | $10^9$ | $2/(3 \times 10^9)$ | `0.000000001` |

Each dog's velocity has a component $v\cos 120^\circ = -v/2$ along the line to its target, so the gap of $s$ shrinks at $1.5v$ throughout.
