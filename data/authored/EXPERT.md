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
