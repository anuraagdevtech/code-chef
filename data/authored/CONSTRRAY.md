---
topic: Constructive
subtopic: A symmetry that forces the parity of N
time: $O(N)$ per test case
space: $O(N)$
---
Write $D_i = P_i - S_i$ and let $T$ be the total sum. Then $P_{N-i} = T - S_i$ and $S_{N-i} = T - P_i$, so

$$D_{N-i} = D_i$$

The conditions demand $\mathrm{sign}(D_i) = (-1)^{i+1}$, so $i$ and $N-i$ must have the **same parity** — which happens exactly when $N$ is even. For odd $N$ some index pairs with one of the opposite parity and the requirements contradict, so the answer is $-1$. The sample's $N = 3$ is the smallest instance: $i = 1$ wants $A_1 > A_3$ while $i = 2$ reduces to $A_1 < A_3$.

For even $N$ that same identity does the construction's work. With $c_i = A_i - A_{N+1-i}$ we get $D_i = c_1 + \cdots + c_i$, and the $c$ sequence is forced to be antisymmetric ($c_{N+1-i} = -c_i$). So fixing $D_1, \ldots, D_{N/2}$ determines the rest, and the second half of the conditions is satisfied automatically.

Choose the smallest alternating targets, $D_i = (-1)^{i+1}$. Then $c_1 = 1$ and $c_i = 2(-1)^{i+1}$ for $i \geq 2$. Realise them by putting all the weight in the first half:

$$A = [\,1,\ -2,\ 2,\ -2,\ \ldots,\ \underbrace{0, 0, \ldots, 0}_{N/2}\,]$$

Every entry is within $\pm 2$, comfortably inside the $\pm 10^9$ bound.

For $N = 4$ this gives `1 -2 0 0`, whose differences are $D = 1, -1, 1$ — alternating as required. The sample's `0 -5 343 -100` is a different valid answer; any is accepted. For $N = 2$ it reduces to `1 0`, where the single condition $A_1 > A_2$ is all there is.

## Edge cases

- **An odd $N$ is impossible, by a symmetry.** Writing $D_i = P_i - S_i$ and using $S_i = \text{total} - P_{N-i}$ gives $D_{N-i} = D_i$ — so indices $i$ and $N-i$ must demand the same sign, forcing them to share parity. For odd $N$, $i = 1$ and $i = N-1$ have opposite parities and the same $D$, a contradiction.
- **That same symmetry is what makes the construction cheap.** Only the indices up to $N/2$ need arranging; the rest follow for free, since $N - i$ has the same parity as $i$ when $N$ is even.
- **The trailing zeros make $S_i = 0$ for $i \leq N/2$**, so the condition reduces to the sign of $P_i$ alone.
- **The front $1, -2, 2, -2, \dots$ makes $P_i$ alternate between $+1$ and $-1$**, exactly matching the required signs.
- **$N = 2$** is the smallest case: $[1, 0]$, with the single condition $P_1 = 1 > S_1 = 0$.
- **Values stay tiny** ($|A_i| \leq 2$), far inside the $10^9$ bound.
- **This answer differs from the sample's** (`1 0` against `343 -343`), and the statement allows any valid array, so a special judge checks the prefix and suffix sums.

## Dry run

$N = 6$ gives $A = 1, -2, 2, 0, 0, 0$ with total $1$.

| $i$ | $P_i$ | $S_i$ | required | holds? |
|---:|---:|---:|---|:---:|
| 1 | 1 | 0 | $P > S$ (odd) | ✓ |
| 2 | $-1$ | 0 | $P < S$ (even) | ✓ |
| 3 | 1 | 0 | $P > S$ (odd) | ✓ |
| 4 | 1 | 2 | $P < S$ (even) | ✓ |
| 5 | 1 | 0 | $P > S$ (odd) | ✓ |

Note $D_1 = D_5 = 1$ and $D_2 = D_4 = -1$, the symmetry in action.
