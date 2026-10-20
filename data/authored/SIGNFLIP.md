---
topic: Greedy
subtopic: Flip the largest magnitudes first
time: $O(N \log N)$ per test case
space: $O(N)$
---
Two freedoms compose here, and separating them makes the problem easy.

**The subsequence may drop anything.** So after the flips are decided, the best subsequence is simply "every positive element" — negatives and zeros are excluded at no cost. The empty subsequence is allowed, so the answer is never negative.

**The flips should target the most negative elements.** Turning $-v$ into $+v$ swings the achievable sum by $v$, since the element goes from excluded to contributing $v$. So each flip is worth the *magnitude* of the negative it fixes, and the greedy is to spend the $K$ flips on the largest magnitudes.

Flipping a positive is never useful — it would only remove it from the subsequence — and flipping fewer than $K$ times is allowed, so there is no obligation to use them all.

Putting it together: sum the positives, then add the magnitudes of the $K$ most negative values (or all of them, if fewer than $K$ negatives exist).

Sample case 1: positives give $6 + 2 = 8$; the two most negative are $-10$ and $-4$, adding $14$, for $22$. Note $-1$ is left unflipped — the flips go to the biggest magnitudes, not the first negatives encountered.

Sample case 2 has $K = 0$ and all negatives, so nothing can be fixed and the empty subsequence gives $0$ — not $-5$. Sample case 3 has no negatives at all, so the three available flips go unused and the answer is the full sum $6$.

Sorting ascending puts the most negative values first, making the $K$ flips a prefix. With the sum of $N$ reaching $10^6$, the sort is the dominant cost and bulk input reading matters.
