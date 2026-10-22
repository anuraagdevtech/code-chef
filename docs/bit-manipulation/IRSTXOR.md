# 262. Interesting XOR!

> CodeChef problem code [`IRSTXOR`](https://www.codechef.com/problems/IRSTXOR) &middot; difficulty **1487** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Maximising a product under a fixed XOR |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

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

## Solution (Python)

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

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The bound $A, B < 2^d$ is what makes the maximum finite.** Without it, both numbers could carry arbitrarily high matching bits — the XOR would be unaffected and the product unbounded.
- **Bits where $C$ is $0$ should be set in both.** $A$ and $B$ must agree there, and setting both to $1$ raises each factor at no cost to the XOR.
- **Bits where $C$ is $1$ must differ**, so they are split — and the product is maximised by balancing the two factors, which means giving $A$ the single top bit of $C$ and $B$ all of $C$'s lower set bits. Since $2^{d-1}$ exceeds the sum of everything below it, any other split is worse.
- **$d = C.\text{bit\_length}()$** is exactly the smallest $d$ with $2^d > C$, for $C \geq 1$.
- **$C$ a power of two** leaves only one differing bit, so one factor gets it and the other gets all the zero-bits below.
- **$C \leq 10^9$** keeps the factors under $2^{30}$ and the product under $2^{60}$ — past 32-bit, inside 64-bit, exact in Python.

## Dry run

Sample: $C = 13 = 1101_2$, so $d = 4$ and both factors are below $16$.

| bit | $2^b$ | $C$ | requirement | $A$ | $B$ |
|---:|---:|---:|---|---:|---:|
| 3 | 8 | 1 | differ — give to $A$ (top bit) | 1 | 0 |
| 2 | 4 | 1 | differ — give to $B$ | 0 | 1 |
| 1 | 2 | 0 | agree — set both | 1 | 1 |
| 0 | 1 | 1 | differ — give to $B$ | 0 | 1 |

$A = 1010_2 = 10$, $B = 0111_2 = 7$, and $10 \oplus 7 = 13$ with product `70`.

> CodeChef tags: `Mathematics`, `Bit Manipulation`, `Algorithms`, `Constructive`

---

Same problem in rating order (#287 of 486): [../../by-rating/287-IRSTXOR.md](../../by-rating/287-IRSTXOR.md)
