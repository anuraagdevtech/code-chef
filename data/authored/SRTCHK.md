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

## Edge cases

- **One comparison tests both conditions at once.** Checking `sorted(A) == B` verifies that $B$ holds the same multiset *and* that it is in non-decreasing order — two separate checks collapse into one.
- **A wrong multiset is caught** even when $B$ is itself sorted: the first sample row has $B = 1,2,3,4$ against an $A$ containing two $2$s.
- **An unsorted $B$ is caught** even with the right elements — the second row has the right values in the wrong order.
- **Duplicates must be preserved exactly**, which a set-based comparison would miss; the multiset is what matters.
- **Equal arrays answer `yes`** when $A$ is already sorted.
- **$n = 1$** is trivially `yes` when the two single elements match.
- **Sum of $n \leq 10^5$**: one sort per case, with both arrays read in the same pass.

## Dry run

| $A$ | $\mathrm{sorted}(A)$ | $B$ | equal? | output |
|---|---|---|:---:|---|
| $1,3,2,2$ | $1,2,2,3$ | $1,2,3,4$ | no (values) | `no` |
| $1,3,2,2$ | $1,2,2,3$ | $1,2,3,2$ | no (order) | `no` |
| $1,3,2,2$ | $1,2,2,3$ | $1,2,2,3$ | yes | `yes` |
