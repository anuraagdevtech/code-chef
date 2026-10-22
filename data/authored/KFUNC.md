---
topic: Number Theory
subtopic: Digital roots are periodic along an arithmetic progression
time: $O(\log R)$ per test case
space: $O(1)$
---
$F$ is the **digital root**, and since a number is congruent to its digit sum modulo $9$,

$$F(X) = \begin{cases} 9 & X \equiv 0 \pmod 9 \\ X \bmod 9 & \text{otherwise}\end{cases}$$

for $X \geq 1$. So $F(A_i)$ depends only on $A_i \bmod 9$, and along the progression $A_i = A_1 + (i-1)D$ that residue steps by $D \bmod 9$ each time — a cyclic walk on $\mathbb{Z}_9$ with period

$$p = \frac{9}{\gcd(D \bmod 9,\ 9)}$$

(or $1$ when $D \equiv 0$). So the summands repeat with period at most $9$, and the sum over $[L, R]$ is

$$\left\lfloor \frac{n}{p} \right\rfloor \cdot \bigl(\text{one period's sum}\bigr) + \bigl(\text{first } n \bmod p \text{ terms}\bigr), \qquad n = R - L + 1$$

with the walk started at $(A_1 + (L-1)D) \bmod 9$.

That starting residue must be computed **modulo 9**, because $(L-1)D$ reaches $10^{27}$ — far past 64-bit range in C++, and merely wasteful in Python. Likewise $n$ reaches $10^{18}$, so the periodic collapse is the whole point: the loop runs at most nine times regardless.

The samples check both ends. $A_1 = 1, D = 1$ over $i \in [1,3]$ gives $F = 1, 2, 3$ and a sum of $6$. And $A_1 = 14, D = 7$ over $i \in [2,4]$ gives the terms $21, 28, 35$ with digital roots $3, 1, 8$, summing to $12$ — the period here is $9$, so all three fall inside one cycle.

## Edge cases

- **$F$ is the digital root**, which equals $X \bmod 9$ with $0$ mapped to $9$ — so no digit sums are ever computed.
- **Along an arithmetic progression the roots are periodic**, with period $9/\gcd(D \bmod 9,\, 9)$ — which is $1$, $3$ or $9$. One cycle is tabulated and the range is counted by whole cycles plus a remainder.
- **$(L-1) \cdot D$ must be reduced before multiplying.** At $L \leq 10^{18}$ and $D \leq 10^9$ the product reaches $10^{27}$, so the code reduces $(L-1)$ modulo $9$ first — the arithmetic is only needed modulo $9$ anyway.
- **$D \equiv 0 \pmod 9$ makes the period $1$**, so every term has the same root and the sum is $n$ times it — including $D = 0$, a constant progression.
- **The root $0$ must be printed as $9$**, which the table does when building the cycle — forgetting it undercounts by $9$ per occurrence.
- **$R$ up to $10^{18}$** makes $n$ enormous, so the whole-cycle multiplication is essential.
- **$L$ may equal $R$**, giving a single term.

## Dry run

Second sample: $A_1 = 14$, $D = 7$, $L = 2$, $R = 4$.

| step | value |
|---|---:|
| $D \bmod 9$ | 7 |
| first term's root: $(14 + 1 \cdot 7) \bmod 9$ | 3 |
| period $9/\gcd(7,9)$ | 9 |
| cycle of roots | $3, 1, 8, 6, 4, 2, 9, 7, 5$ |

Three terms, so the sum is $3 + 1 + 8 = $ `12`. Directly: $A_2 = 21$, $A_3 = 28$, $A_4 = 35$, whose digital roots are $3$, $1$ and $8$ ✓
