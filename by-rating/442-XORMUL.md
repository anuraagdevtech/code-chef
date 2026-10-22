[&larr; 441. Weird Subarrays](441-WEIRDSUBARR.md) &middot; [Index](README.md) &middot; [443. Fair Distribution &rarr;](443-FAIR_DISTRIB.md)

# 442. Xor and Multiply

> [`XORMUL`](https://www.codechef.com/problems/XORMUL) &middot; difficulty **1739** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Lift the shared bits, then balance the differing ones |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Basic Math`, `Bitwise Operation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

JJ has three integers $N$, $A$ and $B$ where $0 \le A, B \lt 2^N$. He wants to find a third integer $X$ such that:
- $0 \le X \lt 2^N$
- the value of $(A \oplus X) \times (B \oplus X)$ is maximum.

Here $\oplus$ represents the [Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator.

Can you help him find such an integer $X$? If there are multiple integers which satisfy the given conditions, print any.

**Input**

- The first line will contain $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $N$, $A$ and $B$ - the integers mentioned in the problem statement.

**Output**

For each test case, output an integer $X$ which satisfies the given conditions.

If multiple answers exist, print any.

## Constraints

- $1 \leq T \leq 5000$
- $1 \le N \le 30$
- $0 \le A, B \lt 2^N$

## Sample

**Sample input**

```
3
1 0 0
3 4 6
2 2 1
```

**Sample output**

```
1
3
0
```

<details><summary>Explanation</summary>

**Test case 1:** For $X = 1$, $(0 \oplus 1) \times (0 \oplus 1) = 1$ which can be proven to be the maximum value of this expression.

**Test case 2:** For $X = 3$, $(4 \oplus 3) \times (6 \oplus 3) = 35$ which can be proven to be the maximum value of this expression.

</details>

## Approach

Look at the two factors $A \oplus X$ and $B \oplus X$ bit by bit.

**Where $A$ and $B$ agree**, both factors get the same bit, and we can choose $X$ to make it $1$. So every agreeing bit contributes to *both* factors — pure gain, taken by setting $X_b = 1 - A_b$. Call the resulting common part

$$P = \bigl(2^N - 1\bigr) \oplus (A \oplus B)$$

**Where $A$ and $B$ differ**, exactly one factor gets the bit whatever $X$ does; $X_b$ only chooses *which* one. So with $Q = A \oplus B$ the product is

$$(P + u)(P + v), \qquad u + v = Q$$

where $u$ is the subset of $Q$'s bits handed to the first factor. The sum is fixed, so the product is maximised by making $u$ and $v$ as **close as possible** — and for a set of distinct powers of two the closest split is immediate: give the highest bit to one side and *all* the rest to the other, since $2^h$ exceeds the sum of every lower bit.

So: complement $A$ on the agreeing bits, send $Q$'s top bit to one factor, and send $Q$'s remaining bits to the other. When $A = B$ there are no differing bits and both factors become $2^N - 1$.

Any optimal $X$ is accepted. For $N = 3, A = 4, B = 6$ the differing bit is bit $1$, and our $X = 3$ gives $7 \cdot 5 = 35$ — matching the sample. For $N = 2, A = 2, B = 1$ every bit differs, so $Q = 3$ splits as $2$ against $1$ and $X = 0$ gives $2 \cdot 1 = 2$, which beats the $0$ that any unbalanced split would yield.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 3 * i])
        a, b = int(data[2 + 3 * i]), int(data[3 + 3 * i])
        diff = a ^ b
        # Agreeing bits: flip them up so both factors gain them.
        x = ((1 << n) - 1) ^ diff ^ (a & ~diff)
        if diff:
            top = 1 << (diff.bit_length() - 1)
            # Top differing bit to one factor, all the lower ones to the other.
            x |= (~a & top) | (~b & diff & ~top)
            x &= (1 << n) - 1
        out.append(str(x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Bits where $A$ and $B$ agree should be lifted in both factors**, so $X$ takes the complement there — a free gain for both sides of the product.
- **Bits where they differ split between the factors**, and their total contribution is fixed whichever way they fall — so the product is maximised by *balancing*, which means giving the single top differing bit to one factor and all the lower differing bits to the other.
- **The top differing bit outweighs all the lower ones**, which is why a balanced split is the best achievable rather than an even division of count.
- **No differing bits at all** ($A = B$) leaves nothing to split: $X$ is the complement everywhere and both factors become $2^N - 1$. The first sample row is this case, with $A = B = 0$ giving $X = 1$.
- **The result must be masked to $N$ bits**, since the complement of a small value sets bits above the limit.
- **$A = B = 0$ with $N = 1$** is the smallest instance and still answers $1$, not $0$.
- **Any maximising $X$ is accepted**, so a special judge evaluates the product rather than matching the value.

## Dry run

Second sample: $N = 3$, $A = 4$ ($100_2$), $B = 6$ ($110_2$), so they differ only at bit $1$.

| bit | $A$ | $B$ | agree? | $X$'s bit | reason |
|---:|---:|---:|:---:|---:|---|
| 2 | 1 | 1 | yes | 0 | both already have it |
| 1 | 0 | 1 | no | 1 | give it to $A$ (the top differing bit) |
| 0 | 0 | 0 | yes | 1 | lift both |

$X = 011_2 = 3$, giving $(4 \oplus 3) \times (6 \oplus 3) = 7 \times 5 = 35$ — the maximum.

---

Same problem grouped by topic: [../docs/bit-manipulation/XORMUL.md](../docs/bit-manipulation/XORMUL.md)
