---
topic: Basic Math
subtopic: Strict inequality turned into a floor
time: $O(1)$ per test case
space: $O(1)$
---
Renting for $m$ months costs $mX$, and Chef wants that to stay **strictly** below the purchase price $Y$:

$$mX < Y$$

The largest integer $m$ satisfying a strict inequality is

$$m = \left\lceil \frac{Y}{X} \right\rceil - 1 = \left\lfloor \frac{Y - 1}{X} \right\rfloor$$

and the second form is the one to use — a single floor division, no ceiling helper needed.

The $-1$ inside the numerator is what encodes *strictly*. Plain $\lfloor Y/X \rfloor$ answers "how many months cost **at most** $Y$", which is off by one exactly when $X$ divides $Y$. Sample case 2 is that case: $X = Y = 5$ gives $\lfloor 5/5 \rfloor = 1$, but renting for one month costs exactly the purchase price and is not strictly cheaper, so the answer is $0$.

Sample case 1 confirms the non-dividing case: $Y = 12$ at $X = 5$ gives $\lfloor 11/5 \rfloor = 2$ months ($10 < 12$), while a third month would cost $15$ and lose.

The "output $0$ if Chef should not rent at all" instruction needs no separate branch — the formula already returns $0$ whenever $X \geq Y$, since $Y - 1 < X$ then.

With $X, Y$ up to $10^9$ the arithmetic stays well inside integer range, and Python has no limit regardless.

## Edge cases

- **$Y$ an exact multiple of $X$** ($X = Y = 5$): the answer is $0$, because $1 \times 5 < 5$ is false. The $-1$ in $(Y-1)//X$ is exactly what makes the inequality strict, and the sample's second row catches an implementation that drops it.
- **$Y < X$**: nothing fits, so $0$.
- **Largest inputs** ($10^9$): no overflow concern in Python, and the expression stays in integers throughout.
- Writing $\lfloor (Y-1)/X \rfloor$ rather than $\lfloor Y/X \rfloor$ is the whole content: the first counts multiples *strictly below* $Y$, the second includes $Y$ itself.

## Dry run

| $X$ | $Y$ | $Y - 1$ | $//\,X$ | check | output |
|---:|---:|---:|---:|---|---|
| 5 | 12 | 11 | 2 | $2 \times 5 = 10 < 12$ | `2` |
| 5 | 5 | 4 | 0 | $1 \times 5 = 5 \not< 5$ | `0` |
