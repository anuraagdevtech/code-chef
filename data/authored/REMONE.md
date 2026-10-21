---
topic: Sorting
subtopic: Two candidate offsets, verified by a merge
time: $O(N \log N)$ per test case
space: $O(N)$
---
Sort both arrays. $B$ is $A$ with one element dropped and $X$ added to the rest, so sorting preserves the correspondence: $B_0$ must come from either $A_0$ or $A_1$ — the only two possibilities for "smallest surviving element", depending on whether $A_0$ was the one removed.

That gives just **two candidate offsets**:

$$X = B_0 - A_1 \qquad\text{or}\qquad X = B_0 - A_0$$

Since $A_1 > A_0$, the first is the smaller, so try it first and take the first that validates.

**Validation** is a two-pointer merge: walk $A$ and $B$ together, consuming a $B$ element whenever $A_i + X$ matches it and otherwise skipping that $A_i$. The candidate is valid when at most **one** skip occurs and all of $B$ is consumed.

The constraint $X > 0$ must also be checked — $B_0 - A_1$ can easily be zero or negative, as in sample case 3 where $A = [2,4]$ and $B = [3]$ give $3 - 4 = -1$, rejecting that candidate and leaving $X = 1$.

Sample case 1 shows the larger candidate winning: $A = [1,3,4,8]$ and $B = [8,11,15]$ reject $X = 5$ (which would need an $11$ that $A+5$ does not produce) and accept $X = 7$, dropping the $3$.

Sample case 2 takes the smaller candidate, $X = 2$, dropping the $4$ — and it is genuinely smaller than the alternative $X = 6$, which is why the order of trying matters for the "smallest $X$" requirement.

Values reach $2 \times 10^9$, so this needs **64-bit** arithmetic outside Python.
