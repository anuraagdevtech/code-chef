---
topic: Arrays
subtopic: Aggregating by key, then sorting
time: $O(N \log N)$ per test case
space: $O(N)$
---
Three blocks of $N$ lines each give a problem code and a solve count. A code may appear in **more than one division**, and those counts must be added together — so the structure is a dictionary keyed by code, accumulating counts.

After reading all $3N$ entries, the answer is the dictionary's values sorted non-decreasing. Note the output length is the number of **distinct** codes $P$, which can be anything from $N$ (every division shares the same problem set) to $3N$ (no sharing at all).

Two things to read carefully.

**The divisions arrive in reverse order** — third, then second, then first. Since the counts are simply summed, the order is irrelevant to the answer, but it is the sort of detail that matters if anything per-division were ever needed.

**$P$ is not printed**, only the sorted counts, space-separated on one line per test case.

The samples span the range. Case 1 has three distinct codes, one per division, so the output has $3N = 3$ values. Case 3 has the single code `Z` in all three divisions, collapsing to one value of $300$. Case 2 is the mixed case: `AB` and `AC` each appear twice while `AA` and `AD` appear once, giving `1 1 2 2`.

A `defaultdict(int)` keeps the accumulation to one pass. With $\sum N \leq 10^5$ there are up to $3 \times 10^5$ entries, so bulk input reading matters; the codes are at most $8$ uppercase letters, so hashing them is cheap.
