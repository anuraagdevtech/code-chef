# 405. Concat Sort

> CodeChef problem code [`CONCATSORT`](https://www.codechef.com/problems/CONCATSORT) &middot; difficulty **1637** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Counting descents in the sorted order's position sequence |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

JJ has an array $A$. He can perform the following operation on $A$:
- Divide $A$ into two subsequences $P$ and $Q$ such that each $A_i$ belongs to either $P$ or $Q$.
- Set $A := P\ \texttt{concat}\ Q$

Here $\texttt{concat}$ denotes the concatenation operation. For e.g. $[2, 1, 5] \texttt{ concat } [4, 3] = [2, 1, 5, 4, 3]$.

Is it possible to make $A$ sorted in non-decreasing order after applying the above operation **at most once**?

Note: An array $X$ is a subsequence of an array $Y$ if $X$ can be obtained by deletion of several (possibly, zero or all) elements from $Y$.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the array $A$.

**Output**

For each test case, output `YES` if it is possible to make the array $A$ sorted after applying the given operation **at most once**. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
6
4 5 6 1 2 3
5
1 3 5 2 4
5
5 10 7 11 9
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** We can select $P = [1, 2, 3]$ and $Q = [4, 5, 6]$. Therefore $A$ will become $[1, 2, 3, 4, 5, 6]$ which is sorted.

**Test case $2$:** It can be proven that it is not possible to sort $A$ by using the given operation at most once.

**Test case $3$:** We can select $P = [5, 7, 9]$ and $Q = [10, 11]$. Therefore $A$ will become $[5, 7, 9, 10, 11]$ which is sorted.

</details>

## Approach

The result $P \,\|\, Q$ must be $\mathrm{sorted}(A)$, and $P$ comes entirely before $Q$, so for some split $k$ the array $P$ holds the $k$ smallest elements and $Q$ the rest. Each piece keeps its original relative order, so the question becomes: can the sorted order be cut into **two increasing runs of original positions**?

Stably sort $A$ and let $\mathrm{pos}[r]$ be the original index of the element of rank $r$. $P$ is a valid subsequence exactly when $\mathrm{pos}[0] < \cdots < \mathrm{pos}[k-1]$, and $Q$ exactly when $\mathrm{pos}[k] < \cdots < \mathrm{pos}[N-1]$. So every **descent** — an $r$ with $\mathrm{pos}[r] > \mathrm{pos}[r+1]$ — must fall at the cut, and there is only one cut:

$$\text{answer} = \text{YES} \iff \#\{\,r : \mathrm{pos}[r] > \mathrm{pos}[r+1]\,\} \leq 1$$

Zero descents means $A$ is already sorted (take $Q$ empty, which the "at most once" wording permits); one descent fixes $k$ uniquely. The sort must be **stable**, so equal values keep their original order and never manufacture a spurious descent.

The samples are one of each. $[4,5,6,1,2,3]$ gives $\mathrm{pos} = [3,4,5,0,1,2]$ with the single descent $5 > 0$, so splitting there works — $P = [1,2,3]$, $Q = [4,5,6]$. $[5,10,7,11,9]$ gives $\mathrm{pos} = [0,2,4,1,3]$, again one descent, so `YES` with $P = [5,7,9]$ and $Q = [10,11]$ — note the two subsequences interleave in $A$, which is allowed since they are subsequences rather than blocks. And $[1,3,5,2,4]$ gives $\mathrm{pos} = [0,3,1,4,2]$ with two descents, so one operation cannot suffice.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Stable sort, so equal values never create a spurious descent.
        order = sorted(range(n), key=a.__getitem__)
        descents = sum(order[r] > order[r + 1] for r in range(n - 1))
        out.append("YES" if descents <= 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The split is into two *subsequences*, so each keeps its original relative order** — meaning the sorted order's position sequence must break into a prefix and a suffix that are each increasing in position.
- **That is exactly "at most one descent"** in the position sequence: one cut point, so one place where the positions may drop.
- **Already sorted** gives zero descents and still answers `YES`, since the operation may be applied zero times (or with an empty $Q$).
- **Two descents are fatal** (the second row, $1,3,5,2,4$, whose position sequence $0,3,1,4,2$ drops twice) — no single concatenation can repair both.
- **A stable sort is required.** Equal values must keep their original order, or an arbitrary tie-break could invent a descent and reject a solvable case.
- **Sorting indices rather than values** is what makes the descent count meaningful; sorting the values alone loses the position information entirely.
- **Sum of $N \leq 2 \cdot 10^5$**: one sort and one pass.

## Dry run

Third sample: $A = 5, 10, 7, 11, 9$.

| rank | value | original position |
|---:|---:|---:|
| 1 | 5 | 0 |
| 2 | 7 | 2 |
| 3 | 9 | 4 |
| 4 | 10 | 1 |
| 5 | 11 | 3 |

Position sequence $0, 2, 4, 1, 3$ has one descent ($4 \to 1$), so `YES`: take $P = [5, 7, 9]$ and $Q = [10, 11]$.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#373 of 486): [../../by-rating/373-CONCATSORT.md](../../by-rating/373-CONCATSORT.md)
