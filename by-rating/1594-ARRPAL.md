# 1594 &middot; Yet Another Palindrome Problem

> CodeChef problem code [`ARRPAL`](https://www.codechef.com/problems/ARRPAL) &middot; time limit **1.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Prefix increments force a non-increasing profile |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/ARRPAL.md](../docs/arrays/ARRPAL.md)

## Question

Chef has an array $A$ of size $N$. He can perform the following operation on $A$:
- Select an $i$ $(1 \le i \le N)$ and for all $1 \le j \le i$, set $A_j := A_j + 1$ (i.e. add $1$ to every element in the prefix of length $i$).

Chef wants to convert $A$ to a *palindrome* by using the above operation **minimum** number of times. Can you help Chef?
If it is not possible to convert $A$ to a *palindrome*, output $-1$.

Note: An array is called *palindrome* if it reads the same backwards and forwards, for e.g. $[1, 4, 1]$ and $[7, 3, 3, 7]$ are palindromic arrays.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output the **minimum** number of operations required to convert $A$ to a palindromic array.

If it is not possible to do so, output $-1$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3 \cdot 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
3
4
4 2 2 4
5
5 4 3 2 1
4
1 2 3 4
```

**Sample output**

```
0
-1
3
```

<details><summary>Explanation</summary>

**Test case $1$:** The given array is already a palindrome.

**Test case $2$:** It can be proven that it is not possible to convert $A$ to a palindromic array using the given operation.

**Test case $3$:** We can perform the following operations:
- Select $i = 1$, $[1, 2, 3, 4] \rightarrow [2, 2, 3, 4]$
- Select $i = 2$, $[2, 2, 3, 4] \rightarrow [3, 3, 3, 4]$
- Select $i = 1$, $[3, 3, 3, 4] \rightarrow [4, 3, 3, 4]$

</details>

## Approach

Let $d_j$ be how many operations cover index $j$. Since every operation covers a **prefix**, an operation covering $j$ also covers everything before it, so

$$d_1 \geq d_2 \geq \cdots \geq d_N \geq 0$$

and the total number of operations is $d_1$ — every operation covers index $1$.

The final array is $A_j + d_j$, and the palindrome requirement pairs $j$ with $N+1-j$:

$$d_j - d_{N+1-j} = A_{N+1-j} - A_j =: \delta_j$$

Two conditions follow, and both are necessary.

**Each $\delta_j \geq 0$.** Because $j < N+1-j$ and $d$ is non-increasing, the left side cannot be negative. So the mirror element must already be at least as large — sample case 2, $[5,4,3,2,1]$, fails immediately with $\delta_1 = 1 - 5 < 0$.

**The $\delta_j$ must themselves be non-increasing.** Expanding $\delta_j - \delta_{j+1} = (d_j - d_{j+1}) + (d_{N-j} - d_{N+1-j})$ shows it is a sum of two non-negative terms.

When both hold, the construction is immediate: set $d_j = \delta_j$ on the first half and $d_j = 0$ on the second. That is non-increasing and satisfies every pairing, so the answer is

$$d_1 = \delta_1 = A_N - A_1$$

Sample case 3, $[1,2,3,4]$, has $\delta = (3, 1)$ — non-negative and non-increasing — giving $3$. Sample case 1 is already a palindrome with $\delta = (0,0)$, so zero operations.

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
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        ok = True
        prev = None
        for j in range(n // 2):
            # Prefix increments make the coverage non-increasing, so the
            # mirror gaps must be non-negative and non-increasing too.
            gap = a[n - 1 - j] - a[j]
            if gap < 0 or (prev is not None and gap > prev):
                ok = False
                break
            prev = gap
        out.append(str(a[n - 1] - a[0]) if ok else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
