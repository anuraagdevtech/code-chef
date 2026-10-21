---
topic: Sorting
subtopic: Verifying a claimed sort
time: $O(N \log N)$ per test case
space: $O(N)$
---
$B$ is the sorted version of $A$ exactly when it is both **a rearrangement of $A$** and **in non-decreasing order**. Checking `sorted(A) == B` tests both at once: sorting canonicalises $A$'s multiset, and equality then forces $B$ to have the same elements in that same ascending order.

Both halves genuinely matter, and the samples separate them.

Case 1 has $A = [1,3,2,2]$ against $B = [1,2,3,4]$. $B$ *is* sorted, but it contains a $4$ that $A$ never had and is missing a $2$ — so it fails the multiset test. Checking only that $B$ is ascending would wrongly accept it.

Case 2 has $B = [1,2,3,2]$, which has the right multiset but is **not** ascending. Checking only the multiset — comparing `sorted(A)` against `sorted(B)`, say — would wrongly accept this one.

Case 3, $B = [1,2,2,3]$, satisfies both and is the only `yes`.

The single comparison avoids writing either check by hand. An $O(N)$ alternative is to verify $B$ is non-decreasing in one pass and compare frequency counts, but with $\sum N \leq 10^5$ the sort is comfortably fast and far harder to get wrong.

Comparing the raw byte tokens rather than parsed integers would be wrong here, since `007` and `7` denote the same value — so the tokens are converted before sorting.
