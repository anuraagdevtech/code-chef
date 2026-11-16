---
topic: Greedy
subtopic: Valid total counts followed by lexicographic candidate elimination
time: $O(N\log N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If the total number of knights is $k$, person $i$ must be a knight exactly when $a_i\le k\le b_i$. Use a difference array to count how many intervals cover every $k$ from zero through $N$. A valid assignment corresponds exactly to a total satisfying `coverage[k] == k`.

To construct the lexicographically smallest assignment, maintain all currently possible totals in sorted order. At person $i$, choose zero if any possible total lies outside their interval; delete every candidate inside it. Otherwise every candidate forces one. Whether all candidates lie inside is decided from the minimum and maximum remaining candidates. A successor DSU skips deleted candidates, so each candidate is removed at most once. Binary search locates the first candidate in a deletion interval. Count the initial valid totals before applying this greedy filter.

## Edge cases

- Zero knights is a possible total.
- Interval endpoints are inclusive.
- The smallest valid total does not necessarily give the lexicographically smallest assignment.
- A valid assignment is guaranteed to exist.

## Dry run

For intervals `[1,4],[2,4],[3,4],[4,4]`, every total from zero to four is consistent. There are five assignments; total zero yields `0000`, which is lexicographically smallest.
