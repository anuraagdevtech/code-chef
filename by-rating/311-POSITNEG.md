[&larr; 310. Guddu on a Date](310-KS2.md) &middot; [Index](README.md) &middot; [312. Monsters &rarr;](312-SPCP5.md)

# 311. Positive or Negative Subarrays

> [`POSITNEG`](https://www.codechef.com/problems/POSITNEG) &middot; difficulty **1526** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | One power of two dominates all the lower ones |
| **CodeChef tags** | `Algorithms`, `Mathematics`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Consider an array $A$ having length $N$ such that $A_i = 2^{i-1}$ for all $1 \le i \le N$.

You are given an integer array $B$ having length $N$ such that $B_i = +1$ or $B_i = -1$ for all $1 \le i \le N$.

We create another array $C$ of length $N$ such that $C_i = B_i \cdot A_i$

- Let the number of subarrays of $C$ having sum **strictly** greater than $0$ be $P$ and
- Let the number of subarrays of $C$ having sum **strictly** less than $0$ be $Q$

Determine the value of $|P - Q|$. (Here $|x|$ denotes the absolute value of $x$)

Note: An array $X$ is a subarray of an array $Y$ if $X$ can be obtained from $Y$ by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $B$.
- The second line of each test case contains $N$ space-separated integers $B_1, B_2, \dots, B_N$ denoting the array $B$.

**Output**

For each test case, output the absolute difference between the number of subarrays of $C$ having sum strictly greater than $0$ and the number of subarrays of $C$ having sum strictly less than $0$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $B_i = +1$ or $B_i = -1$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
4
4
1 -1 1 1
3
-1 -1 -1
2
1 -1
2
1 1
```

**Sample output**

```
6
6
1
3
```

<details><summary>Explanation</summary>

In the first test case:-
the given array $B$ is $[1, -1, 1, 1]$ and the given array  $A$ is $[1, 2, 4, 8]$,.
We need to create array $C$ by multiplying corresponding elements of $A$ and $B$.
Thus, $C = [1, -2, 4, 8]$.

The subarrays of the array $[1, -2, 4, 8]$ and their corresponding sum are:

$[1]$: sum $= 1$
$[1, -2]$: sum $= -1$
$[1, -2, 4]$: sum $= 3$
$[1, -2, 4, 8]$: sum $= 11$
$[-2]$: sum $= -2$
$[-2, 4]$: sum $= 2$
$[-2, 4, 8]$: sum $= 10$
$[4]$: sum $= 4$
$[4, 8]$: sum $= 12$
$[8]$: sum $= 8$

So, the number of subarrays having sum strictly greater than $0$ is $8$, and the number of subarrays having sum strictly less than $0$ is $2$. Therefore, the answer is $|8-2|=6$.

In the 4th test case:-
Given the array $A = [1, 2]$ and the array $B = [1, 1]$, we need to create an array $C$ by multiplying corresponding elements of $A$ and $B$. Thus, we have:

C=[1,2]

The subarrays of the array $C$ and their corresponding sum are:

$[1]$: sum $= 1$
$[2]$: sum $= 2$
$[1, 2]$: sum $= 3$

So, the number of subarrays having sum strictly greater than $0$ is $3$, and the number of subarrays having sum strictly less than $0$ is $0$. Therefore, the answer is $|3-0|=3$.

</details>

## Approach

Since $2^{k} > 2^{k-1} + 2^{k-2} + \cdots + 1$, the **largest-index term dominates** any subarray: in $C[l..r]$ the term $\pm 2^{r-1}$ outweighs everything before it combined. So

$$\mathrm{sign}\bigl(\textstyle\sum_{i=l}^{r} C_i\bigr) = B_r$$

The left endpoint is irrelevant, and no subarray sums to zero.

So every subarray ending at $r$ is positive when $B_r = +1$ and negative when $B_r = -1$ — and there are exactly $r$ such subarrays, one for each $l \in \{1, \ldots, r\}$. Therefore

$$P - Q = \sum_{r=1}^{N} B_r \cdot r$$

and the answer is its absolute value. One pass, no subarray enumeration — which matters, since there are $\binom{N+1}{2}$ of them.

Sample case 1, $B = [1,-1,1,1]$, gives $1 - 2 + 3 + 4 = 6$. Sample case 3, $B = [1,-1]$, gives $1 - 2 = -1$, so the answer is $1$ — the absolute value is what makes $P < Q$ harmless.

The dominance argument is the whole problem; recognising that the sign depends only on the *last* element is what collapses a quadratic count into a linear sum.

With $N$ up to $10^5$ the weighted sum reaches about $5 \times 10^9$, which **exceeds 32 bits** — worth noting outside Python.

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
        b = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # The top power of two decides the sign, so only B_r matters, and
        # there are r subarrays ending at r.
        total = sum(int(v) * (r + 1) for r, v in enumerate(b))
        out.append(str(abs(total)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The last term dominates the whole subarray.** Since $2^{r-1} > 2^{r-2} + \dots + 2^{l-1}$, the sign of $C_l + \dots + C_r$ is exactly the sign of $B_r$ — so only the right endpoint matters.
- **No subarray sums to zero**, which is why $P + Q$ covers every subarray and the signed count telescopes cleanly into $\sum_r B_r \cdot r$.
- **There are $r$ subarrays ending at position $r$**, so each $B_r$ is weighted by its own index — not by $1$, and not by the count of subarrays containing it.
- **All signs the same** (the second row, every $B_i = -1$) gives the full triangular total, $1 + 2 + 3 = 6$ in magnitude.
- **The answer is an absolute value**, so a $Q$ larger than $P$ is fine; the second and first rows both give $6$ with opposite signs inside.
- **Cancellation is possible**: $[1, -1]$ gives $1 - 2 = -1$, so the answer can be small even on a short array.
- **Sum of $N \leq 3 \cdot 10^5$** with totals near $5 \times 10^9$ at $N = 10^5$ — past 32-bit.

## Dry run

First sample: $B = +1, -1, +1, +1$, so $C = 1, -2, 4, 8$.

| $r$ | $B_r$ | subarrays ending at $r$ | contribution |
|---:|---:|---:|---:|
| 1 | $+1$ | 1 | $+1$ |
| 2 | $-1$ | 2 | $-2$ |
| 3 | $+1$ | 3 | $+3$ |
| 4 | $+1$ | 4 | $+4$ |

$P - Q = 6$, so the output is `6`. For instance $C_1 + C_2 = -1 < 0$, matching $B_2 = -1$.

---

Same problem grouped by topic: [../docs/bit-manipulation/POSITNEG.md](../docs/bit-manipulation/POSITNEG.md)
