---
topic: Sorting
subtopic: Counting descents in the sorted order's position sequence
time: $O(N \log N)$ per test case
space: $O(N)$
---
The result $P \,\|\, Q$ must be $\mathrm{sorted}(A)$, and $P$ comes entirely before $Q$, so for some split $k$ the array $P$ holds the $k$ smallest elements and $Q$ the rest. Each piece keeps its original relative order, so the question becomes: can the sorted order be cut into **two increasing runs of original positions**?

Stably sort $A$ and let $\mathrm{pos}[r]$ be the original index of the element of rank $r$. $P$ is a valid subsequence exactly when $\mathrm{pos}[0] < \cdots < \mathrm{pos}[k-1]$, and $Q$ exactly when $\mathrm{pos}[k] < \cdots < \mathrm{pos}[N-1]$. So every **descent** — an $r$ with $\mathrm{pos}[r] > \mathrm{pos}[r+1]$ — must fall at the cut, and there is only one cut:

$$\text{answer} = \text{YES} \iff \#\{\,r : \mathrm{pos}[r] > \mathrm{pos}[r+1]\,\} \leq 1$$

Zero descents means $A$ is already sorted (take $Q$ empty, which the "at most once" wording permits); one descent fixes $k$ uniquely. The sort must be **stable**, so equal values keep their original order and never manufacture a spurious descent.

The samples are one of each. $[4,5,6,1,2,3]$ gives $\mathrm{pos} = [3,4,5,0,1,2]$ with the single descent $5 > 0$, so splitting there works — $P = [1,2,3]$, $Q = [4,5,6]$. $[5,10,7,11,9]$ gives $\mathrm{pos} = [0,2,4,1,3]$, again one descent, so `YES` with $P = [5,7,9]$ and $Q = [10,11]$ — note the two subsequences interleave in $A$, which is allowed since they are subsequences rather than blocks. And $[1,3,5,2,4]$ gives $\mathrm{pos} = [0,3,1,4,2]$ with two descents, so one operation cannot suffice.
