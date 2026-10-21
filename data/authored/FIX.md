---
topic: Greedy
subtopic: Forced slots, and the maximum everywhere else
time: $O(N)$ per test case
space: $O(N)$
---
Walk left to right and ask at each position whether $B_i$ is forced.

The prefix condition at $i$ requires every distinct value of $A_1 \ldots A_i$ to have appeared in $B_1 \ldots B_i$. Inductively $B_1 \ldots B_{i-1}$ already covers $A_1 \ldots A_{i-1}$, so the only possible gap is $A_i$ itself, and only when $A_i$ has not appeared in $B$ yet. In that case $B_i = A_i$ is forced. Otherwise $B_i$ is **free**, and since every element of $B$ must occur somewhere in $A$, the largest legal choice is $\max A$.

$$B_i = \begin{cases} A_i & A_i \notin \{B_1, \ldots, B_{i-1}\} \\ \max A & \text{otherwise}\end{cases}$$

Filling free slots with $\max A$ is safe as well as locally greedy: it only *adds* to the set of values already present in $B$, which can never turn a later free slot into a forced one. So the greedy choice never costs anything downstream, and taking the largest value at the earliest differing position settles the lexicographic comparison.

Note the test is against the values already in $B$, not against those seen in $A$. The two differ exactly when a free slot has already deposited $\max A$ before $\max A$'s own first appearance in $A$ — and then that appearance is free too.

In all three samples $B$ coincides with $A$, because no free slot arises before each new value. The mechanism shows up on an input like $A = [1,1,2]$, where the repeated $1$ frees position $2$ for a $2$, which in turn frees position $3$, giving $B = [1,2,2]$.
