# 385. Frequency Array Retrieval

> [`FREQARRRET`](https://www.codechef.com/problems/FREQARRRET) &middot; difficulty **1654** &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Lexicographic labelling of equal-frequency groups |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Sorting`, `Frequency Arrays`, `Greedy`, `Lexicographic Order` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Consider an array $A$ consisting of $N$ positive elements. The *frequency array* of $A$ is the array $B$ of size $N$ such that $B_i =$ *frequency* of element $A_i$ in $A$.

For example, if $A = [4, 7, 4, 11, 2, 7, 7]$, the *frequency array* $B = [2, 3, 2, 1, 1, 3, 3]$.

You have lost the array $A$, but fortunately you have the array $B$.
Your task is to construct the **lexicographically smallest** array $A$ such that:
- $1\le A_i \le 10^5$;
- The frequency array of $A$ is equal to $B$.

If no such array $A$ exists, print $-1$.

Note: Array $X$ is lexicographically smaller than array $Y$, if $X_i \lt Y_i$, where $i$ is the first index where $X$ and $Y$ differ.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the array.
    - The next line contains $N$ space-separated integers - $B_1, B_2, \ldots, B_N$, the frequency array.

**Output**

For each test case, output on a new line, $N$ space separated integers - $A_1, A_2, \ldots, A_N$, the **lexicographically smallest** array $A$. If no such array $A$ exists, print $-1$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^6$.

## Sample

**Sample input**

```
5
5
2 3 3 3 2
5
1 1 1 1 1
5
5 5 5 5 5
3
1 2 4
8
1 3 2 3 2 2 2 3
```

**Sample output**

```
1 2 2 2 1
1 2 3 4 5
1 1 1 1 1
-1
1 2 3 2 3 4 4 2
```

<details><summary>Explanation</summary>

**Test case $1$:** The lexicographically smallest array $A$ having the given frequency array $B$ is $A = [1, 2, 2, 2, 1]$. The element $A_1$ and $A_5$ have frequency $2$ while $A_2, A_3,$ and $A_4$ have frequency $3$.

**Test case $2$:** The lexicographically smallest array $A$ having the given frequency array $B$ is $A = [1, 2, 3, 4, 5]$. Each element in $A$ has frequency $1$.

**Test case $3$:** The lexicographically smallest array $A$ having the given frequency array $B$ is $A = [1, 1, 1, 1, 1]$. Each element in $A$ has frequency $5$.

**Test case $4$:** No possible array $A$ exists having the given frequency array.

</details>

## Approach

Elements sharing a value form a **group** whose size is that value's frequency, so every index with $B_i = f$ belongs to a group of exactly $f$ indices, all with the same $B$ value. Feasibility is therefore a divisibility check per frequency:

$$f \mid \#\{\,i : B_i = f\,\} \quad \text{for every } f$$

and if any class fails, print $-1$. (Sample 4 has a single index with $B_i = 2$, which cannot fill a group of two.)

For the lexicographically smallest array, note that only the *partition* into groups matters — the labels can then be renamed, and the smallest renaming assigns $1, 2, 3, \ldots$ in order of first appearance. So sweep left to right and, for each index, take the **smallest value available**: join the currently open group of its frequency if there is one, otherwise open a new group with the next unused label. Joining is always better, because it reuses an already-smaller label and a smaller value at the earliest differing position settles the comparison.

This never strands a partial group: within one frequency class, indices fill group after group in order, so each closes exactly when it reaches $f$ members. At most one group per frequency is open at a time, so the bookkeeping is a counter and a label per frequency.

Labels stay within bounds: the number of groups is at most $N \leq 10^5$, matching the $A_i \leq 10^5$ limit.

Sample 5, $B = [1,3,2,3,2,2,2,3]$, shows the interleaving: the lone $B_i = 1$ takes label $1$ and closes at once; the three $3$s share label $2$ across positions $2, 4, 8$; and the four $2$s split into label $3$ (positions $3, 5$) and label $4$ (positions $6, 7$), giving `1 2 3 2 3 4 4 2`.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        b = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        if any(c % f for f, c in Counter(b).items()):
            out.append("-1")
            continue
        label = 0
        open_label = {}        # frequency -> label of the group still filling
        filled = {}
        a = []
        for f in b:
            if f not in open_label:
                label += 1     # a fresh label is the smallest unused value
                open_label[f] = label
                filled[f] = 0
            a.append(open_label[f])
            filled[f] += 1
            if filled[f] == f:
                del open_label[f]
        out.append(" ".join(map(str, a)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Feasibility is a divisibility check.** All positions sharing a frequency $f$ must group into complete blocks of exactly $f$ equal values, so the count of such positions must be a multiple of $f$ — the fourth row fails because one position claims frequency $2$.
- **Lexicographic smallness comes from opening a fresh label only when needed.** The group for a frequency stays open until it has $f$ members; a new label is minted only when no open group of that frequency exists, and since labels are minted in increasing order, that is always the smallest usable value.
- **$f = 1$ closes immediately**, so a run of ones yields $1, 2, 3, \dots$ — the second row.
- **A single group covering everything** gives all the same label, as in the third row where five positions each claim frequency $5$.
- **Groups of different frequencies interleave freely**, which is why the open groups are tracked per frequency rather than as one pointer — the last row alternates between frequencies $2$ and $3$.
- **A group must be closed once full**, or later positions would wrongly join it and overshoot their claimed frequency.
- **$B_i \leq 10^5$ and the labels stay within $10^5$**, since at most $N$ labels are ever minted.

## Dry run

Last sample: $B = 1, 3, 2, 3, 2, 2, 2, 3$.

| position | $f$ | open group for $f$? | label | group now |
|---:|---:|---|---:|---|
| 1 | 1 | no → mint 1 | 1 | full, closed |
| 2 | 3 | no → mint 2 | 2 | 1 of 3 |
| 3 | 2 | no → mint 3 | 3 | 1 of 2 |
| 4 | 3 | yes (2) | 2 | 2 of 3 |
| 5 | 2 | yes (3) | 3 | full, closed |
| 6 | 2 | no → mint 4 | 4 | 1 of 2 |
| 7 | 2 | yes (4) | 4 | full, closed |
| 8 | 3 | yes (2) | 2 | full, closed |

Output `1 2 3 2 3 4 4 2`.

---

Same problem grouped by topic: [../docs/greedy/FREQARRRET.md](../docs/greedy/FREQARRRET.md)
