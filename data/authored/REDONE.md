---
topic: Number Theory
subtopic: A telescoping product in disguise
time: $O(1)$ per test case after an $O(N)$ precomputation
space: $O(N)$
---
The combining rule factorises:

$$X + Y + XY = (1+X)(1+Y) - 1$$

So if we track $1 + v$ instead of $v$ for every element, the operation becomes plain **multiplication**. Replacing two values multiplies their shifted forms together, and the shifted form of the result is the product.

After all $N-1$ operations, one value remains, and its shifted form is the product of every original shifted value:

$$1 + \text{result} = \prod_{i=1}^{N} (1 + i) = 2 \cdot 3 \cdots (N+1) = (N+1)!$$

so the answer is $(N+1)! - 1$.

Notice what this says: the result is **independent of the order of operations**, because multiplication is commutative and associative. The problem asks for the maximum, but every sequence of choices gives the same value — there is nothing to optimise, which is the real surprise.

Checking the samples: $N = 1$ gives $2! - 1 = 1$; $N = 2$ gives $3! - 1 = 5$; $N = 4$ gives $5! - 1 = 119$.

With $T$ up to $10^5$ and $N$ up to $10^6$, factorials modulo $10^9+7$ are precomputed once in a single $O(N)$ pass, making each query a lookup. Computing a factorial per query would be $10^{11}$ operations.

One subtlety of working modulo a prime: the $-1$ must be taken **after** the modular reduction, and the result kept non-negative — `(fact[n + 1] - 1) % MOD` handles that.

## Edge cases

- **The operation is a disguised product.** $X + Y + XY = (1+X)(1+Y) - 1$, so the quantity $\prod (1 + L_i)$ is invariant across every move — the order of choices cannot matter.
- **The invariant starts at $(N+1)!$**, since $\prod_{i=1}^{N} (1 + i) = 2 \cdot 3 \cdots (N+1)$, and ends at $1 + V$ for the single survivor. Hence $V = (N+1)! - 1$.
- **$N = 1$** performs zero operations and leaves the list as $[1]$, which the formula gives as $2! - 1 = 1$.
- **The factorials must be precomputed modularly.** With $T$ up to $10^5$ and $N$ up to $10^6$, each query is a table lookup; computing a factorial per query would be far too slow.
- **The subtraction needs a final `% MOD`.** The reduced factorial can be $0$, in which case $0 - 1$ is negative, and the modulo brings it back into range.
- **The table runs to $10^6 + 1$**, one past the maximum $N$, because the answer uses $(N+1)!$.

## Dry run

| $N$ | list | invariant $\prod(1 + L_i)$ | survivor $V$ |
|---:|---|---:|---:|
| 1 | $[1]$ | $2 = 2!$ | `1` |
| 2 | $[1, 2]$ | $2 \cdot 3 = 3!$ | `5` |
| 4 | $[1,2,3,4]$ | $2 \cdot 3 \cdot 4 \cdot 5 = 5!$ | `119` |

For $N = 2$: $1 + 2 + 1 \cdot 2 = 5$, and $1 + 5 = 6 = 3!$ ✓
