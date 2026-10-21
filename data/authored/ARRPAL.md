---
topic: Arrays
subtopic: Prefix increments force a non-increasing profile
time: $O(N)$ per test case
space: $O(1)$
---
Let $d_j$ be how many operations cover index $j$. Since every operation covers a **prefix**, an operation covering $j$ also covers everything before it, so

$$d_1 \geq d_2 \geq \cdots \geq d_N \geq 0$$

and the total number of operations is $d_1$ — every operation covers index $1$.

The final array is $A_j + d_j$, and the palindrome requirement pairs $j$ with $N+1-j$:

$$d_j - d_{N+1-j} = A_{N+1-j} - A_j =: \delta_j$$

Two conditions follow, and both are necessary.

**Each $\delta_j \geq 0$.** Because $j < N+1-j$ and $d$ is non-increasing, the left side cannot be negative. So the mirror element must already be at least as large — sample case 2, $[5,4,3,2,1]$, fails immediately with $\delta_1 = 1 - 5 < 0$.

**The $\delta_j$ must themselves be non-increasing.** Expanding $\delta_j - \delta_{j+1} = (d_j - d_{j+1}) + (d_{N-j} - d_{N+1-j})$ shows it is a sum of two non-negative terms.

When both hold, the construction is immediate: set $d_j = \delta_j$ on the first half and $d_j = 0$ on the second. That is non-increasing and satisfies every pairing, so the answer is

$$d_1 = \delta_1 = A_N - A_1$$

Sample case 3, $[1,2,3,4]$, has $\delta = (3, 1)$ — non-negative and non-increasing — giving $3$. Sample case 1 is already a palindrome with $\delta = (0,0)$, so zero operations.

## Edge cases

- **Prefix increments force a non-increasing coverage profile.** If $c_j$ counts the operations covering index $j$, then $c_1 \geq c_2 \geq \dots \geq c_N$ — so the mirror gaps $A_{n+1-j} - A_j$ must be non-negative *and* non-increasing in $j$.
- **A negative gap is immediately fatal**, since the later half can only be raised less than the earlier half. The second row, $5,4,3,2,1$, fails at the very first pair.
- **Non-negative gaps are not enough** — they must also be ordered. An input like $1, 5, 5, 4$ has gaps $3$ then $0$: fine. Reversed, $4, 5, 5, 1$ gives gaps $-3$ and $0$ and fails on sign, while $1, 2, 9, 4$ gives $3$ then $7$, which is non-negative but increasing, so `-1`.
- **The answer is $A_N - A_1$**, which is the first gap: setting $c_N = 0$ makes $c_1$ exactly that, and every operation covers index $1$ so $c_1$ is the operation count.
- **Already a palindrome** → all gaps $0$ → $0$ operations (the first row).
- **An odd $N$ leaves the middle element unconstrained**, which is why the loop runs over $\lfloor N/2 \rfloor$ pairs.
- **Sum of $N \leq 3 \cdot 10^5$**: one pass with an early break.

## Dry run

Third sample: $A = 1, 2, 3, 4$.

| pair $j$ | $A_j$ | mirror $A_{n+1-j}$ | gap | non-increasing? |
|---:|---:|---:|---:|:---:|
| 1 | 1 | 4 | 3 | — |
| 2 | 2 | 3 | 1 | $1 \leq 3$ ✓ |

Valid, so the answer is the first gap, `3`: three operations on prefixes of lengths $1$, $2$ and $2$ turn $A$ into $4, 4, 3, 4$… more precisely $c = (3, 2, 0, 0)$ gives $4, 4, 3, 4$ — wait, the coverage $c = (3,1,0,0)$ yields $4,3,3,4$, a palindrome.
