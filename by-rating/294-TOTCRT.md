# 294. Total Correct Submissions

> [`TOTCRT`](https://www.codechef.com/problems/TOTCRT) &middot; difficulty **1499** &middot; time limit **1.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Aggregating by key, then sorting |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Maps`, `Implementation` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Codechef challenges have three divisions. In one challenge, there are $N$ problems in each division, but some problems may be shared among multiple divisions. Each problem is uniquely identified by a *code* — a string containing only uppercase English letters. Each participant can only submit in one of the divisions.

Chef wants to find the number of correct solutions, in total among all $3$ divisions, for each problem. Given a list of $N$ problem codes with the numbers of correct solutions for each problem in each division, find the total number of correct solutions for each problem and sort them in non-decreasing order.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains a string $S_{3,i}$ followed by a space and an integer $C_{3,i}$ — the problem code and the number of correct solutions on the $i$-th problem in the third division.
- $N$ more lines follow. For each valid $i$, the $i$-th of these lines contains a string $S_{2,i}$ followed by a space and an integer $C_{2,i}$ — the problem code and the number of correct solutions on the $i$-th problem in the second division.
- Finally, $N$ more lines follow. For each valid $i$, the $i$-th of these lines contains a string $S_{1,i}$ followed by a space and an integer $C_{1,i}$ — the problem code and the number of correct solutions on the $i$-th problem in the first division.

**Output**
For each test case, let $P$ be the number of distinct problems; you should print $P$ space-separated integers — the number of solutions for each of these problems, sorted in non-decreasing order.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 2 \cdot 10^4$
- $1 \leq |S_{1,i}|, |S_{2,i}|, |S_{3,i}| \leq 8$ for each valid $i$
- $S_{1,i}, S_{2,i}, S_{3,i}$ contain only uppercase English letters for each valid $i$
- $1 \leq C_{1,i}, C_{2,i}, C_{3,i} \leq 5 \cdot 10^8$ for each valid $i$
- the problem codes in each division are pairwise distinct, but some problem codes may appear in multiple divisions
- the sum of $N$ over all test cases does not exceed $10^5$

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 2 \cdot 10^4$
- $1 \leq |S_{1,i}|, |S_{2,i}|, |S_{3,i}| \leq 8$ for each valid $i$
- $S_{1,i}, S_{2,i}, S_{3,i}$ contain only uppercase English letters for each valid $i$
- $1 \leq C_{1,i}, C_{2,i}, C_{3,i} \leq 5 \cdot 10^8$ for each valid $i$
- the problem codes in each division are pairwise distinct, but some problem codes may appear in multiple divisions
- the sum of $N$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
3
1
A 1
B 2
C 3
2
AA 1
AB 1
AB 1
AC 1
AC 1
AD 1
1
Z 100
Z 100
Z 100
```

**Sample output**

```
1 2 3
1 1 2 2
300
```

<details><summary>Explanation</summary>

**Example case 1:** There is only $1$ problem in each division and no problems are shared among divisions, so the total number of distinct problems is $3$ and the numbers of solutions are: $1$ for "A", $2$ for "B", $3$ for "C".

**Example case 2:** There are $2$ problems in each division and each pair of consecutive divisions shares $1$ problem, so the total number of distinct problems is $4$ and the numbers of solutions are: $1$ for "AA", $2$ for "AB", $2$ for "AC", $1$ for "AD". We need to sort them in non-decreasing order, so the final answer is $(1, 1, 2, 2)$.

**Example case 3:** There is only $1$ problem "Z" in the entire contest, shared among all divisions, and the number of solutions for it is $300$.

</details>

## Approach

Three blocks of $N$ lines each give a problem code and a solve count. A code may appear in **more than one division**, and those counts must be added together — so the structure is a dictionary keyed by code, accumulating counts.

After reading all $3N$ entries, the answer is the dictionary's values sorted non-decreasing. Note the output length is the number of **distinct** codes $P$, which can be anything from $N$ (every division shares the same problem set) to $3N$ (no sharing at all).

Two things to read carefully.

**The divisions arrive in reverse order** — third, then second, then first. Since the counts are simply summed, the order is irrelevant to the answer, but it is the sort of detail that matters if anything per-division were ever needed.

**$P$ is not printed**, only the sorted counts, space-separated on one line per test case.

The samples span the range. Case 1 has three distinct codes, one per division, so the output has $3N = 3$ values. Case 3 has the single code `Z` in all three divisions, collapsing to one value of $300$. Case 2 is the mixed case: `AB` and `AC` each appear twice while `AA` and `AD` appear once, giving `1 1 2 2`.

A `defaultdict(int)` keeps the accumulation to one pass. With $\sum N \leq 10^5$ there are up to $3 \times 10^5$ entries, so bulk input reading matters; the codes are at most $8$ uppercase letters, so hashing them is cheap.

## Solution

```python
import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        totals = defaultdict(int)
        # Three blocks of n entries; a code may appear in several divisions.
        for _ in range(3 * n):
            totals[data[pos]] += int(data[pos + 1])
            pos += 2
        out.append(" ".join(map(str, sorted(totals.values()))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

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

---

Same problem grouped by topic: [../docs/arrays/TOTCRT.md](../docs/arrays/TOTCRT.md)
