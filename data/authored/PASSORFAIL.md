---
topic: Basic Math
subtopic: Scoring with a penalty
time: $O(1)$ per test case
space: $O(1)$
---
Chef attempts all $N$ questions, getting $X$ right and therefore $N - X$ wrong. Correct answers pay $3$ and wrong ones cost $1$, so the score is

$$3X - (N - X) = 4X - N$$

and he passes when that reaches $P$.

The simplification to $4X - N$ is worth seeing. Each question answered correctly rather than incorrectly is a swing of $4$ marks — the $3$ gained plus the $1$ penalty avoided — against a baseline of $-N$ if everything were wrong. That reframing makes the arithmetic a single expression and explains why the coefficient is $4$ rather than $3$.

The negative-marking is the trap. Ignoring the penalty and testing $3X \geq P$ passes sample case 1 by luck but fails case 2: with $N = 5, X = 2$ the real score is $8 - 5 = 3$, which falls short of $P = 4$, whereas $3X = 6$ would wrongly pass.

Sample case 3 shows the score going negative: $X = 0$ on $4$ questions gives $-4$, which fails even against $P = 0$. So no clamping at zero is appropriate — the comparison must be done on the signed score.

The bar is "**at least** $P$", so the comparison is `>=` and scoring exactly $P$ passes.
