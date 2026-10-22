[&larr; 335. Chef and squares](335-CHSQR.md) &middot; [Index](README.md) &middot; [337. Chef In Infinite Plane &rarr;](337-CHFPLN.md)

# 336. Yet Another Constructive Problem

> [`ORANDCON`](https://www.codechef.com/problems/ORANDCON) &middot; difficulty **1580** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | The expression computes a bitwise majority |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Bitwise Operation`, `Constructive` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given a positive integer $X$ which is at most $10^8$.

Find three **distinct** non-negative integers $A, B, C$ that do not exceed $10^9$ and satisfy the following equation:

$$(A \mid B) \mathbin{\&} (B \mid C) \mathbin{\&} (C \mid A) = X$$

Here, $\mid $ denotes the [bitwise OR operator](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and $\mathbin{\&}$ denotes the [bitwise AND operator](https://en.wikipedia.org/wiki/Bitwise_operation#AND).

It can be shown that a solution always exists for inputs satisfying the given constraints. If there are multiple solutions, you may print **any** of them.

**Input**

- The first line contains an integer $T$, the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing one integer, $X$.

**Output**

- For each test case, print on a new line three **different** space-separated integers $A, B, C$.
- Your output will be considered correct only if $A, B, C$ are distinct non-negative integers not exceeding $10^9$ that satisfy the equation given in the problem statement.
- If there are multiple solutions, you may print **any** of them.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10^8$
- $0 \leq A, B, C \leq 10^9$
- $A, B, C$ must be pairwise distinct

## Sample

**Sample input**

```
4
3
2
13
100000000
```

**Sample output**

```
1 2 3
2 3 4
6 9 13
23570468 129811858 80835401
```

<details><summary>Explanation</summary>

**Test case $1$:** $(1 \mid 2) \mathbin{\&} (2 \mid 3) \mathbin{\&} (3 \mid 1) = 3 \mathbin{\&} 3 \mathbin{\&} 3 = 3$ and hence $A = 1, B = 2, C = 3$ is one valid solution when $X = 3$. However there are several other solutions.

For example, $A = 1, B = 6, C = 3$ is also valid and will also be considered correct.

**Test case $2$:** $(2 \mid 3) \mathbin{\&} (3 \mid 4) \mathbin{\&} (4 \mid 2) = (3 \mathbin{\&} 7) \mathbin{\&} 6 = 3 \mathbin{\&} 6 = 2$.

**Test case $3$:** $(6 \mid 9) \mathbin{\&} (9 \mid 13) \mathbin{\&} (13 \mid 6) = (15 \mathbin{\&} 13) \mathbin{\&} 15 = 13 \mathbin{\&} 15 = 13$.

</details>

## Approach

Read the expression bit by bit. A bit survives $(A \mid B) \mathbin{\&} (B \mid C) \mathbin{\&} (C \mid A)$ exactly when it is present in all three pairwise ORs — which happens precisely when **at least two of $A, B, C$ carry it**. A bit in only one of them is missing from the OR of the other two, and a bit in none is missing everywhere.

So the expression is the bitwise **majority** of $A$, $B$ and $C$, and the task is to make that majority equal $X$.

The easy construction gives all three numbers every bit of $X$ — a unanimous majority — and then makes them distinct using bits that appear in **only one** number each, so they never reach the majority:

$$A = X, \qquad B = X \mid 2^{27}, \qquad C = X \mid 2^{28}$$

Bit $27$ appears only in $B$ and bit $28$ only in $C$, so neither contributes, while every bit of $X$ appears in all three.

The choice of $27$ and $28$ is dictated by the bounds. Since $X \leq 10^8 < 2^{27}$, those two bits are guaranteed clear in $X$, so they genuinely act as distinct markers. And the largest value, $X \mid 2^{28} \leq 10^8 + 2.69 \times 10^8$, stays under the $10^9$ ceiling — whereas bit $29$ or $30$ would overflow it.

Distinctness is immediate: $A$ has neither marker bit, $B$ has one, $C$ the other.

Checking $X = 3$: the three numbers are $3$, $134217731$ and $268435459$, whose pairwise ORs all contain bits $0$ and $1$ and nothing else in common, giving $3$. **Any valid triple is accepted**, so this is judged by a checker rather than against the sample text.

## Solution

```python
import sys

# X < 2^27, so these two bits are clear in X and act as distinct markers,
# while X | 2^28 still fits under 10^9.
MARK_B = 1 << 27
MARK_C = 1 << 28


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # The expression is a bitwise majority, so give all three every bit of
        # X and separate them with bits that only one of them holds.
        out.append(f"{x} {x | MARK_B} {x | MARK_C}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The expression is a bitwise majority.** Bit $b$ of $(A|B) \mathbin{\&} (B|C) \mathbin{\&} (C|A)$ is set exactly when at least two of $A, B, C$ have bit $b$ — because a bit held by only one of them is missing from the one OR that excludes it.
- **So every bit of $X$ goes into all three**, and the three are separated by marker bits that only one of them holds, which the majority then discards.
- **The markers must be clear in $X$.** Since $X \leq 10^8 < 2^{27}$, bits $27$ and $28$ are guaranteed free — picking a marker inside $X$'s range could collide and corrupt the result.
- **The bound $10^9$ is respected**: the largest output is $X \mid 2^{28} \leq 10^8 + 2.68 \times 10^8$, comfortably under.
- **Distinctness is automatic**, as the three differ in bits $27$ and $28$.
- **$X \geq 1$ is guaranteed**, so no all-zero degenerate case arises — though the construction would handle it.
- **This answer differs from the sample's** (`3 134217731 268435459` against `1 2 3`); the statement allows any valid triple, so a special judge evaluates the expression.

## Dry run

$X = 3 = 11_2$.

| bit | $A = X$ | $B = X \mid 2^{27}$ | $C = X \mid 2^{28}$ | how many have it | majority |
|---:|:---:|:---:|:---:|---:|:---:|
| 0 | 1 | 1 | 1 | 3 | **1** |
| 1 | 1 | 1 | 1 | 3 | **1** |
| 27 | 0 | 1 | 0 | 1 | 0 |
| 28 | 0 | 0 | 1 | 1 | 0 |

The majority is $11_2 = 3 = X$ ✓

---

Same problem grouped by topic: [../docs/bit-manipulation/ORANDCON.md](../docs/bit-manipulation/ORANDCON.md)
