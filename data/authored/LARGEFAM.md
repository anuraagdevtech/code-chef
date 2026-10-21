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
