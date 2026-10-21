---
topic: Greedy
subtopic: Halving the top frequency against the runner-up
time: $O(N)$ per test case
space: $O(N)$
---
Only the **most frequent** value is worth touching, and only by splitting it off to a *fresh* value. Retargeting occurrences onto a value already in the array raises that value's count, which can never help; and operating on anything other than the top value leaves the maximum where it was.

So let $c_1 \geq c_2$ be the two largest frequencies. Moving $t$ of the $c_1$ occurrences to an unused $y$ leaves frequencies $c_1 - t$ and $t$, so the new maximum is

$$\max(c_1 - t,\; t,\; c_2)$$

The first two terms are minimised by splitting as evenly as possible, $t = \lceil c_1 / 2 \rceil$, since one of them is at least the mean $c_1/2$ whatever $t$ is. The runner-up is untouched, giving

$$\text{answer} = \max\!\left(\left\lceil \frac{c_1}{2} \right\rceil,\; c_2\right)$$

(with $c_2 = 0$ when the array has only one distinct value). Note the operation is optional, and the formula never exceeds $c_1$, so "at most once" needs no separate case.

Which term wins is exactly what the samples separate. For $[1,1,1,1,1]$ there is no runner-up, so the halving is unobstructed: $\lceil 5/2 \rceil = 3$. For $[1,2,2,1,2,2]$ the top count $4$ halves to $2$, and the runner-up is also $2$, so they tie at $2$ — halving further would be pointless. And for $[1,2,1,2]$ the top count is only $2$, so halving gives $1$ but the runner-up $2$ dominates, leaving the answer unchanged at $2$: an array that is already balanced cannot be improved.

A `Counter` plus the two largest values via `most_common(2)` is all the implementation needs.
