---
topic: Basic Math
subtopic: Triangular numbers and their inverse
time: $O(1)$ per test case
space: $O(1)$
---
After $t$ minutes the kiln has gained $1 + 2 + \cdots + t$ degrees, which is the $t$-th **triangular number**:

$$\sum_{i=1}^{t} i = \frac{t(t+1)}{2}$$

So the temperature is $Y + \frac{t(t+1)}{2}$, and melting begins at the smallest $t$ with

$$\frac{t(t+1)}{2} \geq X - Y$$

Writing $d = X - Y$ (positive, since $Y < X$ is guaranteed), this is a quadratic in $t$. Solving $t^2 + t - 2d \geq 0$ gives

$$t \geq \frac{-1 + \sqrt{1 + 8d}}{2}$$

Rather than taking a float square root and rounding — where a value landing a hair under an exact root silently gives $t - 1$ — the code computes `math.isqrt(8 * d + 1)` for an exact integer root, derives a candidate, and nudges it up while it falls short. The correction loop runs at most once or twice, so the whole thing stays $O(1)$.

A plain loop adding $1, 2, 3, \ldots$ until the target is reached would also be fast enough here, since $t$ never exceeds about $450$ when $d \leq 10^5$. But with $T$ up to $10^5$ that is $10^7$ iterations in Python, which is the kind of thing that turns a correct solution into a timeout. The closed form avoids the question.

The note that only end-of-minute temperatures count is what makes this a discrete search over integers rather than a continuous one. Checking sample 3: $d = 5$, and the triangular numbers run $1, 3, 6$ — so $t = 3$ is the first to reach it.
