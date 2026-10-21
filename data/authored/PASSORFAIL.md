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

## Edge cases

- **The score exactly meets the cutoff** ($N=5$, $X=2$, $P=3$: score $3$): `PASS`, so the comparison is non-strict. The sample's first row.
- **Nothing correct** ($N=4$, $X=0$, $P=0$): the score is $-4$. **The score can go negative and must not be clamped** — clamping it to $0$ would wrongly report `PASS` against a cutoff of $0$. The sample's third row is exactly this trap.
- **Everything correct** ($X = N$): the score is $3N$, the maximum, and since $P \leq 3N$ it always passes.
- $3X - (N - X)$ collapses to $4X - N$, which keeps the whole thing in one integer expression.

## Dry run

| $N$ | $X$ | $P$ | correct $3X$ | wrong $-(N-X)$ | score $4X - N$ | $\geq P$? | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 5 | 2 | 3 | 6 | $-3$ | 3 | yes (equal) | `PASS` |
| 5 | 2 | 4 | 6 | $-3$ | 3 | no | `FAIL` |
| 4 | 0 | 0 | 0 | $-4$ | $-4$ | no | `FAIL` |

Row 3 is the negative score that a clamp would destroy.
