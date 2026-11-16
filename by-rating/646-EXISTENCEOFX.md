[&larr; 645. Cute Chef Gift](645-COPAR.md) &middot; [Index](README.md) &middot; [647. Distinct Values &rarr;](647-DIST_VALS.md)

# 646. Existence Of X

> [`EXISTENCEOFX`](https://www.codechef.com/problems/EXISTENCEOFX) &middot; difficulty **2235** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Column addition from the lowest bit - each bit of X is forced |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Constructive`, `Bitwise Operation`, `ad-hoc` |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log \max(A, B, C))$ per test case |
| **Space** | $O(1)$ |

## Question

You are given non-negative integers $A$, $B$ and $C$.

Does there exist a non-negative integer $X$ such that $A \oplus X+ B \oplus X = C \oplus X$?

As a reminder, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains three space-separated non-negative integers $A$, $B$ and $C$.

**Output**

For each test case, print on a new line the answer: `YES` if valid $X$ exists, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `Yes`, `YES, `yes`, `yEs` will all be treated as identical.

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq A, B, C < 2^{27}$

## Sample

**Sample input**

```
5
2 5 7
2 3 13
7 0 7
2 7 6
1 6 6
```

**Sample output**

```
YES
NO
YES
YES
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** $X=0$ satisfies the equation.

**Test case $2$:** It can be proved that there does not exist a non-negative integer $X$ which satisfies the equation.

**Test case $3$:** $X=0$ satisfies the equation.

**Test case $4$:** $X=3$ satisfies the equation.

**Test case $5$:** $X=1$ satisfies the equation.

</details>

## Approach

Add $(A \oplus X)$ and $(B \oplus X)$ column by column from the lowest bit, with a carry. In column $k$ the sum bit is

$$(a_k \oplus x_k) \oplus (b_k \oplus x_k) \oplus \text{carry} = a_k \oplus b_k \oplus \text{carry},$$

which does not depend on $x_k$ at all. It has to equal the bit of $C \oplus X$, namely $c_k \oplus x_k$, so

$$x_k = a_k \oplus b_k \oplus c_k \oplus \text{carry}$$

is forced. The carry into the next column is then determined as well: it is 1 when at least two of $a_k \oplus x_k$, $b_k \oplus x_k$ and the old carry are 1.

So there is exactly one candidate $X$, built bit by bit. Above the highest bit of the inputs all three bits are 0: if the carry is 0 there, $x$ stays 0 and everything is consistent; if the carry is 1, then $x_k = 1$, both summands get a 1 and the carry is 1 again - it never dies, so no finite $X$ exists. The loop therefore runs a couple of bits past the input width and answers YES exactly when the carry has vanished.

## Solution

```python
import sys


def solve(tokens):
    a, b, c = (next(tokens), next(tokens), next(tokens))
    carry = 0
    for position in range(29):
        bit_a = a >> position & 1
        bit_b = b >> position & 1
        bit_c = c >> position & 1
        x = bit_a ^ bit_b ^ bit_c ^ carry
        carry = (bit_a ^ x) + (bit_b ^ x) + carry >> 1
    return 'YES' if carry == 0 else 'NO'


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $X = 0$ works whenever $A + B = C$, and the procedure finds it.
- $A = B = C = 0$: YES.
- A carry surviving past the top bit means NO, however many more bits are examined.
- The inputs are below $2^{27}$; 29 columns are processed.

## Dry run

`A = 1, B = 6, C = 6`:

| bit | a b c | carry in | x | summand bits | carry out |
|---:|---|---:|---:|---|---:|
| 0 | 1 0 0 | 0 | 1 | 0, 1 | 0 |
| 1 | 0 1 1 | 0 | 0 | 0, 1 | 0 |
| 2 | 0 1 1 | 0 | 0 | 0, 1 | 0 |

The carry is 0 at the end: YES with $X = 1$, and indeed $(1 \oplus 1) + (6 \oplus 1) = 0 + 7 = 7 = 6 \oplus 1$.

---

Same problem grouped by topic: [../docs/bit-manipulation/EXISTENCEOFX.md](../docs/bit-manipulation/EXISTENCEOFX.md)
