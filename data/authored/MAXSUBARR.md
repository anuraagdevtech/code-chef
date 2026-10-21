---
topic: Greedy
subtopic: Kadane plus a freely orderable block
time: $O(N + M)$ per test case
space: $O(N + M)$
---
The operations look restrictive, but two observations dissolve them.

First, **any element of $B$ can be made adjacent to $A$**. To use a middle element of $B$, peel the elements in front of it off and push them onto the *front* of $A$, then push the one you want onto the back. So the block of $B$-elements sitting immediately to the right of $A$ can be any subset of $B$, and the unwanted ones are parked on the other side, outside the subarray.

Second, **order within that block is irrelevant** — only its sum enters the answer. So the best block is simply all the positive elements of $B$:

$$P = \sum_{b \in B,\ b > 0} b$$

A chosen subarray of the final array is then one of three shapes: entirely inside $A$; a suffix of $A$ extended rightwards into the appended block; or a prefix of $A$ extended leftwards into the prepended block. (Spanning both sides is covered, since all of $A$ is itself a suffix of $A$, and the positives can all go to one end.) Hence

$$\text{answer} = \max\bigl(\mathrm{kadane}(A),\ P + \max(0, \mathrm{maxSuffix}(A)),\ P + \max(0, \mathrm{maxPrefix}(A))\bigr)$$

The empty subarray is allowed, so every term is floored at $0$ and the answer is never negative. Taking $P$ alone — an empty suffix — covers the case where the $B$-block beats everything in $A$.

Sample 1 shows the suffix branch winning: $A = [3,26,-79,72,23]$ has best suffix $95$ and $P = 110$, giving $205$, well above Kadane's $95$. Sample 3 shows the prefix branch: the best prefix $10 - 5 + 14 = 19$ plus $P = 5$ gives $24$, beating the suffix route's $4 + 5$. And sample 2 has $B = [-97]$, so $P = 0$ and the answer is just $A$ itself — note that all $M$ operations still happen, but the unwanted element is parked where it cannot hurt.
