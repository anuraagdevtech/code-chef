# 352. Count Subarrays

> CodeChef problem code [`SUBINC`](https://www.codechef.com/problems/SUBINC) &middot; difficulty **1478** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting subarrays by maximal runs |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Given an array $A_1, A_2, ..., A_N$, count the number of subarrays of array $A$ which are non-decreasing.
A subarray $A[i, j]$, where $1 ≤ i ≤ j ≤ N$ is a sequence of integers ${A_i}$, $A_{i+1}$, ..., ${A_j}$.

A subarray $A[i, j]$ is non-decreasing if $A_i ≤ A_{i+1} ≤ A_{i+2} ≤ ... ≤ A_j$. You have to count the total number of such subarrays.

### Input

- The first line of input contains an integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$ denoting the size of array.

- The second line contains $N$ space-separated integers $A_1$, $A_2$, ..., $A_N$ denoting the elements of the array.

### Output

For each test case, output in a single line the required answer.

### Constraints

-   $1 ≤ T ≤ 5$
-   $1 ≤ N ≤ 10^5$
-   $1 ≤ A_i ≤ 10^9$

### Subtasks

-   **Subtask 1** (20 points) : $1 ≤ N ≤ 100$
-   **Subtask 2** (30 points) : $1 ≤ N ≤ 1000$
-   **Subtask 3** (50 points) : Original constraints

## Constraints

-   $1 ≤ T ≤ 5$
-   $1 ≤ N ≤ 10^5$
-   $1 ≤ A_i ≤ 10^9$

## Sample

**Sample input**

```
2
4
1 4 2 3
1
5
```

**Sample output**

```
6
1
```

<details><summary>Explanation</summary>

**Example case 1.**
All valid subarrays are $A[1, 1], A[1, 2], A[2, 2], A[3, 3], A[3, 4], A[4, 4]$.
Note that singleton subarrays are identically non-decreasing.

**Example case 2.**
Only single subarray $A[1, 1]$ is non-decreasing.

</details>

## Approach

A subarray is non-decreasing exactly when **every adjacent pair inside it** is non-decreasing, so the property is determined entirely by the positions where $A_i > A_{i+1}$. Those breaks cut the array into maximal non-decreasing runs, and a subarray is valid iff it lies wholly inside one run. A run of length $L$ contains

$$\binom{L+1}{2} = \frac{L(L+1)}{2}$$

subarrays, and summing over the runs gives the answer.

The one-pass form avoids even finding the runs explicitly. Let $r_i$ be the length of the longest non-decreasing stretch ending at $i$:

$$r_i = \begin{cases} r_{i-1} + 1 & A_i \geq A_{i-1} \\ 1 & \text{otherwise}\end{cases}$$

Then $r_i$ is precisely the number of valid subarrays *ending* at $i$ — their left endpoints are the last $r_i$ positions — so the total is $\sum_i r_i$. This is the same count regrouped by right endpoint instead of by run, and it needs no second pass.

Every single element is a valid subarray, so the answer is never below $N$; the second sample is that minimum, $N = 1$ giving $1$.

For $[1, 4, 2, 3]$ the running lengths are $1, 2, 1, 2$, summing to $6$. Equivalently the runs are $[1,4]$ and $[2,3]$, each contributing $\tfrac{2 \cdot 3}{2} = 3$.

The count reaches $\tfrac{N(N+1)}{2} \approx 5 \times 10^9$ for a fully sorted array, which overflows 32-bit arithmetic — C++ needs `long long` here, while Python is safe by default.

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
        total = 0
        run = 0
        prev = None
        for v in a:
            # run = subarrays ending here, which is the stretch length itself.
            run = run + 1 if prev is not None and v >= prev else 1
            total += run
            prev = v
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
