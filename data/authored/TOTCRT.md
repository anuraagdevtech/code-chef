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

## Edge cases

- **A problem code may appear in several divisions and its counts add** — that is the whole point of the problem. The second case has `AB` in divisions $1$ and $2$ and `AC` in divisions $2$ and $3$, each summing to $2$.
- **Codes are pairwise distinct within a division**, so no double-counting happens inside a single block and the three blocks can be read as one flat run of $3N$ pairs.
- **The division boundaries are irrelevant** once the totals are keyed by code, which is why the reading loop never tracks which block it is in.
- **The output is the sorted list of totals**, not keyed by code and not in input order.
- **The same code in all three divisions** (the third case, `Z` three times) collapses to one entry of $300$ — so the output can be shorter than $3N$ and even shorter than $N$.
- **$C_i$ up to $5 \times 10^8$ across three divisions** puts a total at $1.5 \times 10^9$, past 32-bit signed.
- **Codes are up to eight uppercase letters**, so the raw byte tokens serve directly as dictionary keys.

## Dry run

Second sample, $N = 2$.

| division | entries |
|---:|---|
| 1 | `AA 1`, `AB 1` |
| 2 | `AB 1`, `AC 1` |
| 3 | `AC 1`, `AD 1` |

| code | total |
|---|---:|
| `AA` | 1 |
| `AB` | 2 |
| `AC` | 2 |
| `AD` | 1 |

Sorted: `1 1 2 2`.
