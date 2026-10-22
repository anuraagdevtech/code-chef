[&larr; 217. Appy and Contest](217-HMAPPY2.md) &middot; [Index](README.md) &middot; [219. Gift Shop and Coupon &rarr;](219-GFTSHP.md)

# 218. Maximize the Minimum

> [`MAXTHEMIN`](https://www.codechef.com/problems/MAXTHEMIN) &middot; difficulty **1358** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | The (K+1)-th smallest survives |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

JJ has an array $A$ of size $N$. He can perform the following operations on the array **at most** $K$ times:

- Set $A_i := A_{i + 1}$ where $1 \le i \le N - 1$
- Set $A_i := A_{i - 1}$ where $2 \le i \le N$

He wants to maximize the value of the minimum element of the array $A$. Formally, he wants to maximize the value of $\min\limits_{1 \le i \le N} A_i$.

Can you help him do so?

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $K$ - the size of the array $A$ and the maximum number of operations allowed respectively.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output the maximum value of the minimum element of the array $A$ that can be obtained after applying the given operation at most $K$ times.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $0 \le K \le 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
4
5 4
5 4 3 2 1
6 1
8 2 3 9 6 10
5 2
4 3 4 3 5
5 1000
4 3 4 3 5
```

**Sample output**

```
5
3
4
5
```

<details><summary>Explanation</summary>

**Test Case 1:** We can perform the following operations (in the following order):
- Set $A_2 := A_1$. Array $A$ becomes $[5, 5, 3, 2, 1]$
- Set $A_3 := A_2$. Array $A$ becomes $[5, 5, 5, 2, 1]$
- Set $A_4 := A_3$. Array $A$ becomes $[5, 5, 5, 5, 1]$
- Set $A_5 := A_4$. Array $A$ becomes $[5, 5, 5, 5, 5]$

Therefore the answer is $5$.

**Test Case 2:** We can perform the following operations (in the following order):
- Set $A_2 := A_3$. Array $A$ becomes $[8, 3, 3, 9, 6, 10]$

Therefore the answer is $3$.

**Test Case 3:** We can perform the following operations (in the following order):
- Set $A_2 := A_3$. Array $A$ becomes $[4, 4, 4, 3, 5]$
- Set $A_4 := A_3$. Array $A$ becomes $[4, 4, 4, 4, 5]$

Therefore the answer is $4$.

</details>

## Approach

Each operation overwrites one element with a neighbour's value, so **at most $K$ positions can be changed**. Whatever is not overwritten keeps its original value, and the final minimum is at most the smallest surviving original.

That gives an upper bound: however the $K$ operations are spent, at least $N - K$ originals remain, so the minimum cannot exceed the $(K+1)$-th smallest value — overwriting the $K$ smallest is the best one could hope for.

The bound is achievable. Values propagate along neighbours, so each of the $K$ smallest elements can be overwritten by a larger adjacent value, one operation apiece. Hence

$$\text{answer} = A_{(K)} \text{ in sorted order, i.e. } \mathrm{sorted}(A)[\min(K,\, N-1)]$$

The clamp handles the case $K \geq N - 1$, where enough operations exist to flood the whole array with its maximum. Sample cases 1 and 4 are both this: case 1 has exactly $K = N - 1 = 4$, and case 4 has $K$ far beyond it, both answering $\max(A) = 5$.

Without the clamp, `sorted(a)[k]` would index out of range on case 4.

Sample case 2 is the plain case: one operation removes the single smallest element $2$, leaving $3$ as the new minimum — the second smallest, which is `sorted(a)[1]`.

Sample case 3 removes both $3$s with two operations, promoting the minimum to $4$.

Sorting costs $O(N \log N)$; `heapq.nsmallest` or a partial selection would shave that to $O(N \log K)$, immaterial at these bounds.

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
        # At most k originals can be overwritten, so the (k+1)-th smallest
        # survives. With k >= n - 1 the whole array can be flooded.
        out.append(str(a[min(k, n - 1)]))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Each operation changes exactly one position**, so after $K$ of them at least $N - K$ originals survive — and the minimum can therefore never exceed the $(K+1)$-th smallest. That bound is also attainable, which is the whole proof.
- **$K \geq N - 1$** (the first and fourth rows): the whole array can be flooded with the maximum, so the answer is $\max(A)$.
- **$K$ may exceed $N$ by a wide margin** — the fourth row has $K = 1000$ with $N = 5$ — so the index must be clamped to $n - 1$ rather than trusted, or it raises `IndexError`.
- **$K = 0$**: nothing is touched and the answer is $\min(A)$.
- **Duplicates must each be overwritten.** The third row has two $3$s, and reaching $4$ costs exactly the $K = 2$ available; with $K = 1$ one $3$ would remain.
- **Copies come only from a neighbour**, so the value spreads one position per operation — the first sample's explanation walks the $5$ rightwards across four operations.

## Dry run

Third sample: $A = 4, 3, 4, 3, 5$ sorted to $3, 3, 4, 4, 5$, with $K = 2$.

| rank | value | must be overwritten? |
|---:|---:|---|
| 1 | 3 | yes (uses one operation) |
| 2 | 3 | yes (uses the second) |
| 3 | 4 | **survives** → the answer |
| 4 | 4 | survives |
| 5 | 5 | survives |

Index $\min(K, N-1) = 2$ (0-based) gives `4`.

---

Same problem grouped by topic: [../docs/sorting/MAXTHEMIN.md](../docs/sorting/MAXTHEMIN.md)
