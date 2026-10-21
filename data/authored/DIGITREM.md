---
topic: Basic Math
subtopic: Digit-position candidates for the next clean number
time: $O(\log^2 N)$ per test case
space: $O(\log N)$
---
We want the smallest $M \geq N$ whose decimal form avoids the digit $D$; the answer is $M - N$.

Let $p$ be the **leftmost** position where $N$'s digit equals $D$. If there is none, $M = N$ and the answer is $0$. Otherwise, let $i$ be the first position where $M$ and $N$ differ. Then $M_i > N_i$ (else $M < N$), and $M$ agrees with $N$ before $i$, so those digits must be clean — forcing $i \leq p$. That gives at most $p+1$ candidates, one per $i$:

- keep $N$'s digits before $i$;
- at $i$, take the **smallest** digit above $N_i$ that is not $D$;
- fill the rest with the smallest allowed digit, which is $0$ unless $D = 0$, in which case it is $1$.

Take the smallest candidate. A position can fail outright when the digit would have to exceed $9$ — and if *every* position fails, $M$ must be longer than $N$, so the answer is the smallest clean number with one more digit: leading $1$ (or $2$ when $D = 1$) followed by the fill digit.

Filling with the smallest digit rather than copying $N$'s tail is the point: once a more significant digit has been raised, the tail is free, and zeroing it out is what keeps $M$ minimal.

The samples walk through each branch. $21$ with $D = 5$ is already clean. $8$ with $D = 8$ raises the only digit to $9$, costing $1$. $100$ with $D = 0$ raises position $1$ to $1$ and fills with $1$, giving $111$ — not $200$, because the more significant raise is dearer. $5925$ with $D = 9$ cannot raise the $9$ at all, so it raises the leading $5$ to $6$ and zeroes the rest: $6000$. And $434356$ with $D = 3$ raises the second digit to $4$, giving $440000$.
