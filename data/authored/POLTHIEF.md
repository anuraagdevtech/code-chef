---
topic: Basic Math
subtopic: Relative speed
time: $O(1)$ per test case
space: $O(1)$
---
The policeman starts at $X$ moving at $2$ units per second; the thief starts at $Y$ moving at $1$. The thief runs directly away, so the gap between them shrinks at the **relative speed**

$$2 - 1 = 1 \text{ unit per second}$$

The initial gap is $|X - Y|$, so the capture time is

$$\frac{|X - Y|}{1} = |X - Y|$$

The answer is simply the absolute difference.

Two things make this cleaner than it first looks. The absolute value handles both directions at once — the thief may start to the left or the right, and the coordinates may be negative, since $X, Y \in [-10^5, 10^5]$. Writing `x - y` without `abs` would return a negative time for half the inputs.

And the phrase "the thief will try to evade for as long as possible" is what fixes the relative speed at $1$ rather than $3$. If the thief ran *toward* the policeman the gap would close at $2 + 1 = 3$ and the time would be a third as long; fleeing is the thief's best play, so the worst case for the policeman is the answer. Reading the adversarial clause as a maximisation is the real content here.

The case $X = Y$ needs no special handling: the gap is zero and the answer is $0$, as sample case 3 shows.
