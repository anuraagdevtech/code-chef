---
topic: Greedy
subtopic: The smallest element as universal partner
time: $O(N)$ per test case
space: $O(1)$
---
To delete an element $x$, it must be paired with some $y$ where $x + y \leq K$. The **best possible partner is always the array's minimum** $m$, since no other value gives a smaller sum. So $x$ is deletable at all only if $x + m \leq K$.

That gives the test immediately. If even the **largest** element can be paired with the minimum,

$$\min(A) + \max(A) \leq K$$

then every element except $m$ can be deleted one at a time using $m$ as the partner, leaving $m$ alone. If instead $m + \max(A) > K$, the maximum can never be removed by anything — and neither can $m$ be removed while leaving the maximum behind, because that final pair would also exceed $K$. So the array is stuck with at least two elements.

The tempting shortcut is to test the two **smallest** elements, reasoning that the cheapest available pair is what matters. That is wrong, and the counterexample is instructive: $[1, 100, 200]$ with $K = 101$ passes $1 + 100 \leq 101$, yet $200$ can never be deleted and nothing can be paired with it, so the answer is `NO`. The binding constraint is the *largest* element, not the second smallest.

$N = 1$ is a separate case: the array is already a single element and no operation is needed, so the answer is `YES` regardless of $K$ — sample case 1.

Sample case 2, $[2,2,2]$ with $K = 3$, cannot even start, since $2 + 2 > 3$. Sample case 3 has $1 + 5 = 6 \leq 7$, so everything collapses onto the $1$.

## Edge cases

- **$N = 1$ needs its own branch.** The array is already a single element, so zero operations suffice; the general formula would test $2 A_1 \leq K$ and reject, for example, $A = [5]$ with $K = 3$. The sample's first row happens to pass either way, so it does not expose this.
- **The minimum is the universal partner**, so the *maximum* is the binding case. Checking the two smallest elements instead would accept arrays whose largest element can never be paired off.
- **The minimum is never removed** — it is kept as the survivor — so it stays available as a partner for every other element, which is what makes one comparison enough.
- **All equal** (the second row): $\min + \max = 2 A_1 = 4$, which exceeds $K = 3$ even though each element alone is well under it.
- **Exactly equal to $K$** → `YES`; the condition is non-strict.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass computing both extremes.

## Dry run

| $N$ | $K$ | array | min | max | $\min + \max$ | output |
|---:|---:|---|---:|---:|---:|---|
| 1 | 3 | $1$ | — | — | — (single element) | `YES` |
| 3 | 3 | $2,2,2$ | 2 | 2 | 4 | `NO` |
| 4 | 7 | $1,4,3,5$ | 1 | 5 | 6 | `YES` |

In row 3 the $1$ pairs with $5$, then $4$, then $3$, removing each in turn and surviving itself.
