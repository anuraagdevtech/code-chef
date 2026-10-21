---
topic: Sets
subtopic: Keep everything except the forbidden value
time: $O(N)$ per test case
space: $O(N)$
---
MEX here is the smallest **positive** integer missing, so MEX $= M$ says two things: every value in $1, \ldots, M-1$ must appear among the chosen elements, and $M$ must not.

The second condition is the only reason to discard anything. Every element other than $M$ is harmless — values above $M$ and repeats of values below $M$ cannot change the MEX, since the MEX is determined solely by which of $1, 2, \ldots$ are present. So the maximum selection is "everything except the copies of $M$":

$$\text{answer} = N - \mathrm{cnt}(M)$$

and that selection automatically satisfies the first condition, provided each of $1, \ldots, M-1$ occurs in $A$ at all. If any of them is missing, no selection can work and the answer is $-1$.

Note the problem's MEX starts from $1$, not $0$ — so $0$ never matters, and the constraint $A_i \geq 1$ means every element is a candidate value.

The sample has $A = [1,2,4]$ and $M = 3$. Both $1$ and $2$ are present and no element equals $3$, so all three elements are kept and the MEX of $\{1,2,4\}$ is indeed $3$. Had the array been $[1,2,3,4]$, the $3$ would have to go, leaving $3$ elements again — but from a longer array.

A set is enough for the presence test and a single counter for $\mathrm{cnt}(M)$, so one pass suffices. Checking $1 \ldots M-1$ costs $O(M) \leq O(N)$.
