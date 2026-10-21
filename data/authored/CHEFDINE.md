---
topic: Greedy
subtopic: Cheapest representative per group
time: $O(N \log N)$ per test case
space: $O(N)$
---
A complete meal needs at least $K$ **distinct** categories. Since ordering more dishes only adds time, the optimal meal takes exactly $K$ dishes, one from each of $K$ different categories.

Two greedy steps follow.

**Within a category, take the cheapest dish.** Any other choice from the same category costs at least as much and contributes the same category, so it is dominated.

**Across categories, take the $K$ cheapest representatives.** The per-category minima are independent, so sorting them and summing the smallest $K$ is optimal.

If fewer than $K$ distinct categories exist on the menu, no complete meal is possible and the answer is $-1$ — sample case 4, which has only two categories against $K = 3$.

Building the minima with a dictionary keyed by category is one pass; sorting the values and summing a prefix finishes it.

Sample case 2 is the one that exercises both steps. Category $1$ offers dishes costing $3$ and $4$, so its representative is $3$; category $2$ offers $0$ and $1$, giving $0$; category $3$ offers $3$ and $1$, giving $1$. With representatives $[3, 1, 0, 2, 4]$, the three cheapest sum to $0 + 1 + 2 = 3$.

Note that cooking times may be **zero** ($B_i \geq 0$), so a total of $0$ is legitimate and no positivity may be assumed. Taking the first dish seen per category rather than the minimum would answer $3 + 3 + 0 = 6$ here.

## Edge cases

- **A preparation time of zero is legal** ($B_i \geq 0$), so the per-category minimum must not use $0$ as an "unset" sentinel. The second row's answer depends on a genuine $0$.
- **Fewer than $K$ distinct categories** → $-1$. The fourth row has only two categories and needs three, even though it has five dishes.
- **Only the cheapest dish per category counts**, so a category full of slow dishes is represented by its one fast dish and nothing else — the second row's category $1$ offers $3$ and $4$ and contributes only $3$.
- **Exactly $K$ categories** → every one of them is used and the sort is a formality.
- **Category labels are compared as raw byte tokens**, which is safe because the input has no leading zeros, so each label has one spelling.
- **Sum of $N \leq 10^5$**: only the per-category minima are sorted, at most $\min(N, \text{distinct})$ values.

## Dry run

Second sample: $N = 8$, $K = 3$, categories $1,3,2,2,4,1,3,5$ with times $3,3,0,1,2,4,1,4$.

| category | times offered | cheapest |
|---:|---|---:|
| 1 | $3, 4$ | 3 |
| 2 | $0, 1$ | **0** |
| 3 | $3, 1$ | 1 |
| 4 | $2$ | 2 |
| 5 | $4$ | 4 |

Five categories available, so pick the three cheapest minima: $0 + 1 + 2 = $ `3`.
