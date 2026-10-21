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
