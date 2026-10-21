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
