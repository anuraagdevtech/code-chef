# 1703 &middot; OR Tuples

> CodeChef problem code [`ORTUPLES`](https://www.codechef.com/problems/ORTUPLES) &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Independent bits with an eight-case table |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Bitwise Operation`, `Combinatorics` |
| **CodeChef category** | easy |
| **Time** | $O(20)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/combinatorics/ORTUPLES.md](../docs/combinatorics/ORTUPLES.md)

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

## Solution (Python)

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

## Complexity

- **Time:** $O(20)$ per test case
- **Space:** $O(1)$
