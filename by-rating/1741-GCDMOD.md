# 1741 &middot; Modular GCD

> CodeChef problem code [`GCDMOD`](https://www.codechef.com/problems/GCDMOD) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Reducing the big operand modulo the small one |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Modular Arithmetic`, `GCD`, `Euclid's Algorithm`, `Modular Exponentiation` |
| **CodeChef category** | easy |
| **Time** | $O(\log N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/GCDMOD.md](../docs/number-theory/GCDMOD.md)

## Question

At ShareChat, there are are plenty of interesting problems to solve. Here is one of them.

Given integers $A$, $B$ and $N$, you should calculate the GCD of $A^N + B^N$ and $|A - B|$. (Assume that $GCD(0, a) = a$ for any positive integer $a$). Since this number could be very large, compute it modulo $1000000007$ ($10^9 + 7$).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $A$, $B$ and $N$.

### Output
For each test case, print a single line containing one integer — the required GCD modulo $10^9 + 7$.

### Constraints
- $1 \le T \le 10$
- $1 \le A, B, N \le 10^{12}$
- $B \le A$

### Subtasks
**Subtask #1 (10 points):** $1 \le A, B, N \le 10$

**Subtask #2 (40 points):** $1 \le A, B, N \le 10^9$

**Subtask #3 (50 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le A, B, N \le 10^{12}$
- $B \le A$

## Sample

**Sample input**

```
2
10 1 1
9 1 5
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

**Example case 1:** $GCD(10^1 + 1^1, 10 - 1) = GCD(11, 9) = 1$

**Example case 2:** $GCD(9^5 + 1^5, 9 - 1) = GCD(59050, 8) = 2$

</details>

## Approach

$A^N + B^N$ is astronomically large, but a GCD only needs it **modulo the other operand**. Let $d = A - B$. Since $A \equiv B \pmod d$,

$$A^N + B^N \equiv B^N + B^N = 2B^N \pmod d$$

and therefore

$$\gcd\bigl(A^N + B^N,\ d\bigr) = \gcd\bigl(2B^N \bmod d,\ d\bigr)$$

which is computable with one modular exponentiation — $O(\log N)$ multiplications of numbers below $10^{12}$ — followed by a Euclidean GCD.

The degenerate case is $A = B$, where $d = 0$. The statement's convention $\gcd(0, a) = a$ then makes the answer $A^N + B^N = 2A^N$ itself, which must be reduced modulo $10^9+7$ — the only branch where the modulus actually does any work, since otherwise the answer is at most $d \leq 10^{12}$... and still needs reducing, as $10^{12}$ exceeds the modulus.

The reduction is what makes the problem tractable: computing $A^N + B^N$ modulo $10^9+7$ and *then* taking a GCD would be wrong, because reducing by the wrong modulus destroys the divisibility structure.

The samples: $A{=}10, B{=}1, N{=}1$ gives $d = 9$ and $2 \cdot 1 = 2$, so $\gcd(2,9) = 1$. And $A{=}9, B{=}1, N{=}5$ gives $d = 8$ with $2 \cdot 1^5 = 2$, so $\gcd(2,8) = 2$ — matching $\gcd(9^5 + 1, 8) = \gcd(59050, 8) = 2$.

## Solution (Python)

```python
import sys
from math import gcd

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, n = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        d = a - b
        if d == 0:
            out.append(str(2 * pow(a, n, MOD) % MOD))
            continue
        # A == B (mod d), so A^N + B^N collapses to 2 B^N there.
        out.append(str(gcd(2 * pow(b, n, d) % d, d) % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log N)$ per test case
- **Space:** $O(1)$
