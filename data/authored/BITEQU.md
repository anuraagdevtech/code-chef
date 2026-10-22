---
topic: Constructive
subtopic: Neutralising the AND to reduce to one XOR
time: $O(1)$ per test case
space: $O(1)$
---
The equation has three operators, but one of them can be switched off. Pick $a$ and $b$ with **disjoint bits**, so $a \mathbin{\&} b = 0$ and the whole left side collapses to

$$c \oplus d = N$$

Choosing $a = 2^{58}$ and $b = 2^{59}$ does it: both are under $10^{18}$, they share no bit, and they are far above anything $N$ can reach ($N < 2^{32}$), so they cannot collide with $c$ or $d$.

Then set $c = 2^{33}$ and $d = 2^{33} \oplus N = 2^{33} + N$. Both are positive, both differ from each other whenever $N \neq 0$, and both stay below $2^{34}$. All four values are distinct and in range, so the answer is never $-1$.

The one exception is $N = 0$, where $c \oplus d = 0$ forces $c = d$. There the AND must do some work: $a = 12$, $b = 10$ gives $a \mathbin{\&} b = 8$, and with $c = 1$ the left side is $(8 \mathbin{|} 1) \oplus 9 = 9 \oplus 9 = 0$, with $12, 10, 1, 9$ all distinct.

So a solution exists for every $N$ in range, and the distinctness requirement — the real constraint here — is handled by keeping the two "padding" values in a bit range nothing else touches.

Any answer is accepted. For $N = 1$ we print $2^{58}, 2^{59}, 2^{33}, 2^{33}{+}1$ where the sample prints the far tidier `1 4 3 2`; both satisfy the equation. The sample's third line, with $N = 3221225472 = 2^{31} + 2^{30}$, shows that the intended solutions were found by randomised search — which is unnecessary once the AND is zeroed out.

## Edge cases

- **Making $a \mathbin{\&} b = 0$ collapses the equation to $c \oplus d = N$**, so two of the four values are spent on neutralising the AND — $2^{58}$ and $2^{59}$ share no bit.
- **$N = 0$ needs a different shape.** With the AND neutralised, $c \oplus d = 0$ would force $c = d$ and break distinctness — so for zero the AND must carry the value instead: $12 \mathbin{\&} 10 = 8$, then $(8 \mathbin{|} 1) \oplus 9 = 0$.
- **$c$ is placed above every possible $N$** at $2^{33}$, which guarantees $d = c \oplus N \neq c$ for $N \neq 0$ and keeps both clear of the two padding values.
- **All four must be positive**, which $2^{33} \oplus N \geq 2^{33}$ satisfies since $N < 2^{32}$ leaves bit $33$ set.
- **The $10^{18}$ ceiling is respected**: $2^{59} \approx 5.8 \times 10^{17}$ is the largest value used.
- **The `|c` step is harmless** once the AND is zero, since $0 \mathbin{|} c = c$ — the OR is simply passed through.
- **This answer differs from the sample's** (`288230376151711744 576460752303423488 8589934592 8589934593` against `1 4 3 2`), and any valid quadruple is accepted, so a special judge evaluates the expression.

## Dry run

$N = 1$.

| step | value |
|---|---|
| $a \mathbin{\&} b = 2^{58} \mathbin{\&} 2^{59}$ | 0 (disjoint bits) |
| $0 \mathbin{|} c = 2^{33}$ | $2^{33}$ |
| $2^{33} \oplus d$ where $d = 2^{33} \oplus 1$ | $1$ ✓ |

All four are distinct and positive. For $N = 0$ the quadruple $12, 10, 1, 9$ gives $(8 \mathbin{|} 1) \oplus 9 = 9 \oplus 9 = 0$.
