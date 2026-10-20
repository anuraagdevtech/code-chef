---
topic: Basic Math
subtopic: Percentage comparison without division
time: $O(1)$ per test case
space: $O(1)$
---
There are $X$ schools of $Y$ students each, so $X \cdot Y$ students sat the exams and $Z$ of them passed. The question is whether the pass rate exceeded $50\%$:

$$\frac{Z}{X \cdot Y} > \frac{1}{2}$$

Cross-multiplying by the positive quantity $2 \cdot X \cdot Y$ turns this into

$$2Z > X \cdot Y$$

which is again pure integer arithmetic. Dividing instead would introduce a float and, worse, invite a rounding mistake exactly at the halfway point that the problem cares most about.

The *strictly* greater wording matters. When $2Z = X \cdot Y$ the pass rate is exactly $50\%$ and the answer is `NO`. Sample case 4 is built on this: $X=3, Y=6, Z=9$ gives $18$ students and $9$ passes, precisely half, so `NO`.

With $T$ up to $2 \cdot 10^4$ it is worth reading all input at once rather than calling `input()` per line; the arithmetic itself is free.
