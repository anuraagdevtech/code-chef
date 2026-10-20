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
