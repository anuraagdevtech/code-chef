# 1551 &middot; XxOoRr

> CodeChef problem code [`XXOORR`](https://www.codechef.com/problems/XXOORR) &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Bits are independent, so count per column |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Bitwise Operation`, `Observation` |
| **CodeChef category** | easy |
| **Time** | $O(N \log \max A)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/bit-manipulation/XXOORR.md](../docs/bit-manipulation/XXOORR.md)

## Question

Given an array $A_1, A_2 \ldots A_N$, find the minimum number of operations (possibly zero) required to convert all integers in $A$ to $0$.

In one operation, you
- choose a non-negative integer $p$ ($p \geq 0$),
- select at most $K$ indices in the array $A$, and
- for each selected index $i$, replace $A_i$ with $A_i\oplus 2^p$. Here, $\oplus$ denotes bitwise XOR.

### Subtasks
- **Subtask #1 (100 points)**: Original Constraints

**Input**

- The first line contains an integer $T$ - the number of test cases. Then $T$ test cases follow.
- The first line of each test case contains two integers $N$, $K$ - the size of the array and the maximum number of elements you can select in an operation.
- The second line of each test case contains $N$ integers $A_1, A_2 \ldots A_N$.

**Output**

For each test case, output the minimum number of operations to make all elements of the array $0$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, K \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $2\cdot 10^5$

## Sample

**Sample input**

```
1
3 2
3 6 10
```

**Sample output**

```
5
```

<details><summary>Explanation</summary>

Here is one way to achieve $[0, 0, 0]$ from $[3, 6, 10]$ in $5$ operations:
1. Choose $p = 0$ and indices $\{1\}$. Now $A$ becomes $[2, 6, 10]$.
2. Choose $p = 1$ and indices $\{1,2\}$. Now $A$ becomes $[0, 4, 10]$.
3. Choose $p = 1$ and indices $\{3\}$. Now $A$ becomes $[0, 4, 8]$.
4. Choose $p = 2$ and indices $\{2\}$. Now $A$ becomes $[0, 0, 8]$.
5. Choose $p = 3$ and indices $\{3\}$. Now $A$ becomes $[0, 0, 0]$.

It can be shown that at least $5$ operations are required.

</details>

## Approach

An operation picks a **single** bit position $p$ and flips it in at most $K$ chosen elements. Since it never touches any other bit, the $30$ bit positions are **completely independent problems** — the work for bit $p$ cannot help bit $q$.

For bit $p$, let $c_p$ be how many elements currently have it set. Every one of those must be flipped, and each operation flips at most $K$ of them, so bit $p$ needs exactly

$$\left\lceil \frac{c_p}{K} \right\rceil$$

operations — the bound is tight because the chosen indices are free, so every operation can flip a full $K$ until the last.

Summing over the bits gives the answer:

$$\sum_{p} \left\lceil \frac{c_p}{K} \right\rceil$$

Separating a problem by bit position is the standard move whenever the operation is XOR with a power of two, and here it turns an apparently tangled search into $30$ independent counting problems.

Working the sample, $A = [3, 6, 10]$ with $K = 2$: in binary $0011$, $0110$, $1010$. The column counts are $1, 3, 1, 1$ for bits $0$ through $3$, giving $1 + 2 + 1 + 1 = 5$.

Note bit $1$ is the only column needing two operations — three elements at two per operation. Bits set in a single element still cost one operation each, which is why the total exceeds the largest column count.

Counting columns is one pass over the array per bit, or equivalently one pass accumulating all $30$ counters at once.

## Solution (Python)

```python
import sys

BITS = 30


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        # Each operation touches one bit position, so the columns are separate.
        counts = [0] * BITS
        for v in data[pos + 2:pos + 2 + n]:
            x = int(v)
            while x:
                low = x & -x
                counts[low.bit_length() - 1] += 1
                x ^= low
        pos += 2 + n
        out.append(str(sum((c + k - 1) // k for c in counts)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log \max A)$ per test case
- **Space:** $O(1)$
