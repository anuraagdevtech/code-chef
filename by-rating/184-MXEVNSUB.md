# 184. Maximum Length Even Subarray

> [`MXEVNSUB`](https://www.codechef.com/problems/MXEVNSUB) &middot; difficulty **1221** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Parity of a triangular number |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an integer $N$. Consider the sequence containing the integers $1, 2, \ldots, N$ in increasing order (each exactly once). Find the maximum length of its contiguous subsequence with an even sum.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**

For each test case, print a single line containing one integer --- the maximum length of a contiguous subsequence with even sum.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^4$

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
3
3
4
5
```

**Sample output**

```
3
4
4
```

<details><summary>Explanation</summary>

**Example case 1:** The optimal choice is to choose the entire sequence, since the sum of all its elements is $1 + 2 + 3 = 6$, which is even.

**Example case 3:** One of the optimal choices is to choose the subsequence $[1, 2, 3, 4]$, which has an even sum.

</details>

## Approach

The whole sequence $1, 2, \ldots, N$ sums to the triangular number

$$\frac{N(N+1)}{2}$$

If that total is **even**, the entire sequence qualifies and the answer is $N$ — no contiguous subsequence can be longer.

If it is **odd**, the full sequence is disqualified, so the best possible length is $N - 1$. And $N - 1$ is always achievable: dropping the leading $1$ changes the sum by an odd amount, flipping its parity to even, and the remainder $2, \ldots, N$ is still contiguous. So the answer is exactly $N - 1$.

The argument is tight in both directions — an upper bound of $N$ or $N-1$ from the parity, matched by an explicit construction — which is what makes this a one-line answer rather than a search.

Checking the samples: $N = 3$ sums to $6$, even, giving $3$. $N = 4$ sums to $10$, even, giving $4$. $N = 5$ sums to $15$, odd, giving $4$ — the subsequence $2,3,4,5$ summing to $14$.

Note that dropping the **last** element instead works only when $N$ is odd, since the sum must change by an odd amount. Dropping the leading $1$ always works, which is why it is the cleaner construction to reason about.

The edge case $N = 1$ gives an odd sum of $1$, so the answer is $0$ — the empty subsequence, whose sum of $0$ is even. The formula produces this without a guard.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        total = n * (n + 1) // 2
        # If the whole run is odd, dropping the leading 1 fixes the parity.
        out.append(str(n if total % 2 == 0 else n - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$N = 1$**: the total is $1$, odd, so the formula gives $0$ — correctly saying no non-empty contiguous block of $\{1\}$ has an even sum.
- **$N = 2$**: total $3$, odd, so the answer is $1$ (the single element $2$).
- **Dropping the leading $1$ is what fixes an odd total.** The sequence starts at $1$, so the suffix $2, \dots, N$ has a sum one less than the whole — flipping the parity — which is why $N - 1$ always works whenever $N$ does not. No shorter block is ever needed.
- **The answer depends only on $N \bmod 4$**, since the triangular number $N(N+1)/2$ is even for $N \equiv 0, 3$ and odd for $N \equiv 1, 2$.
- **$T$ up to $10^4$** with $N$ up to $10^4$: the closed form answers each case in constant time, with no per-case scan.

## Dry run

| $N$ | total $N(N+1)/2$ | parity | longest even block | output |
|---:|---:|---|---|---:|
| 1 | 1 | odd | — | `0` |
| 2 | 3 | odd | $\{2\}$ | `1` |
| 3 | 6 | even | $\{1,2,3\}$ | `3` |
| 4 | 10 | even | $\{1,2,3,4\}$ | `4` |
| 5 | 15 | odd | $\{2,3,4,5\}$ | `4` |
| 6 | 21 | odd | $\{2,\dots,6\}$ | `5` |

The sample covers $N = 3, 4, 5$; the pattern repeats with period $4$.

---

Same problem grouped by topic: [../docs/number-theory/MXEVNSUB.md](../docs/number-theory/MXEVNSUB.md)
