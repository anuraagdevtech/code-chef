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
