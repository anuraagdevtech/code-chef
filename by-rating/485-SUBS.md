[&larr; 484. Sort Checker](484-SRTCHK.md) &middot; [Index](README.md) &middot; [486. Sort by swaps &rarr;](486-SWPSRT1.md)

# 485. Fair distribution

> [`SUBS`](https://www.codechef.com/problems/SUBS) &middot; difficulty **unrated** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Sliding a fixed-size window |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Given an array  $A_1, A_2, .., A_N$  of size $N$ and an integer $K$.
You want to choose $K$ elements from array $A$ such that difference between maximum and minimum element ( from chosen elements) is minimum.

**Input**
- The first line of input contains one integer $T$.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line of each test case contains $N$ space-separated integers $A_i$.

**Output**
For each test case, print a single line containing one integer —  difference between maximum and minimum element.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le K \le N$
- $0 \le A_i \le 10^9$
- Sum of $N$ over all test cases doesn't exceed $2*10^6$

**Subtasks**
**Subtask #1 (10 points):**
- $1 \le N \le 20$

**Subtask #2 (30 points):**
- $1 \le N \le 1000$

**Subtask #3 (60 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le K \le N$
- $0 \le A_i \le 10^9$
- Sum of $N$ over all test cases doesn't exceed $2*10^6$

## Sample

**Sample input**

```
3
4 3
1 2 4 7
4 2
2 4 1 7
5 4
1 5 44 20 40
```

**Sample output**

```
3
1
39
```

<details><summary>Explanation</summary>

**Example case 1:**
All possible ways of choosing are,
$(1,2,4) = 4-1 =3$
$(1,2,7) = 7-1 =6$
$(1,4,7) = 7-1 =6$
$(2,4,7) = 7-2 =5$ .
Hence answer is $3$

**Example case 2:**
All possible ways of choosing are,
$(2,4) = 4-2 = 2$
$(2,1) = 2-1 = 1$
$(2,7) = 7-2 = 5$
$(4,1) = 4-1 = 3$
$(4,7) = 7-4 = 2$
$(1,7) = 7-1 = 6$
Hence answer is $1$

**Example case 3:**
Optimal way to choose is  $( 5, 44, 20, 40) = 44-5 = 39$.

</details>

## Approach

The spread of a chosen set depends only on its largest and smallest members, so the middle elements are free. That means an optimal choice of $K$ elements can always be taken **contiguous in sorted order**: if two chosen values have an unchosen value between them, swapping it in never widens the spread.

So sort the array and slide a window of width $K$, taking the best:

$$\min_{0 \leq i \leq N-K} \bigl(A_{i+K-1} - A_i\bigr)$$

Sorting dominates at $O(N \log N)$; the sweep itself is linear with no extra storage.

The contiguity argument is what makes this cheap. Without it one might consider $\binom{N}{K}$ subsets, which is hopeless at $N = 10^5$.

Sample case 1, $[1,2,4,7]$ with $K = 3$, has windows $[1,2,4]$ spanning $3$ and $[2,4,7]$ spanning $5$ — so $3$. Note the best window is **not** the one containing the two closest elements in isolation; it is the tightest run of three.

Sample case 3, $[1,5,44,20,40]$ with $K = 4$, sorts to $[1,5,20,40,44]$ with both windows spanning $39$ — a tie, which needs no special handling.

Duplicates give a span of $0$ and are handled naturally. When $K = N$ there is a single window, the whole array, and when $K = 1$ every window has width $0$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # An optimal choice is contiguous once sorted, so slide a window.
        out.append(str(min(a[i + k - 1] - a[i] for i in range(n - k + 1))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **An optimal choice is contiguous once sorted.** If two chosen elements straddle an unchosen one, swapping it in can only shrink the spread — so sliding a window of size $K$ over the sorted array covers every candidate.
- **The spread of a window is its last element minus its first**, since the array is sorted — no per-window maximum or minimum is needed.
- **$K = N$ leaves one window**, giving the full spread of the array.
- **$K = 1$ gives $0$**, as a single element has no spread.
- **Duplicates can give $0$** when $K$ of them coincide, which the window finds without a special case.
- **The window count is $N - K + 1$**, which is at least $1$ since $K \leq N$ is guaranteed.
- **$A_i$ may be $0$**, and the values reach $10^9$, so the spread fits comfortably.
- **Sum of $N$ up to $2 \cdot 10^6$**: one sort per case and one linear sweep.

## Dry run

Third sample: $A = 1, 5, 44, 20, 40$ sorted to $1, 5, 20, 40, 44$, with $K = 4$.

| window | spread |
|---|---:|
| $1, 5, 20, 40$ | $40 - 1 = 39$ |
| $5, 20, 40, 44$ | $44 - 5 = 39$ |

Both tie, so the answer is `39`.

---

Same problem grouped by topic: [../docs/sorting/SUBS.md](../docs/sorting/SUBS.md)
