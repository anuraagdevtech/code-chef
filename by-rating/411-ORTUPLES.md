# 411. OR Tuples

> [`ORTUPLES`](https://www.codechef.com/problems/ORTUPLES) &middot; difficulty **1703** &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Independent bits with an eight-case table |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Bitwise Operation`, `Combinatorics` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(20)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has $3$ numbers $P$, $Q$ and $R$. Chef wants to find the number of triples $(A, B, C)$ such that:
- $(A \mid B) = P,$ $(B \mid C) = Q$ and $(C \mid A) = R$ (Here, $\mid$ denotes the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR))
- $0 \le A, B, C \lt 2^{20}$

Can you help Chef?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing $3$ space-separated integers denoting $P, Q$ and $R$ respectively.

**Output**

For each test case, output a single integer denoting the number of triplets $(A, B, C)$ that satisfy the given conditions.

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq P, Q, R \lt 2^{20}$

## Sample

**Sample input**

```
3
10 12 14
0 5 5
0 0 7
```

**Sample output**

```
4
1
0
```

<details><summary>Explanation</summary>

**Test case $1$:** The following $4$ triplets $(A, B, C)$ satisfy $A \mid B = 10, B\mid C = 12,$ and $C\mid A = 14$: $(2, 8, 12), (10, 0, 12), (10, 8, 4),$ and $(10, 8, 12)$.

**Test case $2$:** The following triplet $(A, B, C)$ satisfies $A \mid B = 0, B\mid C = 5,$ and $C\mid A = 5$: $(0, 0, 5)$.

**Test case $3$:** There are no triplets satisfying all the conditions.

</details>

## Approach

OR acts on each bit separately, and the three constraints involve only ORs, so the $20$ bit positions are **completely independent**. The total is a product of per-bit counts, and each per-bit count is a tiny finite question: given the bits $p, q, r$ of $P, Q, R$, how many $(a,b,c) \in \{0,1\}^3$ satisfy $a \mathbin{|} b = p$, $b \mathbin{|} c = q$, $c \mathbin{|} a = r$?

Enumerating all eight patterns of $(p,q,r)$:

| $(p,q,r)$ | count |
|---|---|
| $(0,0,0)$ | 1 |
| $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ | 1 |
| $(1,1,1)$ | 4 |
| $(0,0,1)$, $(0,1,0)$, $(1,0,0)$ | 0 |

The zero rows are the ones that matter. A single $1$ among $p, q, r$ is **contradictory**: if $p = q = 0$ then $a = b = c = 0$, forcing $r = 0$ too. So any bit where exactly one of the three has a one makes the whole answer $0$ — and since the counts multiply, one such bit is fatal.

The $(1,1,1)$ row gives $4$: all of $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ and $(1,1,1)$ work, i.e. at most one of $a, b, c$ may be zero.

$$\text{answer} = \prod_{b=0}^{19} \mathrm{count}\bigl(P_b, Q_b, R_b\bigr)$$

The samples exercise each row. $P,Q,R = 10, 12, 14$ has one bit in the $(1,1,1)$ pattern (bit $3$) and the rest contributing factors of $1$, so the answer is $4$. $0, 5, 5$ has only $(0,0,0)$ and $(0,1,1)$ bits, so exactly one triple works. And $0, 0, 7$ has bits with $r = 1$ alone, so the answer is $0$.

## Solution

```python
import sys

BITS = 20
# count[(p, q, r)] = solutions of a|b=p, b|c=q, c|a=r over single bits.
TABLE = {(0, 0, 0): 1, (0, 1, 1): 1, (1, 0, 1): 1, (1, 1, 0): 1,
         (1, 1, 1): 4, (0, 0, 1): 0, (0, 1, 0): 0, (1, 0, 0): 0}


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p, q, r = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        total = 1
        for b in range(BITS):
            total *= TABLE[(p >> b & 1, q >> b & 1, r >> b & 1)]
            if not total:          # one contradictory bit kills everything
                break
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The bits are independent**, so the count is a product over the $20$ bit positions of a tiny per-bit count — enumerated once into an eight-entry table.
- **Three of the eight patterns are contradictory.** If exactly one of $P, Q, R$ has the bit, no assignment of $a, b, c$ can produce it: a bit present in one OR but absent from another forces the shared variable to $0$, which then makes the first OR impossible.
- **The all-ones pattern has four solutions** — $(a,b,c)$ equal to $(0,1,1)$, $(1,0,1)$, $(1,1,0)$ or $(1,1,1)$ — which is where all the counting happens.
- **The all-zeros pattern has exactly one**, with every variable clear.
- **A single contradictory bit zeroes the answer** (the third row, where $R$ has bits that $P$ and $Q$ lack), so the loop breaks out early.
- **The product can be as large as $4^{20} \approx 10^{12}$**, past 32-bit.
- **All three inputs are below $2^{20}$**, which matches the bound on $A, B, C$ — so no bit above position $19$ ever needs considering.

## Dry run

First sample: $P = 10$, $Q = 12$, $R = 14$ — binary $01010$, $01100$, $01110$.

| bit | $(P, Q, R)$ | solutions |
|---:|---|---:|
| 0 | $(0,0,0)$ | 1 |
| 1 | $(1,0,1)$ | 1 |
| 2 | $(0,1,1)$ | 1 |
| 3 | $(1,1,1)$ | **4** |
| 4+ | $(0,0,0)$ | 1 |

Product `4`. Bit $3$ is the only one where all three agree, and it alone admits the four choices.

---

Same problem grouped by topic: [../docs/combinatorics/ORTUPLES.md](../docs/combinatorics/ORTUPLES.md)
