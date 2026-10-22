# 323. Sort by Adjacent Swaps

> CodeChef problem code [`ADJSRT`](https://www.codechef.com/problems/ADJSRT) &middot; difficulty **unrated** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Insertion sort performs exactly the inversions |
| **Time** | $O(n + \text{inversions})$ |
| **Space** | $O(n)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

**Sort by Adjacent Swaps**
You are given an array $A$ (of size $n$) and you can only perform the adjacent swaps on the array, i.e. you can choose
an index $i$ ($0 \leq i \leq n-2$) and swap the values present in $A_i$ and $A_{i+1}$.

Sort the array using **minimum** number of adjacent swap operations.

Note that there may be multiple possible outputs, you can print **any** of them.

**Input**
The first line contains a single integer $n$, the number of elements in the array

The second line contains $n$ space separated integers, the elements of the array

**Output**
In the first line print the number of swaps that your solution performs on the array, let this number be $m$

In the next line print $m$ space separated integers, each between $0$ and $n-2$ (inclusive), the $i^{th}$ integer denotes that
$A_i$ and $A_{i+1}$ are swapped.

Note that $m$ must be equal to the minimum number of adjacent swap operations required to sort the array.

**Constraints**
$1 \leq n \leq 10^5$

$-10^9 \leq A_i \leq 10^9$

It is guaranteed that for the given array, the minimum number of swaps required is no more than $10^5$

## Constraints

$1 \leq n \leq 10^5$
$-10^9 \leq A_i \leq 10^9$
It is guaranteed that for the given array, the minimum number of swaps required is no more than $10^5$

## Sample

**Sample input**

```
3
3 2 1
```

**Sample output**

```
3
0 1 0
```

<details><summary>Explanation</summary>

The first operation swaps the first two elements of the array ($A_0$ and $A_1$), so the array becomes $\{2, 3, 1\}$

The second operation swaps the second and third elements of the array, so the array becomes $\{2, 1, 3\}$

The third operation swaps the first two elements of the array, so the array becomes $\{1, 2, 3\}$

You can verify that it cannot be done in less than $3$ operations.

</details>

## Approach

Each adjacent swap changes the relative order of exactly **one** pair, so it can remove at most one inversion. A sorted array has none, so the minimum number of adjacent swaps is exactly the **inversion count** of the input.

**Insertion sort achieves that bound.** It only ever swaps a pair that is currently out of order, so every swap removes an inversion and none is wasted. Recording the left index of each swap as it happens produces the required sequence directly.

The complexity point matters here. Insertion sort is usually quoted as $O(n^2)$, but its real cost is $O(n + \text{inversions})$ — the comparisons are proportional to the swaps plus one per element. The problem guarantees at most $10^5$ inversions, so this runs in linear-ish time despite $n$ reaching $10^5$. Bubble sort, by contrast, would scan $O(n^2)$ times regardless of how few swaps it makes, and would time out.

Recording swaps **as they happen** is what makes the output valid: the indices refer to the array state at that moment, and replaying them in order reproduces the sort.

For the sample $[3,2,1]$ the swaps are at indices $0$, then $1$, then $0$ again — three swaps, matching the inversion count of $\binom{3}{2} = 3$ and the published answer exactly.

Equal elements are never swapped, since the comparison is strict, which keeps the count minimal — swapping equal neighbours would waste a move without removing an inversion.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    a = [int(v) for v in data[1:1 + n]]
    swaps = []
    # Insertion sort only swaps genuine inversions, so it hits the minimum.
    # Its real cost is O(n + inversions), not O(n^2).
    for i in range(1, n):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            swaps.append(j - 1)
            j -= 1
    sys.stdout.write(f"{len(swaps)}\n" + " ".join(map(str, swaps)) + "\n")


main()
```

## Complexity

- **Time:** $O(n + \text{inversions})$
- **Space:** $O(n)$

## Edge cases

- **Insertion sort performs exactly the inversions**, one adjacent swap each — and since every adjacent swap removes at most one inversion, that count is the minimum. So the algorithm is optimal by construction, not by accident.
- **Its real cost is $O(n + \text{inversions})$**, not $O(n^2)$: the inner loop runs only while a genuine inversion is found. The problem guarantees at most $10^5$ swaps, which is what makes this viable at $n = 10^5$.
- **The swap indices are reported as the left position** of each adjacent pair, matching the problem's $0 \le i \le n-2$ convention.
- **An already-sorted array yields zero swaps**, and the output is then the count followed by an empty line.
- **Equal elements are never swapped**, since the condition is a strict `>` — which keeps the count at the true inversion number rather than inflating it.
- **The order of the reported swaps matters**: they must be replayable in sequence, which the insertion order guarantees.
- **There is no test-case count**: the input is $n$ followed by the array.

## Dry run

Sample: $A = 3, 2, 1$.

| step | array before | swap at | array after |
|---:|---|---:|---|
| 1 | $3, 2, 1$ | 0 | $2, 3, 1$ |
| 2 | $2, 3, 1$ | 1 | $2, 1, 3$ |
| 3 | $2, 1, 3$ | 0 | $1, 2, 3$ |

Three swaps, which is exactly the inversion count of $3, 2, 1$. Output `3` then `0 1 0`.

---

Same problem in rating order (#477 of 486): [../../by-rating/477-ADJSRT.md](../../by-rating/477-ADJSRT.md)
