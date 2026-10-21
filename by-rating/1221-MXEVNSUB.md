# 1221 &middot; Maximum Length Even Subarray

> CodeChef problem code [`MXEVNSUB`](https://www.codechef.com/problems/MXEVNSUB) &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Parity of a triangular number |
| **CodeChef category** | main |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/MXEVNSUB.md](../docs/number-theory/MXEVNSUB.md)

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

## Solution (Python)

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

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
