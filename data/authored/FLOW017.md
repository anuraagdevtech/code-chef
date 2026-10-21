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

## Edge cases

- **Two values tied for largest** ($10, 10, 5$): sorted gives $(5, 10, 10)$ and the middle is $10$. The "second largest" of a multiset with a repeated maximum is still that maximum, which a "largest strictly below the max" reading would get wrong.
- **All three equal** ($7, 7, 7$): the answer is $7$.
- **Two tied for smallest** ($3, 3, 9$): median $3$.
- **Already ascending / already descending** input: sorting makes the order irrelevant, so no case analysis is needed.
- Values go up to $10^6$ but only comparisons happen, so magnitude is immaterial.

## Dry run

| $A$ | $B$ | $C$ | sorted | middle | output |
|---:|---:|---:|---|---:|---|
| 120 | 11 | 400 | $(11, 120, 400)$ | $120$ | `120` |
| 10213 | 312 | 10 | $(10, 312, 10213)$ | $312$ | `312` |
| 10 | 3 | 450 | $(3, 10, 450)$ | $10$ | `10` |

Each row places the answer in a different input position, which is what makes sorting the clean move.
