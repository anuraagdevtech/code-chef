# 364. Construct Array

> [`CONSTRRAY`](https://www.codechef.com/problems/CONSTRRAY) &middot; difficulty **1624** &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A symmetry that forces the parity of N |
| **CodeChef tags** | `Algorithms`, `Constructive` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given a positive integer $N$.

Consider an array $A$ of length $N$. Let $P_i$ denote the sum of the first $i$ elements of $A$ and $S_i$ denote the sum of the last $i$ elements of $A$.

You need to construct the array $A$ of size $N$ such that all of the following conditions are met:
- $-10^9 \leq A_i \leq 10^9$, for all $(1\le i \le N)$
- $P_i \gt S_i$ if $i$ is odd, for each $(1 \leq i \lt N)$
- $P_i \lt S_i$ if $i$ is even, for each $(1 \leq i \lt N)$

If there are multiple solutions, you can print any of them.
If there is no such array, print $-1$ instead.

**Input**

- Each test contains multiple test cases. The first line contains the number of test cases $T$.
- The only line of each test case contains a single integer $N$, where $N$ is the length of the required array.

**Output**

For each test case, if a **valid** array exists, print $N$ space-separated integers $A_1, A_2, \ldots, A_N$ satisfying all the given conditions.

If there are multiple solutions, you can print any of them.
If there is no such array, print $-1$ instead.

## Constraints

- $1 \leq T \leq 10^3$
- $2 \leq N \leq 10^5$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
3
2
3
4
```

**Sample output**

```
343 -343
-1
0 -5 343 -100
```

<details><summary>Explanation</summary>

**Test case $1$:** All elements are in the given range for the array $A = [343, -343]$.
- For $i = 1$: Since $i$ is odd, $P_1 = 343$ is greater than $S_1 = -343$.

**Test case $2$:** It can be proved that no array of length $3$ exists satisfying all conditions.

**Test case $3$:** All elements are in the given range for the array $A = [0, -5, 343, -100]$.
- For $i = 1$: Since $i$ is odd, $P_1 = 0$ is greater than $S_1 = -100$.
- For $i = 2$: Since $i$ is even, $P_2 = 0 + (-5) = -5$ is less than $S_2 = 343 + (-100) = 243$.
- For $i = 3$: Since $i$ is odd, $P_3 = 0 + (-5) + 343 = 338$ is greater than $S_3 = (-5)+343 +(-100) = 238$.

</details>

## Approach

Write $D_i = P_i - S_i$ and let $T$ be the total sum. Then $P_{N-i} = T - S_i$ and $S_{N-i} = T - P_i$, so

$$D_{N-i} = D_i$$

The conditions demand $\mathrm{sign}(D_i) = (-1)^{i+1}$, so $i$ and $N-i$ must have the **same parity** — which happens exactly when $N$ is even. For odd $N$ some index pairs with one of the opposite parity and the requirements contradict, so the answer is $-1$. The sample's $N = 3$ is the smallest instance: $i = 1$ wants $A_1 > A_3$ while $i = 2$ reduces to $A_1 < A_3$.

For even $N$ that same identity does the construction's work. With $c_i = A_i - A_{N+1-i}$ we get $D_i = c_1 + \cdots + c_i$, and the $c$ sequence is forced to be antisymmetric ($c_{N+1-i} = -c_i$). So fixing $D_1, \ldots, D_{N/2}$ determines the rest, and the second half of the conditions is satisfied automatically.

Choose the smallest alternating targets, $D_i = (-1)^{i+1}$. Then $c_1 = 1$ and $c_i = 2(-1)^{i+1}$ for $i \geq 2$. Realise them by putting all the weight in the first half:

$$A = [\,1,\ -2,\ 2,\ -2,\ \ldots,\ \underbrace{0, 0, \ldots, 0}_{N/2}\,]$$

Every entry is within $\pm 2$, comfortably inside the $\pm 10^9$ bound.

For $N = 4$ this gives `1 -2 0 0`, whose differences are $D = 1, -1, 1$ — alternating as required. The sample's `0 -5 343 -100` is a different valid answer; any is accepted. For $N = 2$ it reduces to `1 0`, where the single condition $A_1 > A_2$ is all there is.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        if n % 2:
            # D_{N-i} = D_i forces i and N-i to share parity.
            out.append("-1")
            continue
        half = n // 2
        front = [1] + [2 if i % 2 else -2 for i in range(2, half + 1)]
        out.append(" ".join(map(str, front + [0] * half)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/constructive/CONSTRRAY.md](../docs/constructive/CONSTRRAY.md)
