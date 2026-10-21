# 268. Approximately II

> [`APPROX2`](https://www.codechef.com/problems/APPROX2) &middot; difficulty **1471** &middot; time limit **1.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Two pointers, then counting by value |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Brute Force`, `Implementation` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array of **N** integers **a_1, a_2, ..., a_N** and an integer **K**. Find the number of such unordered pairs {**i**, **j**} that

- **i** ≠ **j**

- **|a_i + a_j - K|** is minimal possible

Output  the minimal possible value of **|a_i + a_j - K|** (where **i** ≠ **j**) and the number of such pairs for the given array and the integer **K**.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case consists of two space separated integers - **N** and **K** respectively.

The second line contains **N** single space separated integers - **a_1, a_2, ..., a_N** respectively.

**Output**

For each test case, output a single line containing two single space separated integers - the minimal possible value of **|a_i + a_j - K|** and the number of unordered pairs {**i**, **j**} for which this minimal difference is reached.

**Constraints**

- **1** ≤ **T** ≤ **50**

- **1** ≤ **a_i, K** ≤ **10^9**

- **N** = **2** - 31 point.

- **2** ≤ **N** ≤ **1000** - 69 points.

## Constraints

- 1 ≤ T ≤ 50
- 1 ≤ a_i, K ≤ 10^9
- N = 2 - 31 point.
- 2 ≤ N ≤ 1000 - 69 points.

## Sample

**Sample input**

```
1   
4 9
4 4 2 6
```

**Sample output**

```
1 4
```

<details><summary>Explanation</summary>

The minimal possible absolute difference of **1** can be obtained by taking the pairs of **a_1** and **a_2**, **a_1** and **a_4**, **a_2** and **a_4**, **a_3** and **a_4**.

</details>

## Approach

Two separate questions: what is the minimal $|a_i + a_j - K|$, and how many unordered pairs achieve it.

**Finding the minimum.** Sort, then sweep two pointers from the ends. At each step the sum $a_{lo} + a_{hi}$ is a candidate; if it falls short of $K$ advance $lo$ to increase it, otherwise retreat $hi$ to decrease it. Every step either raises or lowers the sum toward $K$, and the scan visits a sum closest to $K$ from each side, so the minimum $d$ is found in $O(N)$ after the sort.

**Counting the pairs.** Once $d$ is known, the qualifying sums are exactly $K - d$ and $K + d$ — and when $d = 0$ those coincide, so the two must not be double-counted. For a target sum $S$, tally values with a `Counter` and for each distinct $v$ pair it with $S - v$:

- $v < S - v$: add $\mathrm{cnt}[v] \cdot \mathrm{cnt}[S-v]$
- $v = S - v$: add $\binom{\mathrm{cnt}[v]}{2}$, since the two picks must be different *positions*

That second case is the one to get right. Sample input $[4,4,2,6]$ with $K=9$ gives $d = 1$; the sum $8$ is reached by $(2,6)$ **and** by the two $4$s paired with each other, and the sum $10$ by each $4$ with the $6$ — four pairs in all, matching the expected `1 4`.

Counting by value rather than by index is what keeps this fast. The direct double loop is $O(N^2)$, which at $N = 1000$ and $T = 50$ is $2.5 \times 10^7$ pair evaluations — fine in C, uncomfortably slow in Python.

## Solution

```python
import sys
from collections import Counter


def count_sum(freq, s):
    """Unordered pairs of distinct positions whose values sum to s."""
    total = 0
    for v, c in freq.items():
        w = s - v
        if w not in freq:
            continue
        if v < w:
            total += c * freq[w]
        elif v == w:
            total += c * (c - 1) // 2      # two different positions
    return total


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        lo, hi = 0, n - 1
        best = abs(a[0] + a[1] - k)
        while lo < hi:
            s = a[lo] + a[hi]
            best = min(best, abs(s - k))
            if s < k:
                lo += 1
            else:
                hi -= 1
        freq = Counter(a)
        pairs = count_sum(freq, k - best)
        if best:                           # k - best and k + best coincide at 0
            pairs += count_sum(freq, k + best)
        out.append(f"{best} {pairs}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/sorting/APPROX2.md](../docs/sorting/APPROX2.md)
