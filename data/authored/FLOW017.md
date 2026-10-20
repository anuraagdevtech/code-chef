---
topic: Sorting
subtopic: Median of three
time: $O(1)$ per test case
space: $O(1)$
---
The second largest of three values is their **median**, so sorting the triple and taking the middle element answers it directly: `sorted((a, b, c))[1]`.

With only three elements the sort is constant time — there is no asymptotic cost to speak of — and it is far more readable than the nest of comparisons the problem seems to invite. Hand-written three-way comparison chains are a classic source of bugs precisely because there are six orderings to get right.

The duplicate case is what makes "second largest" ambiguous, and the problem resolves it the median way. If two values tie for largest, say $(7, 7, 3)$, the answer is $7$, not $3$. Sorting gives this for free: the list becomes $[3, 7, 7]$ and index $1$ holds $7$. A hand-rolled "find the max, remove it, find the max again" approach gets this right too, but an approach that excludes all copies of the maximum would answer $3$ and be wrong.

An alternative closed form avoids sorting entirely:

$$\text{median} = (A + B + C) - \max(A,B,C) - \min(A,B,C)$$

which is neat and also handles duplicates correctly, though it is arguably less obvious at a glance. Either is fine here; the sort states the intent most plainly.

Note that this problem has $T$ test cases on the first line, unlike several of its neighbours.
