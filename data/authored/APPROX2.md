---
topic: Sorting
subtopic: Two pointers, then counting by value
time: $O(N \log N)$ per test case
space: $O(N)$
---
Two separate questions: what is the minimal $|a_i + a_j - K|$, and how many unordered pairs achieve it.

**Finding the minimum.** Sort, then sweep two pointers from the ends. At each step the sum $a_{lo} + a_{hi}$ is a candidate; if it falls short of $K$ advance $lo$ to increase it, otherwise retreat $hi$ to decrease it. Every step either raises or lowers the sum toward $K$, and the scan visits a sum closest to $K$ from each side, so the minimum $d$ is found in $O(N)$ after the sort.

**Counting the pairs.** Once $d$ is known, the qualifying sums are exactly $K - d$ and $K + d$ — and when $d = 0$ those coincide, so the two must not be double-counted. For a target sum $S$, tally values with a `Counter` and for each distinct $v$ pair it with $S - v$:

- $v < S - v$: add $\mathrm{cnt}[v] \cdot \mathrm{cnt}[S-v]$
- $v = S - v$: add $\binom{\mathrm{cnt}[v]}{2}$, since the two picks must be different *positions*

That second case is the one to get right. Sample input $[4,4,2,6]$ with $K=9$ gives $d = 1$; the sum $8$ is reached by $(2,6)$ **and** by the two $4$s paired with each other, and the sum $10$ by each $4$ with the $6$ — four pairs in all, matching the expected `1 4`.

Counting by value rather than by index is what keeps this fast. The direct double loop is $O(N^2)$, which at $N = 1000$ and $T = 50$ is $2.5 \times 10^7$ pair evaluations — fine in C, uncomfortably slow in Python.
