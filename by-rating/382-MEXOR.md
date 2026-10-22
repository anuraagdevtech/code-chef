# 382. MEX-OR

> [`MEXOR`](https://www.codechef.com/problems/MEXOR) &middot; difficulty **1650** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | OR of a prefix of the integers |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Logarithm` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

The *MEX* (minimum excluded) of an array is the smallest non-negative integer that does not belong to the array. For instance:

- The MEX of $[2, 2, 1]$ is $0$, because $0$ does not belong to the array.
- The MEX of $[3, 1, 0, 1]$ is $2$, because $0$ and $1$ belong to the array, but $2$ does not.
- The MEX of $[0, 3, 1, 2]$ is 4 because $0, 1, 2$ and $3$ belong to the array, but $4$ does not.

Find the maximum possible MEX of an array of non-negative integers such that the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the elements in the array does not exceed $X$.

**Input**

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- Each test case contains a single integer $X$ on a single line.

**Output**

For each test case, output on a single line the maximum possible MEX of the array satisfying the given property.

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq X \leq 10^9$

**Subtasks**

**Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
0
1
2
5
```

**Sample output**

```
1
2
2
4
```

<details><summary>Explanation</summary>

**Test case $1$:** The array could be $[0]$.

**Test case $2$:** The array could be $[0, 1]$. Here the bitwise OR of $0$ and $1$ is $1$ and the MEX of the array is $2$ as both $0$ and $1$ belongs to the array.

**Test case $4$:** The array could be $[1, 0, 3, 2]$. Here the bitwise OR of all integers in the array is $3$ and the MEX of the array is $4$.

</details>

## Approach

A MEX of $m$ requires $0, 1, \ldots, m-1$ all to appear, and extra elements can only raise the OR, so the cheapest array achieving MEX $\geq m$ is exactly $\{0, 1, \ldots, m-1\}$. Its OR has a closed form: every bit below the top bit of $m-1$ gets set by some value in the range, so

$$0 \mathbin{|} 1 \mathbin{|} \cdots \mathbin{|} (m-1) = 2^{\,\mathrm{bitlen}(m-1)} - 1$$

a block of ones. So the constraint $\text{OR} \leq X$ becomes $2^t - 1 \leq X$ with $t = \mathrm{bitlen}(m-1)$, and since that bound depends on $m$ only through $t$, the best $m$ is the largest with the same $t$:

$$\text{answer} = 2^t, \qquad t = \max\{\,t : 2^t - 1 \leq X\,\} = \mathrm{bitlen}(X+1) - 1$$

The answer is therefore always a power of two — the MEX jumps from $2^t$ straight to $2^{t+1}$ as $X$ grows, with nothing in between. That is what makes $X = 2$ and $X = 1$ give the same answer: both allow the OR $1$ but not $3$.

The samples trace the jumps. $X = 0$ forces the array $[0]$ alone, so the MEX is $1$. $X = 1$ allows $\{0,1\}$ with OR $1$, so $2$; $X = 2$ cannot afford $\{0,1,2\}$, whose OR is $3$, so it stays at $2$. And $X = 5$ affords $\{0,1,2,3\}$ with OR $3$ but not $\{0,\ldots,4\}$ with OR $7$, giving $4$.

Note the elements need not be distinct or bounded individually — only their OR is constrained — which is why no other construction can do better.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        x = int(tok)
        # OR(0..m-1) is 2^bitlen(m-1) - 1, so the answer is a power of two.
        out.append(str(1 << ((x + 1).bit_length() - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Achieving MEX $= m$ forces the array to contain $0, 1, \dots, m-1$**, whose OR is unavoidable — so the question is the largest $m$ with $\mathrm{OR}(0 \dots m-1) \leq X$.
- **That OR has a closed form**: $\mathrm{OR}(0 \dots m-1) = 2^{\mathrm{bitlen}(m-1)} - 1$, all ones up to the top bit of $m-1$. So it jumps only at powers of two, which makes the answer always a power of two.
- **Extra elements never help.** Adding anything beyond $0 \dots m-1$ can only raise the OR, so the optimal array is exactly that prefix.
- **$X = 0$** forces the array to be all zeros, giving MEX $1$ — the smallest possible answer, and the reason the formula uses $X+1$.
- **$X$ just below a power of two minus one** is the tight case: $X = 2$ still only allows $\{0, 1\}$, because adding $2$ pushes the OR to $3$.
- **The expression $2^{\mathrm{bitlen}(X+1) - 1}$** is the largest power of two at most $X+1$, which is exactly that largest $m$.
- **$X$ up to $10^9$** with constant work per case.

## Dry run

| $X$ | largest prefix $0 \dots m-1$ with OR $\leq X$ | its OR | answer |
|---:|---|---:|---:|
| 0 | $\{0\}$ | 0 | `1` |
| 1 | $\{0,1\}$ | 1 | `2` |
| 2 | $\{0,1\}$ | 1 | `2` |
| 5 | $\{0,1,2,3\}$ | 3 | `4` |

For $X = 5$, extending to $\{0,\dots,4\}$ would give an OR of $7 > 5$.

---

Same problem grouped by topic: [../docs/bit-manipulation/MEXOR.md](../docs/bit-manipulation/MEXOR.md)
