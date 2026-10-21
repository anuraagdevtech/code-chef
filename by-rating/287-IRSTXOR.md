# 287. Interesting XOR!

> [`IRSTXOR`](https://www.codechef.com/problems/IRSTXOR) &middot; difficulty **1487** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Maximising a product under a fixed XOR |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Constructive`, `Bitwise Operation`, `Greedy`, `ad-hoc`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an integer $C$. Let $d$ be the smallest integer such that $2^d$ is strictly greater than $C$.

Consider all pairs of non-negative integers $(A,B)$ such that $A,B \lt 2^d$ and $A \oplus B = C$ ($\oplus$ denotes the bitwise XOR operation). Find the maximum value of $A \cdot B$ over all these pairs.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $C$.

**Output**
For each test case, print a single line containing one integer ― the maximum possible product $A \cdot B$.

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \leq C \leq 10^9$

**Subtasks**
**Subtask #1 (30 points):** $1 \leq C \leq 10^3$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq C \leq 10^9$

## Sample

**Sample input**

```
2
13
10
```

**Sample output**

```
70
91
```

<details><summary>Explanation</summary>

**Example case 1:** The binary representation of $13$ is "1101". We can use $A = 10$ ("1010" in binary) and $B = 7$ ("0111" in binary). This gives us the product $70$. No other valid pair $(A, B)$ can give us a larger product.

**Example case 2:** The binary representation of $10$ is "1010". We can use $A = 13$ ("1101") and $B = 7$ ("0111"). This gives us the maximum product $91$.

</details>

## Approach

Let $d$ be the bit width, so $2^{d-1} \leq C < 2^d$, and let $M = 2^d - 1$ be the all-ones mask.

$A \oplus B = C$ says $A$ and $B$ **differ** exactly on the bits where $C$ is $1$, and **agree** everywhere else. That splits the construction into two independent decisions.

**On $C$'s zero bits**, $A$ and $B$ agree, so setting them all to $1$ raises both numbers and can only increase the product. Those bits are $M \oplus C$, and both $A$ and $B$ receive them.

**On $C$'s one bits**, each bit goes to exactly one of the two. The sum $A + B$ is now fixed at $C + 2(M \oplus C)$ regardless of how they are split, and for a fixed sum the product is largest when the two values are as **close as possible**. The top bit of $C$ is bit $d-1$ and dwarfs all the others combined, so give that single bit to one number and every remaining bit of $C$ to the other — that is the most balanced split achievable.

So, with $h = 2^{d-1}$:

$$A = (M \oplus C) \mid h, \qquad B = (M \oplus C) \mid (C \oplus h)$$

Checking $C = 13 = 1101_2$: here $d = 4$, $M = 1111_2$, and $M \oplus C = 0010_2$. The top bit is $8$, so $A = 0010 \mid 1000 = 10$ and $B = 0010 \mid 0101 = 7$, giving $70$.

For $C = 10 = 1010_2$: $M \oplus C = 0101_2$, $A = 0101 \mid 1000 = 13$, $B = 0101 \mid 0010 = 7$, giving $91$ — larger than for $C = 13$, since the shared ones contribute more.

In Python $d$ is `C.bit_length()`, so the whole thing is a handful of bitwise operations.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        c = int(data[1 + i])
        d = c.bit_length()
        mask = (1 << d) - 1
        shared = mask ^ c            # bits where A and B agree: set both to 1
        high = 1 << (d - 1)          # C's top bit outweighs all the others
        a = shared | high
        b = shared | (c ^ high)
        out.append(str(a * b))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/bit-manipulation/IRSTXOR.md](../docs/bit-manipulation/IRSTXOR.md)
