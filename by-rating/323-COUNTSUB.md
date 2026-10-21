# 323. Unstable Subarray

> [`COUNTSUB`](https://www.codechef.com/problems/COUNTSUB) &middot; difficulty **1545** &middot; time limit **2.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | A telescoping sum, then counting equal pairs |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Maps`, `Simple Algos` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array $A$ of size $N$.

We define the function $f(l, r) = \sum_{i=l}^{r-1}(A_i-A_{i+1})$, where $1\le l \le r \le N$.
Note that $f(i, i)$ is defined as $0$.

A subarray $A[l, r]$ is considered *unstable* if $f(l,r) \neq (A_r-A_l)$.

Count the number of *unstable* subarrays in the array.

Note that the subarray $A[l, r]$ consists of $A_l, A_{(l+1)}, \ldots, A_{(r-1)}, A_r$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

**Output**

For each test case, output on a new line, the count of *unstable* subarrays.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

## Sample

**Sample input**

```
3
3
10 20 30
4
1 2 1 2
5
1 2 3 4 5
```

**Sample output**

```
3
4
10
```

<details><summary>Explanation</summary>

**Test case $1$:** There are $3$ unstable subarrays:
- $A[1, 2]$: Here $f(1, 2) = 10-20 = -10$ and $A_2 - A_1 = 10$.
- $A[1, 3]$: Here $f(1, 3) = (10-20) + (20-30) = -10-10 = -20$ and $A_3 - A_1 = 20$.
- $A[2, 3]$: Here $f(2, 3) = 20-30 = -10$ and $A_3 - A_2 = 10$.

**Test case $2$:** There are $4$ unstable subarrays:
- $A[1, 2]$: Here $f(1, 2) = 1-2 = -1$ and $A_2 - A_1 = 1$.
- $A[1, 4]$: Here $f(1, 4) = (1-2) + (2-1) + (1-2) = -1+1-1 = -1$ and $A_4 - A_1 = 1$.
- $A[2, 3]$: Here $f(2, 3) = 2-1 =  1$ and $A_3 - A_2 =-1$.
- $A[3, 4]$: Here $f(3, 4) = 1-2 = -1$ and $A_4 - A_3 = 1$.

</details>

## Approach

The definition of $f$ **telescopes**:

$$f(l, r) = \sum_{i=l}^{r-1} (A_i - A_{i+1}) = A_l - A_r$$

every interior term cancelling against its neighbour. So the instability test $f(l,r) \neq A_r - A_l$ becomes

$$A_l - A_r \neq A_r - A_l \quad\Longleftrightarrow\quad 2(A_l - A_r) \neq 0 \quad\Longleftrightarrow\quad A_l \neq A_r$$

The whole elaborate sum collapses to **comparing the two endpoints**.

So count the pairs $l \leq r$ with $A_l \neq A_r$. Singletons always have $A_l = A_r$ and are stable, so only $l < r$ can contribute:

$$\binom{N}{2} - \sum_{v} \binom{\mathrm{cnt}_v}{2}$$

— all unordered pairs of positions, minus those whose values coincide, tallied with a `Counter`.

Spotting the telescope is what turns an apparently $O(N^2)$ or even $O(N^3)$ definition into one linear pass. Enumerating subarrays at $\sum N = 5 \times 10^5$ would be hopeless.

Sample case 2, $[1,2,1,2]$, has $\binom{4}{2} = 6$ pairs, of which the two matching pairs $(1,1)$ and $(2,2)$ are stable, leaving $4$. Sample case 3 has all values distinct, so every one of the $\binom{5}{2} = 10$ pairs is unstable.

The count reaches about $1.25 \times 10^{10}$ at $N = 10^5$, which **overflows 32 bits**.

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
        counts = Counter(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # f(l, r) telescopes to A_l - A_r, so a subarray is unstable exactly
        # when its endpoints differ.
        same = sum(c * (c - 1) // 2 for c in counts.values())
        out.append(str(n * (n - 1) // 2 - same))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$f(l,r)$ telescopes to $A_l - A_r$**, so the instability test $f(l,r) \neq A_r - A_l$ becomes $A_l - A_r \neq A_r - A_l$, i.e. simply $A_l \neq A_r$. Everything between the endpoints is irrelevant.
- **Single-element subarrays are always stable.** $f(i,i)$ is defined as $0$ and $A_i - A_i$ is also $0$, which is why the count runs over $l < r$ and the total is $N(N-1)/2$.
- **Counting the complement is easier**: subtract the pairs of equal-valued positions, $\sum \binom{c_v}{2}$, from the total.
- **All values equal** → $0$ unstable subarrays.
- **All values distinct** (the first and third rows) → every pair counts, giving $N(N-1)/2$.
- **Duplicates are counted per position, not per value.** The second row has two $1$s and two $2$s, removing one pair each from six.
- **Sum of $N \leq 5 \cdot 10^5$**: a `Counter` on raw byte tokens, with totals near $10^{10}$ at $N = 10^5$ — past 32-bit.

## Dry run

Second sample: $A = 1, 2, 1, 2$, so $N(N-1)/2 = 6$ subarrays with $l < r$.

| value | count | equal-endpoint pairs |
|---:|---:|---:|
| 1 | 2 | 1 (positions $1,3$) |
| 2 | 2 | 1 (positions $2,4$) |

Unstable $= 6 - 2 = $ `4`. The two excluded subarrays are $A[1,3]$ and $A[2,4]$.

---

Same problem grouped by topic: [../docs/arrays/COUNTSUB.md](../docs/arrays/COUNTSUB.md)
