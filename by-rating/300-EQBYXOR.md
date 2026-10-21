# 300. Equal by XORing

> [`EQBYXOR`](https://www.codechef.com/problems/EQBYXOR) &middot; difficulty **1507** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | The XOR span of an initial segment |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Discrete Maths`, `Bitwise Operation`, `Greedy` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

JJ has three integers $A$, $B$, and $N$. He can apply the following operation on $A$:
- Select an integer $X$ such that $1 \le X \lt N$ and set $A := A \oplus X$. (Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).)

JJ wants to make $A$ **equal** to $B$.
Determine the **minimum** number of operations required to do so. Print $-1$ if it is not possible.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $A$, $B$, and $N$ — the parameters mentioned in the statement.

**Output**

For each test case, output the minimum number of operations required to make $A$ equal to $B$. Output $-1$ if it is not possible to do so.

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq A, B \lt 2^{30}$
- $1 \leq N \le 2^{30}$

**Subtasks**

- **Subtask 1 (30 points):** $N$ is a power of $2$.
- **Subtask 2 (70 points):** Original Constraints.

## Sample

**Sample 1 input**

```
3
5 5 2
3 7 8
8 11 1
```

**Sample 1 output**

```
0
1
-1
```

<details><summary>Explanation</summary>

- **Test Case $1$:** $A$ is already equal to $B$. Hence we do not need to perform any operation.
- **Test Case $2$:** We can perform the operation with $X = 4$ which is $\lt 8$. Therefore $A = 3 \oplus 4 = 7$. Thus, only one operation is required.
- **Test Case $3$:** We can show that it is not possible to make $A$ equal to $B$.

</details>

**Sample 2 input**

```
2
24 27 3
4 5 1000
```

**Sample 2 output**

```
2
1
```

<details><summary>Explanation</summary>

Note that the above sample case belongs to subtask $2$.

- **Test Case 1:** We can first perform the operation with $X = 1$ which is $\lt 3$. Therefore $A = 24 \oplus 1 = 25$. Then we can perform the operation with $X = 2$ which is $\lt 3$. Therefore $A = 25 \oplus 2 = 27$. Therefore we can make $A$ equal to $B$ in $2$ operations. It can be shown that it is not possible to do this in less than $2$ operations.

</details>

## Approach

Let $D = A \oplus B$. Applying several operations XORs $A$ by the combined XOR of the chosen values, so the question is: in how few picks from $\{1, \ldots, N-1\}$ can we XOR to exactly $D$?

- $D = 0$ → **0** operations, $A$ already equals $B$.
- $1 \leq D < N$ → **1**, since $D$ itself is a legal choice.
- Otherwise, two may suffice — and the bound comes from the **XOR span** of the allowed set.

The set $\{1, \ldots, N-1\}$ contains every power of two up to $2^{b-1}$, where $b$ is the bit length of $N-1$. Those powers span all values below $2^b$, and nothing larger is reachable, since every element has at most $b$ bits. So $D$ is reachable at all exactly when

$$D < 2^{\,b}, \qquad b = \text{bit\_length}(N-1)$$

and otherwise the answer is $-1$.

When $D$ is reachable but $D \geq N$, two operations always work. Take $X_1 = 2^{b-1}$, which is at most $N-1$, and $X_2 = D \oplus 2^{b-1} = D - 2^{b-1}$, which is below $2^{b-1}$ and hence also legal — and non-zero because $D \geq N > 2^{b-1}$.

$N = 1$ is the degenerate case: the range $1 \leq X < 1$ is empty, so no operation exists and the answer is $-1$ unless $A$ already equals $B$. Sample case 3 is exactly this, with $N = 1$ and $D = 3$.

Sample case 2 has $D = 3 \oplus 7 = 4 < 8$, so one operation does it.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, n = map(int, data[1 + 3 * i:4 + 3 * i])
        d = a ^ b
        if d == 0:
            out.append("0")
        elif d < n:
            out.append("1")
        elif d < (1 << (n - 1).bit_length()):
            # Reachable from the powers of two below n, in two picks.
            out.append("2")
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/bit-manipulation/EQBYXOR.md](../docs/bit-manipulation/EQBYXOR.md)
