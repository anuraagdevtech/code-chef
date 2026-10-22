# 242. Make Array Odd

> CodeChef problem code [`MAKEARRAYODD`](https://www.codechef.com/problems/MAKEARRAYODD) &middot; difficulty **1445** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Tracking a single bit through XOR and OR |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You are given an array $A$ and an integer $X$. You are allowed to perform the following operation on the array:
- Select two **distinct** indices $i$ and $j$ and set both $A_i$ and $A_j$ as $((A_i \oplus A_j) \mid X)$ simultaneously. Here $\oplus$ and $\mid$ denote the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) and [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) operations respectively.

Find the **minimum** number of operations required to make **all** elements of the array **odd**. If it is not possible to do so, print $-1$ instead.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$, the size of the array and $X$.
    - The next line contains $N$ space-separated integers denoting the elements of the array $A$.

**Output**

For each test case, output on a new line, the **minimum** number of operations required to make **all** elements of the array **odd**. If it is not possible to do so, print $-1$ instead.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $0 \leq X \lt 2^{30}$
- $0 \leq A_i \lt 2^{30}$
- The sum of $N$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
2
3 6
5 7 9
5 4
2 3 4 17 9
```

**Sample output**

```
0
2
```

<details><summary>Explanation</summary>

**Test case $1$:** All elements are already odd. Thus, the number of operation required will be $0$.

**Test case $2$:** We can make all elements odd using $2$ operations -
 - In first operation, we choose $i=1, j=5$.
Here, $(A_i\oplus A_j)\mid X=(2 \oplus 9)\mid 4 = 11 \mid 4 = 15$. Thus, the new array becomes $[15,3,4,17,15]$.
 - In second operation, we choose $i=4, j=3$.
Here, $(A_i\oplus A_j)\mid X=(17 \oplus 4)\mid 4 = 21 \mid 4 = 21$. Thus, the new array becomes $[15,3,21, 21,15]$.

All elements of the array are odd now. It can be shown that we cannot achieve this in less than $2$ operations.

</details>

## Approach

Only the lowest bit matters, so look at what the operation does to it. Setting both entries to $(A_i \oplus A_j) \mid X$ gives a result whose parity is

$$\bigl(\mathrm{lsb}(A_i) \oplus \mathrm{lsb}(A_j)\bigr) \;\lor\; \mathrm{lsb}(X)$$

That splits cleanly on the parity of $X$.

**$X$ odd.** The OR forces the low bit to $1$ regardless of the operands, so *any* operation makes both chosen elements odd. Each move can fix two evens at once, so with $e$ even elements the answer is $\lceil e/2 \rceil$. When $e$ is odd the final move pairs the last even with an already-odd element — harmless, since that element stays odd.

**$X$ even.** The OR contributes nothing to the low bit, so the result is odd only when exactly **one** of the two operands is odd. Each operation therefore consumes one odd partner and converts one even element, reducing the even count by exactly one: the answer is $e$. And if the array contains no odd element at all, no operation can ever produce one — the parity is stuck — so the answer is $-1$.

The all-even, even-$X$ case is the only impossible one, and it is the thing to check for.

Sample case 1 has every element odd already, so $0$ operations regardless of $X$. Sample case 2 has $X = 4$ (even) with two evens and three odds, giving $2$ — one operation per even element.

Counting parities is a single pass; nothing else about the values matters, which is what keeps this $O(N)$ at $\sum N = 10^5$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        evens = sum(1 for v in data[pos + 2:pos + 2 + n] if int(v) % 2 == 0)
        pos += 2 + n
        if evens == 0:
            out.append("0")
        elif x % 2:
            # The OR forces the low bit, so one move fixes two elements.
            out.append(str((evens + 1) // 2))
        elif evens == n:
            # No odd partner exists and none can be created.
            out.append("-1")
        else:
            # Each move needs one odd partner and converts one even.
            out.append(str(evens))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Everything already odd** → $0$ operations, which must be checked before anything else.
- **$X$ odd**: the `| X` forces the low bit on regardless of the XOR, so *any* pair becomes odd — including a pair of two evens. One operation therefore fixes two elements, giving $\lceil \text{evens}/2 \rceil$, and a lone leftover even can be paired with an already-odd element at no extra cost.
- **$X$ even with every element even** → $-1$. The low bit of the result is $a_0 \oplus b_0 = 0$, so two evens stay even and no odd can ever be created.
- **$X$ even with at least one odd**: pairing an even with an odd gives a low bit of $0 \oplus 1 = 1$, so both come out odd — one operation per even element, and the odd count only grows, so a partner is always available. The answer is exactly the number of evens.
- **The two indices must be distinct**, which matters only for $N = 1$; the constraints guarantee $N \geq 2$.
- **Only the low bit of $X$ matters**, so the other $29$ bits never enter the reasoning.

## Dry run

Second sample: $X = 4$ (even), $A = 2, 3, 4, 17, 9$.

| element | parity |
|---:|---|
| 2 | even |
| 3 | odd |
| 4 | even |
| 17 | odd |
| 9 | odd |

Two evens, and odd partners exist, so two operations:

| operation | result |
|---|---|
| pair $2$ with $3$: $(2 \oplus 3) \mid 4 = 1 \mid 4 = 5$ | both become $5$ (odd) |
| pair $4$ with $9$: $(4 \oplus 9) \mid 4 = 13 \mid 4 = 13$ | both become $13$ (odd) |

Output `2`.

> CodeChef tags: `Mathematics`, `Bit Manipulation`, `Algorithms`

---

Same problem in rating order (#255 of 486): [../../by-rating/255-MAKEARRAYODD.md](../../by-rating/255-MAKEARRAYODD.md)
