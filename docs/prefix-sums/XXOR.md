[&larr; 328. Shortest Route](SHROUTE.md) &middot; [Index](../../README.md) &middot; [361. W String &rarr;](WSTRING.md)

# 350. Chef and Easy Problem

> CodeChef problem code [`XXOR`](https://www.codechef.com/problems/XXOR) &middot; difficulty **1810** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Per-bit prefix counts, decided bit by bit |
| **Time** | $O(31(N + Q))$ |
| **Space** | $O(31N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

You are given a sequence **A_1, A_2, ..., A_N** and **Q** queries. In each query, you are given two parameters **L** and **R**; you have to find the smallest integer **X** such that 0 ≤ **X** < 2^31 and the value of (**A_L** xor **X**) + (**A_L+1** xor **X**) + ... + (**A_R** xor **X**) is maximum possible.

Note: xor denotes the <a href = "https://en.wikipedia.org/wiki/Bitwise_operation#XOR">bitwise xor operation</a>.

**Input**

- The first line of the input contains two space-separated integers **N** and **Q** denoting the number of elements in **A** and the number of queries respectively.

- The second line contains **N** space-separated integers **A_1, A_2, ..., A_N**.

- Each of the next **Q** lines contains two space-separated integers **L** and **R** describing one query.

**Output**

For each query, print a single line containing one integer — the minimum value of **X**.

**Constraints**

- 1 ≤ **N** ≤ 10^5

- 1 ≤ **Q** ≤ 10^5

- 0 ≤ **A_i** < 2^31 for each valid **i**

**Subtasks**

**Subtask #1 (18 points):**

- 1 ≤ **N** ≤ 10^3

- 1 ≤ **Q** ≤ 10^3

- 0 ≤ **A_i** < 2^10 for each valid **i**

**Subtask #2 (82 points):** original constraints

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ Q ≤ 10^5
- 0 ≤ A_i < 2^31 for each valid i

## Sample

**Sample input**

```
5 3
20 11 18 2 13
1 3
3 5
2 4
```

**Sample output**

```
2147483629
2147483645
2147483645
```

## Approach

The sum $\sum_{i=L}^{R} (A_i \oplus X)$ splits across bit positions, and bit $b$ of $X$ affects only the $2^b$ column. So the 31 bits of $X$ are **independent** and each can be decided on its own.

Let $m = R - L + 1$ and let $c_b$ be how many of $A_L \ldots A_R$ have bit $b$ set. XORing with a $1$ at that bit flips every one of them, so the column contributes

$$\begin{cases} c_b \cdot 2^b & \text{if } X_b = 0 \\ (m - c_b) \cdot 2^b & \text{if } X_b = 1 \end{cases}$$

Take whichever is larger, which gives $X_b = 1$ exactly when $2c_b < m$. The tie $2c_b = m$ is where the **"smallest $X$"** requirement bites: both choices give the same sum, so take $X_b = 0$. The strict inequality handles this automatically.

The counts come from 31 prefix-sum arrays, one per bit, so each query is 31 constant-time lookups instead of a scan — essential with $N, Q = 10^5$.

Note the answers are huge because every bit above the data is a free win: with $A_i < 2^{31}$ but the actual values much smaller, all high bits have $c_b = 0 < m - c_b$, so $X$ sets them all. That is why the sample outputs sit just under $2^{31}$. For query `1 3` on $[20, 11, 18]$ the counted bits give $X_0 = X_2 = X_3 = 1$ and $X_1 = X_4 = 0$, i.e. $13$ in the low five bits, and bits $5 \ldots 30$ are all set, giving $2147483616 + 13 = 2147483629$.

The two later queries coincide at $2147483645$ even though the subarrays differ — the per-bit majorities happen to agree.

## Solution (Python)

```python
import sys

BITS = 31


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    a = [int(x) for x in data[2:2 + n]]
    # pref[b][i] = how many of the first i elements have bit b set.
    pref = []
    for b in range(BITS):
        run = [0] * (n + 1)
        mask = 1 << b
        total = 0
        for i, v in enumerate(a):
            if v & mask:
                total += 1
            run[i + 1] = total
        pref.append(run)

    out = []
    pos = 2 + n
    for _ in range(q):
        l, r = int(data[pos]), int(data[pos + 1])
        pos += 2
        m = r - l + 1
        x = 0
        for b in range(BITS):
            run = pref[b]
            ones = run[r] - run[l - 1]
            # Flip only when it strictly helps; a tie keeps the bit 0 so that
            # X stays as small as possible.
            if 2 * ones < m:
                x |= 1 << b
        out.append(str(x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(31(N + Q))$
- **Space:** $O(31N)$

## Edge cases

- **The bits are independent**, since each contributes $2^b$ times the count of elements whose bit differs from $X$'s — so each bit of $X$ is chosen on its own from the count of ones in the range.
- **Flip a bit only when it strictly helps**: setting $X$'s bit turns the zeros into ones, which is better when fewer than half the elements already have it. The comparison is $2 \cdot \text{ones} < m$.
- **A tie must leave the bit clear**, because the problem asks for the *smallest* such $X$ — a bit that changes nothing must not be set.
- **The high bits dominate but need no special ordering**, since the choices are independent; the per-bit rule is already optimal.
- **$31$ bit planes are prefixed**, which is what makes each query $O(31)$ rather than $O(31 \cdot \text{range})$.
- **Bits above the data are always set**, since no element has them — which is why the answers are close to $2^{31}$.
- **$X < 2^{31}$ is the stated bound**, matching the $31$ planes exactly.

## Dry run

First query of the sample: the range $1 \dots 3$ holds $20, 11, 18$, so $m = 3$.

| bit | ones in range | $2 \cdot \text{ones} < 3$? | $X$'s bit |
|---:|---:|:---:|---:|
| 0 | 1 | yes | 1 |
| 1 | 2 | no | 0 |
| 2 | 1 | yes | 1 |
| 3 | 1 | yes | 1 |
| 4 | 2 | no | 0 |
| 5–30 | 0 | yes | 1 |

$X = 2147483629$, matching the expected output.

---

Same problem in rating order (#465 of 486): [../../by-rating/465-XXOR.md](../../by-rating/465-XXOR.md)
