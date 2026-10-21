---
topic: Greedy
subtopic: Maximising a set size under a sum budget
time: $O(N \log N)$ per test case
space: $O(N)$
---
Each person has at most one parent and no cycles, so the parent relation is a **forest**. In a forest on $N$ nodes with $r$ components, exactly $N - r$ nodes have a parent, and $r \geq 1$. A liar may have any number of children, so give them none; then the children all come from the truth-tellers, whose child sets are disjoint. Hence for a set $S$ of truth-tellers,

$$\sum_{i \in S} A_i = N - r \;\leq\; N - 1$$

That bound is also sufficient: with the out-degrees summing to at most $N-1$ there are always enough unclaimed people to hand out, and assigning children top-down from fresh nodes never makes anyone their own ancestor. So the problem is exactly

$$\text{maximise } |S| \text{ subject to } \sum_{i \in S} A_i \leq N - 1$$

which is the classic "fit as many items as possible into a budget": sort $A$ ascending and take greedily until the budget is exhausted. Taking the smallest claims first is optimal by exchange — swapping any chosen claim for an unchosen smaller one never breaks the budget.

People claiming $A_i = 0$ are free and always truthful in the optimum, which is why sorting rather than any cleverer selection is enough.

The samples show the budget binding at different points. $[1,0]$ with budget $1$ fits both. $[1,1]$ with budget $1$ fits only one — note that *both* cannot be telling the truth even though each claim is individually plausible, because two people would need two children among only two people, forcing a cycle. $[2,0,1]$ with budget $2$ takes $0$ and $1$ for $2$. And $[2,3,1,2,3]$ with budget $4$ takes $1$ and $2$, stopping before the second $2$ would push the sum to $5$.

## Edge cases

- **The budget is $N-1$, not $N$.** Each person has at most one parent and nobody may be their own ancestor, so the structure is a forest with at least one root — meaning at most $N-1$ people have a parent, and the truth-tellers' claims must sum within that.
- **Liars impose no constraint at all**, since a liar may have any number of children — so the only question is how many claims fit inside the budget.
- **Sorting ascending is optimal**: to maximise the count under a sum budget, take the cheapest claims first, which is the standard exchange argument.
- **A claim of $0$ is free** and always truthful-compatible — the first and third rows each have one, and it costs nothing.
- **A single large claim can block everything after it** (the second row: two claims of $1$ with a budget of $1$, so only one fits).
- **The break is safe** because the sorted claims are non-decreasing: once one exceeds the remaining budget, so does every later one.
- **$A_i < N$ is guaranteed**, so no single claim is immediately impossible, though two may still conflict.

## Dry run

Fourth sample: $N = 5$, claims $2, 3, 1, 2, 3$ sorted to $1, 2, 2, 3, 3$, budget $4$.

| claim | fits in budget? | budget left | truth-tellers |
|---:|:---:|---:|---:|
| 1 | yes | 3 | 1 |
| 2 | yes | 1 | 2 |
| 2 | **no** | — | 2 |

Output `2`. Three children across two parents leaves two childless people, consistent with a forest on five nodes.
