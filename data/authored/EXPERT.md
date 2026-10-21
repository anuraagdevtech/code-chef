---
topic: Basic Math
subtopic: Percentage comparison without division
time: $O(1)$ per test case
space: $O(1)$
---
Munchy is an expert when the approval rate reaches half:

$$\frac{Y}{X} \geq \frac{1}{2}$$

Multiplying through by $2X$ — positive, since $X \geq 1$ — gives the integer test

$$2Y \geq X$$

This is the same cross-multiplication used in the Exams problem, but with one important difference: here the bar is **at least** $50\%$, not *strictly greater*. So the comparison is `>=` and the exact-half case answers `YES`. Sample case 4 ($X = 2$, $Y = 1$) is exactly half and answers `YES`, whereas the corresponding tie in Exams answered `NO`.

That contrast is the real lesson. Two problems can share identical arithmetic and differ only in whether the boundary is inclusive, so the phrase "at least" versus "strictly greater" deserves as much attention as the formula itself.

The constraint $Y \le X$ is guaranteed, so there is no need to handle an approval count exceeding the submission count.

## Edge cases

- **Exactly half approved** ($X = 2$, $Y = 1$): $2Y = X$, and the requirement is "at least half", so the answer is `YES`. The comparison must be `>=` — this is the opposite convention to the strictly-greater percentage problems, and the sample tests it.
- **Everything approved** ($Y = X$): $2X \geq X$ holds for every $X \geq 1$, so always `YES`.
- **Just under half** ($X = 4$, $Y = 1$): $2 \geq 4$ fails, so `NO`.
- **Smallest input** ($X = Y = 1$): $2 \geq 1$, so `YES`.
- $Y \leq X$ is guaranteed, so there is no need to guard against more approvals than submissions.
- $X \leq 10^6$ makes $2Y$ at most $2 \times 10^6$, so nothing overflows even in fixed-width arithmetic.

## Dry run

| $X$ | $Y$ | $2Y$ | $2Y \geq X$ | output |
|---:|---:|---:|:---:|---|
| 5 | 3 | 6 | yes | `YES` |
| 1 | 1 | 2 | yes | `YES` |
| 4 | 1 | 2 | no | `NO` |
| 2 | 1 | 2 | yes (equality) | `YES` |

The last row is the tight case: exactly half still counts.
