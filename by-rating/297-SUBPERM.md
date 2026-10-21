# 297. Subarray permutations

> [`SUBPERM`](https://www.codechef.com/problems/SUBPERM) &middot; difficulty **1502** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Forcing every good subsegment to be a prefix |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

A permutation of length $N$ is an array of $N$ integers $P = [P_1, P_2, \dots, P_N]$ such that every integer from $1$ to $N$ (inclusive) appears in it exactly once. For example, $[2, 3, 4, 1]$ is a permutation of length $4$.

A subsegment of an array $A[L \dots R]=[A_L, A_{L+1}, \dots, A_{R}$] is called *good* if the subsegment is a permutation of length $(R-L+1)$. For example, the array $A = [2, 3, 1, 4, 2]$ contains $3$ good subsegments: $A[3 \dots 3] = [1],$ $A[1\dots 3]$ $= [2, 3, 1],$ $A[2 \dots 5]=[3,1,4,2]$.

You are given two integers $N$ and $K$. Find a permutation of length $N$ such that it contains exactly $K$ good subsegments. Print `-1` if no such permutation exists.

**Input**

- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first and only line of each test case contains two space-separated integers $N, K$.

**Output**

For each test case, output a single line containing the answer:

- If no permutation satisfies the given conditions, print `−1`.
- Otherwise, print $N$ space-separated integers $P_1, P_2, \dots, P_N$, denoting the elements of the permutation. If there are multiple answers, you can output any of them.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq N $
- Sum of $N$ over all test cases does not exceed $3\cdot10^5$.

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
1 1
3 2
4 1
5 3
```

**Sample output**

```
1
1 3 2 
-1
5 3 1 4 2
```

<details><summary>Explanation</summary>

**Test case $1$:** The only permutation of length $1$ is $[1]$, which contains one good subsegment $A[1 \dots 1]$.

**Test case $2$:** The permutation $[1, 3, 2]$ contains $2$ good subsegments: $A[1 \dots 1]$, $A[1 \dots 3]$.

**Test case $3$:** There is no way to construct a permutation of length $4$ which contains one good subsegment.

**Test case $4$:** The permutation $[5, 3, 1, 4, 2]$ contains $3$ good subsegments: $A[3 \dots 3], A[2 \dots 5], A[1 \dots 5]$. There are other permutations of length $5$ having $3$ good subsegments.

</details>

## Approach

The construction becomes easy after one normalising decision: **put $1$ first**. Every good subsegment must contain the value $1$, so with $1$ at position $1$ every good subsegment is a *prefix*. And a prefix of length $L$ holds $L$ distinct values from $1 \ldots N$, so it is good exactly when

$$\max(P_1, \ldots, P_L) = L$$

That turns "exactly $K$ good subsegments" into "exactly $K$ prefix maxima that equal their own length". Prefixes $1$ and $N$ always qualify, which settles the impossible case: for $N \geq 2$, $K = 1$ is unachievable, so print $-1$. ($N = 1$ has only $K = 1$.)

Otherwise pick the good lengths to be $1, 2, \ldots, K-1$ and $N$. To realise a jump from length $\ell$ to length $\ell'$, fill positions $\ell+1 \ldots \ell'$ with the values $\ell+1 \ldots \ell'$ **in decreasing order**. Then every intermediate prefix already contains the block's largest value $\ell'$ while being shorter than $\ell'$, so it is not good, and the prefix of length $\ell'$ is. Concretely:

$$P = [\,1,\, 2,\, \ldots,\, K-1,\ N,\, N-1,\, \ldots,\, K\,]$$

The leading run gives the jumps of size one, and the descending tail gives the single big jump to $N$. When $K = N$ the tail is a single element and this is the identity permutation, whose every prefix is good.

For $N = 3, K = 2$ this is `1 3 2`, matching the sample. For $N = 5, K = 3$ it gives `1 2 5 4 3`, whose good prefixes are lengths $1, 2, 5$; the sample's `5 3 1 4 2` has good segments at lengths $1, 4, 5$ instead — different positions, same count, and both accepted.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if n > 1 and k == 1:
            # Prefixes 1 and N are always good, so one is impossible.
            out.append("-1")
            continue
        # Unit jumps first, then one descending run so no prefix in between
        # has its maximum equal to its length.
        head = list(range(1, k))
        tail = list(range(n, k - 1, -1))
        out.append(" ".join(map(str, head + tail)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$K = 1$ is impossible for $N > 1$.** The singleton holding the value $1$ is always good, and so is the whole array — two distinct subsegments — so at least $2$ good subsegments exist. Only $N = 1$ can have exactly one.
- **Every good subsegment must contain the value $1$**, since a permutation of any length includes $1$. Placing $1$ at the front therefore makes every good subsegment a *prefix*, which is what reduces the construction to choosing which prefixes are good.
- **The leading run $1, 2, \dots, K-1$ gives $K-1$ good prefixes**, each being a permutation of $1 \dots j$.
- **The descending tail blocks every prefix in between.** Position $K$ holds $N$, so any prefix of length $j \geq K$ contains $N$ and can only be a permutation when $j = N$ — supplying exactly one more good prefix, for $K$ in total.
- **$N = 1$, $K = 1$** falls out of the same code: an empty head and a one-element tail.
- **This answer differs from the sample's** at $N = 5$, $K = 3$ (`1 2 5 4 3` against `5 3 1 4 2`); the statement asks for any such permutation, so a special judge counts the good subsegments.

## Dry run

$N = 5$, $K = 3$ gives $P = 1, 2, 5, 4, 3$.

| prefix | values | permutation of its length? |
|---|---|:---:|
| $[1]$ | $\{1\}$ | **yes** |
| $[1,2]$ | $\{1,2\}$ | **yes** |
| $[1,2,5]$ | $\{1,2,5\}$ | no |
| $[1,2,5,4]$ | $\{1,2,4,5\}$ | no |
| $[1,2,5,4,3]$ | $\{1,\dots,5\}$ | **yes** |

No non-prefix subsegment is good, since none of them contains the $1$. Total: `3`.

---

Same problem grouped by topic: [../docs/constructive/SUBPERM.md](../docs/constructive/SUBPERM.md)
