# 308. Median of adjacent maximum numbers

> [`MXMEDIAN`](https://www.codechef.com/problems/MXMEDIAN) &middot; difficulty **1523** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Pairing extremes to lift the median |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array **A** of size **2 * N** consisting of positive integers, where **N** is an odd number. You can construct an array B from **A** as follows, B[i] = max(**A**[2 * i - 1], **A**[2 * i]), i.e. B array contains the maximum of adjacent pairs of array **A**. Assume that we use 1-based indexing throughout the problem.

You want to maximize the [median](https://en.wikipedia.org/wiki/Median) of the array B. For achieving that, you are allowed to permute the entries of **A**. Find out the maximum median of corresponding B array that you can get. Also, find out any permutation for which this maximum is achieved.

**Note**

Median of an array of size n, where n is odd, is the middle element of the array when it is sorted in non-decreasing order. Note that n being odd, the middle element will be unique, i.e. at index (n+1) / 2.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains an integer **N**.

The second line of each test case contains **2 * N** space separated integers denoting array **A**.

**Output**

For each test case, output two lines.

The first of which should contain an integer corresponding to maximum value of the median of array B that you can get.

In the second line, print **2 * N** integers in a single line denoting any permutation of **A** for which the maximum value of median of array B is achieved.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 50000

- 1 ≤ **A**_i ≤ 2 * N

**Subtasks**

- **Subtask #1** (25 points) : 1 ≤ N ≤ 3

- **Subtask #2** (75 points) : original constraints

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 50000
- 1 ≤ A_i ≤ 2 * N

## Sample

**Sample input**

```
3
1
1 2
3
1 2 3 4 5 6
3
1 3 3 3 2 2
```

**Sample output**

```
2
1 2
5
1 3 2 5 4 6
3
1 3 3 3 2 2
```

<details><summary>Explanation</summary>

**Example case 1.** There are only two possible permutations of **A**, for both of those B will be 2. The median of B is 2.

**Example case 2.** For following permutation of A: 1 3 2 5 4 6, the corresponding B will be: 3 5 6, whose median is 5, which is the maximum that you can achieve.

**Example case 3.** For A: 1 3 3 3 2 2, the corresponding B will be: 3, 3, 2. Its
median is 3, which is maximum that you can achieve.

</details>

## Approach

$B$ has $N$ entries with $N$ odd, so its median is both the $k$-th smallest and the $k$-th largest for $k = \frac{N+1}{2}$. The median is therefore at least $X$ exactly when **$k$ of the pairs have maximum at least $X$**, and each such pair needs its own element $\geq X$. So the median can never exceed the $k$-th largest element of $A$:

$$\text{answer} = a_{2N - k + 1} = a_{N + \frac{N+1}{2}} \quad (\text{1-indexed, } a \text{ sorted ascending})$$

That bound is attained by **pairing the extremes**: match the $k$ largest elements with the $k$ smallest, one each, and let the middle $2(N-k)$ elements pair up among themselves. The $k$ chosen pairs then each have maximum at least $a_{2N-k+1}$, so the $k$-th largest entry of $B$ is at least that — and by the bound, exactly that.

Pairing large with small is what makes the construction work: spending two large elements on one pair would waste one of them, since a pair contributes only its maximum. Each large element must carry its own pair.

The sample shows the answer is a value *of $A$*, not an average: $N = 3$ with $A = [1,\ldots,6]$ gives $k = 2$ and the $2$nd largest, $5$. Our pairing prints `1 5 2 6 3 4`, whose $B = [5,6,4]$ has median $5$; the sample's `1 3 2 5 4 6` gives $B = [3,5,6]$, also median $5$ — any optimal arrangement is accepted.

The third sample has repeats, $A = [1,3,3,3,2,2]$, and the $2$nd largest is $3$; here the input order already happens to be optimal, which is why the expected output echoes it unchanged.

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
        a = sorted(int(x) for x in data[pos + 1:pos + 1 + 2 * n])
        pos += 1 + 2 * n
        k = (n + 1) // 2
        out.append(str(a[2 * n - k]))
        # Each of the k largest carries its own pair, partnered by a smallest.
        order = []
        for j in range(k):
            order.append(a[j])
            order.append(a[2 * n - k + j])
        order.extend(a[k:2 * n - k])
        out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/sorting/MXMEDIAN.md](../docs/sorting/MXMEDIAN.md)
