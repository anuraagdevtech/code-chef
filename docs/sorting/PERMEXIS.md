[&larr; 210. Simple Statistics](SIMPSTAT.md) &middot; [Index](../../README.md) &middot; [213. Maximize the Minimum &rarr;](MAXTHEMIN.md)

# 212. Watson asks Does Permutation Exist

> CodeChef problem code [`PERMEXIS`](https://www.codechef.com/problems/PERMEXIS) &middot; difficulty **1207** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Adjacent gaps in sorted order |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Watson gives an array **A** of **N** integers **A_1, A_2, ..., A_N** to Sherlock. He wants Sherlock to reorganize the array in a way such that no two adjacent numbers differ by more than 1.

Formally, if reorganized array is **B_1, B_2, ..., B_N**, then the condition that **| B_i - B_i + 1 | ≤ 1**, for all **1 ≤ i < N**(where **|x|** denotes the absolute value of **x**) should be met.
Sherlock is not sure that a solution exists, so he asks you.

**Input**

First line contains **T**, number of test cases. Each test case consists of **N** in one line followed by **N** integers in next line denoting **A_1, A_2, ..., A_N**.

**Output**

For each test case, output in one line **YES** or **NO** denoting if array **A** can be reorganized in required way or not.

**Constraints**

  - **1** ≤ **T** ≤ **100**

  - **1** ≤ **N** ≤ **10^5**

  - **1** ≤ **A_i** ≤  **10^9**

  - Sum of **N** over all test cases  ≤ **2*10^5**

## Constraints

- 1 ≤ T ≤ 100
  - 1 ≤ N ≤ 10^5
  - 1 ≤ A_i ≤  10^9
  - Sum of N over all test cases  ≤ 2*10^5

## Sample

**Sample input**

```
2
4
3 2 2 3 
2
1 5
```

**Sample output**

```
YES
NO
```

<details><summary>Explanation</summary>

Test case 1:

No need to reorganise.

Test case 2:

No possible way.

</details>

## Approach

A rearrangement with every adjacent pair differing by at most $1$ exists **if and only if the sorted array already has that property**.

One direction is immediate: if sorting works, a valid arrangement exists. The other is the interesting one. Suppose the sorted values have a gap larger than $1$ between some $a$ and the next distinct value $b$. Then the multiset splits into two groups — values $\leq a$ and values $\geq b$ — with no value in between. Any arrangement must at some point step from one group to the other, and that step is a jump of at least $b - a > 1$. So no arrangement can work.

Hence the test is simply: sort, then check every consecutive difference.

That argument is what makes the problem a two-liner rather than a search over permutations. It also shows the sorted order is *canonical* here: if any arrangement works, the sorted one does.

Sample case 1, $[3,2,2,3]$, sorts to $[2,2,3,3]$ with gaps $0, 1, 0$ — all within bounds, so `YES`. Sample case 2, $[1,5]$, has a single gap of $4$ and fails.

Note that duplicates are harmless, contributing gaps of $0$, and that $N = 1$ is vacuously fine with no adjacent pairs at all.

With the sum of $N$ reaching $2 \times 10^5$, the sort dominates and bulk input reading is worth having; `all(...)` over the consecutive pairs short-circuits on the first violation.

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
        a = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # If sorting cannot do it, no arrangement can: a gap > 1 splits the
        # values into two groups that no ordering can bridge.
        ok = all(a[i + 1] - a[i] <= 1 for i in range(n - 1))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Duplicates give a gap of $0$**, which is allowed — the first row is $2, 2, 3, 3$ and answers `YES`.
- **One oversized gap condemns the whole multiset.** If sorted order has $a_{i+1} - a_i \geq 2$, then every value up to $a_i$ is at most $a_i$ and every value from $a_{i+1}$ on is at least $a_{i+1}$, so whatever the arrangement, somewhere the sequence must cross that gap — sorted order is therefore optimal and testing it alone is sufficient.
- **$N = 1$**: no adjacent pair exists, so the `all` over an empty range answers `YES`.
- **Values up to $10^9$** but only differences matter, so no bucketing or counting array is needed.
- **The input line may have trailing whitespace** (the first sample row does), which token-based reading handles naturally.

## Dry run

| input | sorted | adjacent gaps | all $\leq 1$? | output |
|---|---|---|:---:|---|
| $3, 2, 2, 3$ | $2, 2, 3, 3$ | $0, 1, 0$ | yes | `YES` |
| $1, 5$ | $1, 5$ | $4$ | no | `NO` |

---

Same problem in rating order (#181 of 486): [../../by-rating/181-PERMEXIS.md](../../by-rating/181-PERMEXIS.md)
