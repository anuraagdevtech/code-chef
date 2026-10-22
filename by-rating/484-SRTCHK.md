[&larr; 483. Jon and Selina](483-SELINA.md) &middot; [Index](README.md) &middot; [485. Fair distribution &rarr;](485-SUBS.md)

# 484. Sort Checker

> [`SRTCHK`](https://www.codechef.com/problems/SRTCHK) &middot; difficulty **unrated** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Verifying a claimed sort |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

**Sort Checker**
You are given an array $A$ and an array $B$ of the same size. You have to print **yes** if $B$ is the sorted version of $A$ and **no** otherwise.

**Input**
- First line contains a single integer $T$, the number of testcases.
- The first line of each testcase contains a single integer $n$, the number of elements in the arrays.
- The second line of each testcase contains $n$ space separated integers denoting the array $A$.
- The third line of each testcase contains $n$ space separated integers denoting the array $B$.

**Output**
Print one line for each testcase, **yes** or **no**.

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \le n \le 10^5$
- The sum of $n$ over all test cases does not exceed $10^5$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le n \le 10^5$
- The sum of $n$ over all test cases does not exceed $10^5$.

## Sample

**Sample input**

```
3
4
1 3 2 2
1 2 3 4
4
1 3 2 2
1 2 3 2
4
1 3 2 2
1 2 2 3
```

**Sample output**

```
no
no
yes
```

<details><summary>Explanation</summary>

All three testcases have the same array $A$, and the sorted version of $A$ is $\{1, 2, 2, 3\}$.

Therefore only the third testcase contains **yes**, rest contain **no**.

</details>

## Approach

$B$ is the sorted version of $A$ exactly when it is both **a rearrangement of $A$** and **in non-decreasing order**. Checking `sorted(A) == B` tests both at once: sorting canonicalises $A$'s multiset, and equality then forces $B$ to have the same elements in that same ascending order.

Both halves genuinely matter, and the samples separate them.

Case 1 has $A = [1,3,2,2]$ against $B = [1,2,3,4]$. $B$ *is* sorted, but it contains a $4$ that $A$ never had and is missing a $2$ — so it fails the multiset test. Checking only that $B$ is ascending would wrongly accept it.

Case 2 has $B = [1,2,3,2]$, which has the right multiset but is **not** ascending. Checking only the multiset — comparing `sorted(A)` against `sorted(B)`, say — would wrongly accept this one.

Case 3, $B = [1,2,2,3]$, satisfies both and is the only `yes`.

The single comparison avoids writing either check by hand. An $O(N)$ alternative is to verify $B$ is non-decreasing in one pass and compare frequency counts, but with $\sum N \leq 10^5$ the sort is comfortably fast and far harder to get wrong.

Comparing the raw byte tokens rather than parsed integers would be wrong here, since `007` and `7` denote the same value — so the tokens are converted before sorting.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        b = [int(v) for v in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        # One comparison tests both the multiset and the ordering.
        out.append("yes" if sorted(a) == b else "no")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **One comparison tests both conditions at once.** Checking `sorted(A) == B` verifies that $B$ holds the same multiset *and* that it is in non-decreasing order — two separate checks collapse into one.
- **A wrong multiset is caught** even when $B$ is itself sorted: the first sample row has $B = 1,2,3,4$ against an $A$ containing two $2$s.
- **An unsorted $B$ is caught** even with the right elements — the second row has the right values in the wrong order.
- **Duplicates must be preserved exactly**, which a set-based comparison would miss; the multiset is what matters.
- **Equal arrays answer `yes`** when $A$ is already sorted.
- **$n = 1$** is trivially `yes` when the two single elements match.
- **Sum of $n \leq 10^5$**: one sort per case, with both arrays read in the same pass.

## Dry run

| $A$ | $\mathrm{sorted}(A)$ | $B$ | equal? | output |
|---|---|---|:---:|---|
| $1,3,2,2$ | $1,2,2,3$ | $1,2,3,4$ | no (values) | `no` |
| $1,3,2,2$ | $1,2,2,3$ | $1,2,3,2$ | no (order) | `no` |
| $1,3,2,2$ | $1,2,2,3$ | $1,2,2,3$ | yes | `yes` |

---

Same problem grouped by topic: [../docs/sorting/SRTCHK.md](../docs/sorting/SRTCHK.md)
