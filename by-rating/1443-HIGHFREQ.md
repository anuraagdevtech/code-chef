# 1443 &middot; High Frequency

> CodeChef problem code [`HIGHFREQ`](https://www.codechef.com/problems/HIGHFREQ) &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Halving the top frequency against the runner-up |
| **CodeChef category** | main |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/greedy/HIGHFREQ.md](../docs/greedy/HIGHFREQ.md)

## Question

Chef has an array $A$ of length $N$.

Let $F(A)$ denote the maximum frequency of any element present in the array.

For example:

- If $A = [1, 2, 3, 2, 2, 1]$, then $F(A) = 3$ since element $2$ has the highest frequency $ = 3$.
- If $A = [1, 2, 3, 3, 2, 1]$, then $F(A) = 2$ since highest frequency of any element is $2$.

Chef can perform the following operation **at most once**:

- Choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) $S$ of the array such that every element of $S$ is the same, say $x$. Then, choose an integer $y$ and replace every element in this subsequence with $y$.

For example, let $A = [1, 2, 2, 1, 2, 2]$. A few examples of the operation that Chef can perform are:
- $[1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]$
- $[1, \textcolor{red}{2}, 2, 1, \textcolor{red}{2, 2}] \to [1, \textcolor{blue}{19}, 2, 1, \textcolor{blue}{19, 19}]$
- $[\textcolor{red}{1}, 2, 2, 1, 2, 2] \to [\textcolor{blue}{2}, 2, 2, 1, 2, 2]$

Determine the **minimum** possible value of $F(A)$ Chef can get by performing the given operation at most once.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ denoting the length of array $A$.
    - The second line contains $N$ space-separated integers denoting the array $A$.

**Output**

For each test case, output the minimum value of $F(A)$ Chef can get if he performs the operation optimally.

## Constraints

- $1 \leq T \leq 5000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
4
1 2 1 2
5
1 1 1 1 1
6
1 2 2 1 2 2
```

**Sample output**

```
2
3
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef cannot reduce the value of $F(A)$ by performing any operation.

**Test case $2$:** Chef can perform the operation $[\textcolor{red}{1}, 1, \textcolor{red}{1}, 1, \textcolor{red}{1}] \to [\textcolor{blue}{2}, 1, \textcolor{blue}{2}, 1, \textcolor{blue}{2}]$.
The value of $F(A)$ in this case is $3$, which is the minimum possible.

**Test case $3$:** Chef can perform the operation $[1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]$. The value of $F(A)$ in this case is $2$, which is the minimum possible.

</details>

## Approach

Only the **most frequent** value is worth touching, and only by splitting it off to a *fresh* value. Retargeting occurrences onto a value already in the array raises that value's count, which can never help; and operating on anything other than the top value leaves the maximum where it was.

So let $c_1 \geq c_2$ be the two largest frequencies. Moving $t$ of the $c_1$ occurrences to an unused $y$ leaves frequencies $c_1 - t$ and $t$, so the new maximum is

$$\max(c_1 - t,\; t,\; c_2)$$

The first two terms are minimised by splitting as evenly as possible, $t = \lceil c_1 / 2 \rceil$, since one of them is at least the mean $c_1/2$ whatever $t$ is. The runner-up is untouched, giving

$$\text{answer} = \max\!\left(\left\lceil \frac{c_1}{2} \right\rceil,\; c_2\right)$$

(with $c_2 = 0$ when the array has only one distinct value). Note the operation is optional, and the formula never exceeds $c_1$, so "at most once" needs no separate case.

Which term wins is exactly what the samples separate. For $[1,1,1,1,1]$ there is no runner-up, so the halving is unobstructed: $\lceil 5/2 \rceil = 3$. For $[1,2,2,1,2,2]$ the top count $4$ halves to $2$, and the runner-up is also $2$, so they tie at $2$ — halving further would be pointless. And for $[1,2,1,2]$ the top count is only $2$, so halving gives $1$ but the runner-up $2$ dominates, leaving the answer unchanged at $2$: an array that is already balanced cannot be improved.

A `Counter` plus the two largest values via `most_common(2)` is all the implementation needs.

## Solution (Python)

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
        counts = Counter(data[pos + 1:pos + 1 + n]).most_common(2)
        pos += 1 + n
        top = counts[0][1]
        runner = counts[1][1] if len(counts) > 1 else 0
        # Split the leader as evenly as possible; the runner-up is untouched.
        half = (top + 1) // 2
        out.append(str(half if half > runner else runner))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
