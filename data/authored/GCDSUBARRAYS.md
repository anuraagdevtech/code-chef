---
topic: Constructive
subtopic: Starting from the minimum and adding the slack
time: $O(N)$ per test case
space: $O(N)$
---
Every subarray gcd is at least $1$, and there are $\binom{N+1}{2} = \frac{N(N+1)}{2}$ subarrays. So the **minimum achievable total** is

$$B = \frac{N(N+1)}{2}$$

reached by the all-ones array, where every gcd is exactly $1$. If $K < B$ the target is unreachable and the answer is $-1$.

When $K \geq B$, the slack $K - B$ has to be injected without disturbing anything else — and placing one large value at the end does exactly that. Take

$$A = [\underbrace{1, 1, \ldots, 1}_{N-1},\ x], \qquad x = K - B + 1$$

Only the single-element subarray $[x]$ has a gcd other than $1$: any subarray reaching further left includes a $1$, and $\gcd(1, \cdot) = 1$. So the total rises from $B$ by exactly $x - 1$, landing on $K$.

The isolating property of $1$ under gcd is what makes this clean — a large value anywhere else would still be fenced off by its neighbours, but putting it at the end makes the argument immediate.

The bound holds: $x = K - B + 1 \leq K \leq 10^{18}$, and $x \geq 1$ precisely when $K \geq B$.

Sample case 2 is a good check: $N = 2$ gives $B = 3$ and $x = 4 - 3 + 1 = 2$, so $A = [1, 2]$ with subarray gcds $1$, $2$ and $\gcd(1,2) = 1$, totalling $4$. Sample case 3 asks for $K = 1$ with $N = 3$, below the floor of $6$, so $-1$.

**Any valid array is accepted**, so this is judged by a checker.

## Edge cases

- **$n(n+1)/2$ is the unavoidable floor**, since every one of the $n(n+1)/2$ subarrays has a gcd of at least $1$. If $K$ is below it, the answer is $-1$ — the third row needs $K \geq 6$ and has $K = 1$.
- **A neighbouring $1$ collapses every wider subarray.** Any subarray containing one of the $n-1$ ones has gcd exactly $1$, so the only subarray that can carry the slack is the singleton holding $x$ — which is what makes the arithmetic a single subtraction.
- **$n = 1$** has no ones at all, and the single element simply equals $K$ (the first row).
- **Exactly at the floor** ($K = n(n+1)/2$) gives $x = 1$, an array of all ones — valid, and the boundary is inclusive.
- **$x \leq 10^{18}$ holds automatically**, because $x = K - n(n+1)/2 + 1 \leq K \leq 10^{18}$.
- **$K$ up to $10^{18}$** demands exact integers, and the triangular number at $n = 100$ is only $5050$, so no overflow risk arises.

## Dry run

Second sample: $n = 2$, $K = 4$. Floor is $2 \cdot 3/2 = 3$, so $x = 4 - 3 + 1 = 2$ and $A = [1, 2]$.

| subarray | gcd |
|---|---:|
| $[1]$ | 1 |
| $[2]$ | **2** |
| $[1, 2]$ | 1 |

Total $1 + 2 + 1 = 4 = K$ ✓
