# 393. Gcd Queries

> [`GCDQ`](https://www.codechef.com/problems/GCDQ) &middot; difficulty **1674** &middot; time limit **3.5s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Prefix and suffix GCD arrays |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log A + Q \log A)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array **A** of integers of size **N**. You will be given **Q** queries where each query is represented by two integers **L, R**. You have to find the [gcd](http://en.wikipedia.org/wiki/Greatest_common_divisor)(Greatest Common Divisor) of the array after excluding the part from range **L** to **R** inclusive (1 Based indexing). You are guaranteed that after excluding the part of the array
remaining array is non empty.

**Input**

- First line of input contains an integer **T** denoting number of test cases.

- For each test case, first line will contain two space separated integers **N, Q**.

-  Next line contains **N** space separated integers denoting array **A**.

- For next **Q** lines, each line will contain a query denoted by two space separated integers **L, R**.

**Output**

For each query, print a single integer representing the answer of that query.

**Constraints**

**Subtask #1: 40 points**

- **2 ≤ T, N ≤ 100, 1 ≤ Q ≤ N, 1 ≤ A[i] ≤ 10^5**

	- **1 ≤ L, R ≤ N and L ≤ R**

**Subtask #2: 60 points**

- **2 ≤ T, N ≤ 10^5, 1 ≤ Q ≤ N, 1 ≤ A[i] ≤ 10^5**

	- **1 ≤ L, R ≤ N and L ≤ R**

	-  Sum of **N** over all the test cases will be less than or equal to **10^6**.

**Warning : ** Large IO(input output), please use faster method for IO.

## Constraints

- $2 \leq T, N \leq 10^5$
- $1 \leq Q \leq N$
- $1 \leq A_i \leq 10^5$
- $1 \leq L \leq R \leq N$ and $L \leq R$
- the sum of $N$ over all test cases is at most $10^6$
- the array remaining after the exclusion is guaranteed non-empty
- the I/O is large, so buffered reading and writing is required

## Sample

**Sample input**

```
1
3 3
2 6 9
1 1
2 2
2 3
```

**Sample output**

```
3
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** The given array is $[2, 6, 9]$.
- Query $1$: On excluding the range $[1,1]$, the remaining elements are $[6, 9]$. The *gcd* of $6$ and $9$ is $3$.
- Query $2$: On excluding the range $[2,2]$, the remaining elements are $[2, 9]$. The *gcd* of $2$ and $9$ is $1$.
- Query $3$: On excluding the range $[2,3]$, the remaining elements are $[2]$. The *gcd* of $2$ is $2$.

</details>

## Approach

Excluding a contiguous block $[L,R]$ leaves a **prefix and a suffix**, so the answer is the GCD of two precomputable aggregates. GCD is associative and commutative, which is all a prefix-aggregate needs:

$$\mathrm{pre}[i] = \gcd(A_1, \ldots, A_i), \qquad \mathrm{suf}[i] = \gcd(A_i, \ldots, A_N)$$

and the query answer is $\gcd(\mathrm{pre}[L-1], \mathrm{suf}[R+1])$.

The boundaries need care rather than branches: define $\mathrm{pre}[0] = \mathrm{suf}[N+1] = 0$ and use $\gcd(0, x) = x$. That identity makes $0$ the neutral element for GCD, so a query that removes a true prefix or suffix falls out of the same expression — no special cases. The problem guarantees something survives, so both aggregates are never $0$ at once.

Both arrays build in one pass each, after which every query is a single `gcd` call. The alternative, a sparse table or segment tree, is unnecessary here: the excluded part being contiguous means the *kept* part is always exactly two end-anchored pieces.

With $A = [2, 6, 9]$: $\mathrm{pre} = [0, 2, 2, 1]$ and $\mathrm{suf} = [1, 3, 9, 0]$. Removing $[1,1]$ gives $\gcd(0, 3) = 3$; removing $[2,2]$ gives $\gcd(2, 9) = 1$; removing $[2,3]$ gives $\gcd(2, 0) = 2$ — the last two showing both boundary forms.

The statement's I/O warning is real with $\sum N$ up to $10^6$: read the whole stream at once and join the output.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        a = [int(x) for x in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        # gcd(0, x) == x makes 0 the identity, so the ends need no special case.
        pre = [0] * (n + 2)
        for i in range(n):
            pre[i + 1] = gcd(pre[i], a[i])
        suf = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            suf[i + 1] = gcd(suf[i + 2], a[i])
        for _ in range(q):
            l, r = int(data[pos]), int(data[pos + 1])
            pos += 2
            out.append(str(gcd(pre[l - 1], suf[r + 1])))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/prefix-sums/GCDQ.md](../docs/prefix-sums/GCDQ.md)
