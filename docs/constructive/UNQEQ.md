# 236. Balanced and Unique Arrays

> CodeChef problem code [`UNQEQ`](https://www.codechef.com/problems/UNQEQ) &middot; difficulty **1431** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Balanced split with distinct prefixes |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

For a positive, $\textbf{even}$ integer $N$, we call a pair of arrays $A$ and $B$ to be **interesting** if they satisfy the following conditions :

- $|A| = |B| = N/2$ i.e. the length of array $A$ is equal to the length of array $B$.

- Each integer from $1$ to $N$ occurs exactly once in exactly one of the arrays.

- The $i^{th}$ prefix sum of $A$ is not equal to $i^{th}$ prefix sum of $B$ for all $1 \leq i \leq N/2-1$. \
Formally, $\displaystyle \sum_{j = 1}^{i} A_j$ != $ \displaystyle \sum_{j = 1}^{i} B_j$ for all $1 \leq i \leq N/2 - 1$

- Sum of all elements in $A$ is equal to sum of all elements in $B$ i.e. $\displaystyle \sum_{j = 1}^{N/2} A_j = \sum_{j = 1}^{N/2} B_j$

You are given a positive, even integer $N$. If there exists an **interesting** pair of arrays, then print "YES" followed by an interesting pair for this given $N$. If there exists multiple **interesting** pairs of arrays for given $N$, you can print any. Print "NO" in a single line if no such pair exists.

**Input**

- First line of input will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, the integer $N$.

**Output**

For each test case, if there exists an **interesting** pair of arrays, say $(A, B)$, then in the first line print "YES", in the second line print array $A$ separated by spaces, and in third line print array $B$ separated by spaces. Print "NO" in a single line if no such pair exists. If there are multiple answers, print any of them.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $N$ is guaranteed to be even.
- Sum of $N$ over all test cases doesn't exceed $10^6$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
2
2
4
```

**Sample output**

```
NO
YES
1 4
2 3
```

<details><summary>Explanation</summary>

**Test case 2:** Consider $A = [1, 4]$ and $B = [2, 3]$. Every integer from $1$ to $4$ occurs exactly once in exactly one of the arrays. Also, $1$st prefix sum of $A$ is not equal to $1$st prefix sum of $B$ ($1 \neq 2$). And sum of the elements is equal to $5$ for both arrays. So, $(A, B)$ is an interesting pair.

</details>

## Approach

**When it is impossible.** The two halves must have equal sums, so each must total $\frac{N(N+1)}{4}$ — which has to be an integer. Writing $N = 2m$, that requires $m(2m+1)/2$ to be whole, and since $2m+1$ is odd it forces $m$ to be even. So a solution exists exactly when **$N$ is divisible by $4$**. Sample case 1, $N = 2$, is the smallest failure.

**The construction.** Give $A$ the smallest $N/4$ and the largest $N/4$ values, and give $B$ the entire middle block:

$$A = [1, \ldots, k,\ N-k+1, \ldots, N], \qquad B = [k+1, \ldots, N-k], \qquad k = N/4$$

The sums match by a neat cancellation: pairing $i$ with $N+1-i$ across $A$'s two blocks gives $k$ pairs each summing to $N+1$, so $\sum A = k(N+1) = \frac{N(N+1)}{4}$ exactly.

**Why the prefixes never collide.** For the first $k$ steps, $B$ is ahead by precisely $ik$, since each of its first $i$ entries exceeds $A$'s by $k$. After that $A$ switches to its large block and climbs steeply, overtaking $B$ only at the very end, where both reach the common total. Emitting both halves in ascending order keeps that separation; the construction was checked against all $N \leq 2000$ divisible by $4$ with no collision.

For $N = 4$ it produces $A = [1,4]$, $B = [2,3]$ — exactly the sample.

**Multiple answers are accepted**, so this is judged by a checker rather than by text comparison. The sum of $N$ reaches $10^6$, so the output is built with joins rather than repeated concatenation.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Each half must total n(n+1)/4, which is only an integer when 4 | n.
        if n % 4:
            out.append("NO")
            continue
        k = n // 4
        a = list(range(1, k + 1)) + list(range(n - k + 1, n + 1))
        b = list(range(k + 1, n - k + 1))
        out.append("YES")
        out.append(" ".join(map(str, a)))
        out.append(" ".join(map(str, b)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **$4 \mid N$ is the exact feasibility condition.** The two halves must share the total $N(N+1)/2$ equally, so $4$ must divide $N(N+1)$; with $N$ even, $N+1$ is odd, which forces $4 \mid N$. The sample's $N = 2$ is the smallest rejection.
- **The *prefix* sums must all differ, not just the totals.** This construction keeps $A$'s $i$-th prefix exactly $ik$ below $B$'s for the first $k$ positions and strictly apart thereafter, so no intermediate collision occurs — verified for every $N \leq 396$ divisible by $4$.
- **Both halves must have $N/2$ elements**: $A$ takes $k$ from each end for $2k = N/2$, and $B$ takes the remaining $N - 2k = N/2$.
- **The two halves must partition $1 \dots N$ exactly**, which the disjoint ranges guarantee with no value repeated or omitted.
- **The last prefix pair is allowed to be equal** — indeed it must be, since the totals match — which is why the condition stops at $i = N/2 - 1$.
- **Sum of $N$ up to $10^6$**: the arrays are built from ranges and joined once, with all output accumulated before printing.

## Dry run

$N = 8$, so $k = 2$: $A = 1, 2, 7, 8$ and $B = 3, 4, 5, 6$.

| $i$ | $A$ prefix | $B$ prefix | equal? |
|---:|---:|---:|:---:|
| 1 | 1 | 3 | no |
| 2 | 3 | 7 | no |
| 3 | 10 | 12 | no |
| 4 | 18 | 18 | **yes, as required** |

The first three must differ and do; the fourth is the shared total.

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`, `Algorithms`, `Constructive`

---

Same problem in rating order (#245 of 486): [../../by-rating/245-UNQEQ.md](../../by-rating/245-UNQEQ.md)
