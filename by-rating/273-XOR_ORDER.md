[&larr; 272. Cakewalk](272-CKWLK.md) &middot; [Index](README.md) &middot; [274. Chef and Numbers &rarr;](274-CHEFFED.md)

# 273. Order by XOR

> [`XOR_ORDER`](https://www.codechef.com/problems/XOR_ORDER) &middot; difficulty **1476** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | The highest differing bit decides an XOR comparison |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Constructive`, `Bitwise Operation`, `ad-hoc` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given three **distinct** integers $A, B,$ and $C$.

Find **any** integer $X \ (0 \leq X < 2^{30})$ such that:
$(A \oplus X) \lt (B \oplus X) \lt (C \oplus X)$, where $\oplus$ denotes the [Bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

If no such $X$ exists, print $-1$ instead.

**Input**

- The first line of the input contains a single integer $T$, the number of test cases.
- The first and only line of each test case contains three space-separated integers $A, B,$ and $C$.

**Output**

For each test case, output a single integer on a new line, the value of $X$ that satisfies the above conditions or $-1$ if no such $X$ exists.

If multiple such $X$ satisfy the condition, you may print any.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B, C \lt 2^{30}$
- $A, B, C$ are **distinct**.

## Sample

**Sample input**

```
3
1 2 3
3 1 2
3 2 1
```

**Sample output**

```
4
-1
3
```

<details><summary>Explanation</summary>

**Test case $1$:** For $X = 4$,
- $A \oplus X = 1 \oplus 4 \ = 5$
- $B \oplus X = 2 \oplus 4 \ = 6$
- $C \oplus X = 3 \oplus 4 \ = 7$

Thus, $(A \oplus X) \lt (B \oplus X) \lt (C \oplus X)$.

**Test case $2$:** No $X \ (0 \leq X \lt 2^{30})$ exists that satisfies the above conditions.

**Test case $3$:** For $X = 3$,
- $A \oplus X = 3 \oplus 3 \ = 0$
- $B \oplus X = 2 \oplus 3 \ = 1$
- $C \oplus X = 1 \oplus 3 \ = 2$

Thus, $(A \oplus X) \lt (B \oplus X) \lt (C \oplus X)$.

</details>

## Approach

XOR-ing a common $X$ into two numbers preserves which bits differ between them, so the comparison $(A \oplus X) < (B \oplus X)$ is decided entirely at the **highest bit where $A$ and $B$ differ**. Call it $p$; the bits above $p$ are identical and cancel, and the bits below are irrelevant once bit $p$ separates them.

At that bit, we need $A \oplus X$ to hold $0$ and $B \oplus X$ to hold $1$, which pins down one bit of $X$:

$$X_p = A_p$$

(and equivalently $X_p = 1 - B_p$, consistent because $A_p \neq B_p$).

So each of the two required inequalities fixes exactly one bit of $X$:

- $A < B$ fixes bit $p = \text{msb}(A \oplus B)$ to $A_p$
- $B < C$ fixes bit $q = \text{msb}(B \oplus C)$ to $B_q$

If $p \neq q$ the two constraints are independent, so set those bits and leave the rest at $0$. If $p = q$ they collide: the first demands $X_p = A_p$ and the second $X_p = B_p$, and since $A_p \neq B_p$ at their highest differing bit, no $X$ can satisfy both — the answer is $-1$.

In Python, $\text{msb}(z)$ is `z.bit_length() - 1`, and the inputs are distinct so neither XOR is zero.

Sample case 2, $(3,1,2)$, is the conflict: $3 \oplus 1 = 2$ and $1 \oplus 2 = 3$ both have their top bit at position $1$, and $3$ has a $1$ there while $1$ has a $0$ — irreconcilable, so $-1$.

**Any valid $X$ is accepted**, so this is judged by a checker. Sample case 1 publishes $4$ while this construction yields $0$; both order $1, 2, 3$ correctly, so a verbatim diff would report a false mismatch.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # Each inequality is decided at the top bit where its pair differs.
        p = (a ^ b).bit_length() - 1
        q = (b ^ c).bit_length() - 1
        if p == q:
            # One bit, two incompatible demands.
            out.append("-1")
        else:
            x = (a & (1 << p)) | (b & (1 << q))
            out.append(str(x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Each inequality is decided at a single bit** — the highest bit where its pair differs. $A \oplus X < B \oplus X$ holds exactly when $X$'s bit $p$ equals $A$'s, where $p$ is the top differing bit of $A$ and $B$; every lower bit is irrelevant.
- **When the two deciding bits coincide, the demands conflict.** If $p = q$, the bit must match both $A_p$ and $B_p$, and $A$ and $B$ differ there by construction — so the answer is $-1$. The second row is this case.
- **Otherwise the two constraints touch different bits and compose freely**, so setting each of them independently always works; no search over $X$ is needed.
- **Every other bit of $X$ may be anything**, which is why many answers are valid: the first row prints $0$ here where the sample shows $4$, and both satisfy $1 < 2 < 3$ after XOR. A special judge checks the inequalities.
- **The bound $X < 2^{30}$ is automatic**, since $p$ and $q$ are below $30$ for inputs under $2^{30}$.
- **$A, B, C$ are distinct**, so both XORs are non-zero and `bit_length() - 1` is well defined — on a zero XOR it would give $-1$ and a nonsense shift.

## Dry run

Third sample: $A = 3$, $B = 2$, $C = 1$.

| pair | XOR | top differing bit | demand on $X$ |
|---|---:|---:|---|
| $A, B$ | $3 \oplus 2 = 1$ | $p = 0$ | bit $0$ of $X$ $=$ bit $0$ of $A$ $= 1$ |
| $B, C$ | $2 \oplus 1 = 3$ | $q = 1$ | bit $1$ of $X$ $=$ bit $1$ of $B$ $= 1$ |

So $X = 3$, and indeed $3 \oplus 3 = 0 < 2 \oplus 3 = 1 < 1 \oplus 3 = 2$.

---

Same problem grouped by topic: [../docs/bit-manipulation/XOR_ORDER.md](../docs/bit-manipulation/XOR_ORDER.md)
