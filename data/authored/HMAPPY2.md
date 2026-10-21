---
topic: Number Theory
subtopic: Counting multiples with inclusion-exclusion
time: $O(\log \min(A,B))$ per test case
space: $O(1)$
---
With $N$ up to $10^{18}$ nothing can be enumerated; the count has to be closed-form. The number of codes in $1 \ldots N$ divisible by $d$ is $\lfloor N/d \rfloor$, and a code divisible by both $A$ and $B$ is exactly one divisible by $\mathrm{lcm}(A,B)$.

Appy solves the multiples of $A$ that are not multiples of $B$, which is $\lfloor N/A \rfloor - \lfloor N/L \rfloor$ with $L = \mathrm{lcm}(A,B)$, and Chef's share is the mirror image. Their sets are disjoint by construction, so

$$\text{solved} = \left\lfloor \frac{N}{A} \right\rfloor + \left\lfloor \frac{N}{B} \right\rfloor - 2\left\lfloor \frac{N}{L} \right\rfloor$$

The factor of **$2$** is the point: the common multiples are excluded from *both* shares, so they are subtracted twice — unlike the usual union formula, which subtracts them once. Nobody solves a problem divisible by both.

Compute $L$ as $A/\gcd(A,B) \cdot B$ to keep it small, and note $L$ can reach $10^{18}$, so this needs 128-bit care in C++ while Python handles it natively. When $L > N$ the term is simply $0$.

The degenerate case $A = B$ is allowed, and the formula handles it: $L = A$, so the count is $\lfloor N/A \rfloor + \lfloor N/A \rfloor - 2\lfloor N/A \rfloor = 0$ — every problem is divisible by both, so neither may take it.

The sample has $N = 6, A = 2, B = 3$: Appy takes $2$ and $4$, Chef takes $3$, and $6$ goes to neither, giving $3 + 2 - 2 = 3$, which meets $K = 3$ exactly — so `Win`, since the requirement is *at least* $K$.

## Edge cases

- **Common multiples are barred from *both* shares, so they are subtracted twice.** With $N = 6$, $A = 2$, $B = 3$: Appy gets $2$ and $4$, Chef gets $3$, and problem $6$ goes to neither. Standard inclusion–exclusion subtracts the overlap once and reports $4$, which would wrongly answer `Win` at $K = 4$.
- **$A = B$**: the lcm is $A$, so the count is $2\lfloor N/A \rfloor - 2\lfloor N/A \rfloor = 0$ — every multiple is common and nobody solves anything.
- **The lcm must be computed as `a // gcd(a, b) * b`**, dividing before multiplying; with $A, B$ up to $10^9$ the product reaches $10^{18}$, which is native in Python but would overflow a 64-bit signed type in C++.
- **$N$ up to $10^{18}$** forces exact integer division — a float division loses precision above $2^{53}$ and can report the wrong count.
- **$K \leq N$ is guaranteed**, so the target is never trivially impossible.
- **Exactly meeting $K$ counts as a win**, so the comparison is non-strict.

## Dry run

Sample: $N = 6$, $A = 2$, $B = 3$, $K = 3$. $\operatorname{lcm}(2,3) = 6$.

| problem | multiple of 2 | multiple of 3 | solved by |
|---:|:---:|:---:|---|
| 1 | | | nobody |
| 2 | yes | | Appy |
| 3 | | yes | Chef |
| 4 | yes | | Appy |
| 5 | | | nobody |
| 6 | yes | yes | **nobody** (both) |

Count $= 3 + 2 - 2 \cdot 1 = 3 \geq 3$, so `Win`.
