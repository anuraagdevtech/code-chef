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

## Edge cases

- **Both $K - \text{best}$ and $K + \text{best}$ must be counted**, since the closest achievable sum can lie on either side of $K$. The sample has two pairs summing to $8$ and two summing to $10$, and reporting only one side gives $2$ instead of $4$.
- **When the best difference is $0$ the two targets coincide**, so the second count must be skipped or every pair is counted twice — the `if best:` guard.
- **Pairs are unordered and use distinct positions**, so a value paired with itself contributes $\binom{c}{2}$ rather than $c^2$. The two $4$s in the sample give exactly one pair.
- **Duplicates must be counted by frequency**, not by scanning positions, which is what keeps the counting pass linear in the number of distinct values.
- **The two-pointer sweep finds the best difference but not the count**, which is why a separate frequency pass follows; trying to count during the sweep misses pairs the pointers skip over.
- **$N = 2$ is a scored subtask on its own**, and there the single pair is both the best and the only one.

## Dry run

Sample: $K = 9$, values $4, 4, 2, 6$ sorted to $2, 4, 4, 6$.

Two-pointer sweep:

| lo, hi | sum | $|{\text{sum}} - 9|$ | best | move |
|---|---:|---:|---:|---|
| 2, 6 | 8 | 1 | 1 | sum $< K$, lo$+$ |
| 4, 6 | 10 | 1 | 1 | sum $\geq K$, hi$-$ |
| 4, 4 | 8 | 1 | 1 | lo$+$, pointers meet |

Then count pairs at each target:

| target | pairs |
|---:|---|
| $9 - 1 = 8$ | $2{+}6$, and $4{+}4$ → 2 |
| $9 + 1 = 10$ | $4{+}6$ twice (two distinct $4$s) → 2 |

Output `1 4`.
