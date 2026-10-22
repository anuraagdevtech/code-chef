---
topic: Heaps
subtopic: $k$ smallest pairwise sums
time: $O(K \log K + n \log n)$ per test case, where $n = \max q_i$
space: $O(n)$
---
The set of candidate sums is the full $K \times K$ grid $A_i + B_j$, which is up to $4 \times 10^8$ entries — far too many to materialise. But the queries ask only for ranks up to $10^4$, and that caps the work twice over.

First, **truncation**. The $n$-th smallest sum can only use the $n$ smallest values of $A$ and the $n$ smallest of $B$: if a sum used the $(n{+}1)$-th smallest $A$ value, then swapping in each of the $n$ smaller $A$ values with the same $B$ gives $n$ strictly smaller-or-equal sums, so its rank exceeds $n$. So sort both arrays and keep only the first $m = \min(K, n)$ of each.

Second, **a frontier heap**. With both arrays sorted, each row $i$ of the grid is increasing in $j$, so the grid is $m$ sorted lists and the task is a $k$-way merge. Seed a min-heap with the head of every row, $(A_i + B_0,\, i,\, 0)$; each pop yields the next smallest sum overall and is replaced by its row's successor $(A_i + B_{j+1},\, i,\, j+1)$.

Popping $n$ times produces the sorted prefix of sums, after which every query is an array index — so all $Q$ queries of a test case share one $O(n \log m)$ pass rather than each paying for its own.

The sample has $A = [1,2,3]$ and $B = [4,5,6]$, whose nine sums sort to $5, 6, 6, 7, 7, 7, 8, 8, 9$; the $4$th is $7$. Note the repeats — rank counts a multiset, so $(1,6)$, $(2,5)$ and $(3,4)$ all occupy their own rank rather than collapsing into one.

Values reach $10^{18}$, so the sums reach $2 \times 10^{18}$; Python's unbounded integers handle this, but in C++ this needs `unsigned long long` or care with `long long`.

## Edge cases

- **The sums form $K$ sorted rows**, one per element of $A$, each already increasing along $B$ — so a $K$-way merge with one heap entry per row yields them in order without materialising $K^2$ sums.
- **Only the first $\max q_i$ values of each array matter**, since a rank at most $n$ can never use the $(n{+}1)$-th smallest of either side. Truncating both arrays to that length is what keeps the heap small when $K$ far exceeds the largest query.
- **Both arrays must be sorted first**, or the rows are not monotone and the merge breaks.
- **Queries are answered from one shared prefix** of sums, computed to the largest query once rather than per query.
- **A query may repeat or come out of order**, which the stored list handles — the answers are indexed, not streamed.
- **Ranks are 1-based**, hence the `v - 1` lookup.
- **$A_i, B_i$ up to $10^{18}$** makes the sums reach $2 \times 10^{18}$, past 64-bit signed in the worst case and exact only in Python.

## Dry run

Sample: $A = 1, 2, 3$ and $B = 4, 5, 6$, with the query asking for the $4$th smallest sum.

| pop | sum | from | pushed next |
|---:|---:|---|---|
| 1 | 5 | $1+4$ | $1+5 = 6$ |
| 2 | 6 | $2+4$ | $2+5 = 7$ |
| 3 | 6 | $1+5$ | $1+6 = 7$ |
| 4 | **7** | $3+4$ | $3+5 = 8$ |

Output `7`.
