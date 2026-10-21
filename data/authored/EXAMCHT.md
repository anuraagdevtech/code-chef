---
topic: Number Theory
subtopic: Counting divisors of a difference
time: $O(\sqrt{|A-B|})$ per test case
space: $O(1)$
---
Ram and Shyam share a set exactly when $(A-1) \bmod p = (B-1) \bmod p$, which is

$$p \mid (A - B)$$

So the question is purely how many positive $p$ divide $A-B$.

If $A = B$ the difference is $0$ and every $p$ works, so there are infinitely many — print $-1$. That case cannot arise from distinct roll numbers, but the input permits it.

Otherwise the answer is the **number of divisors** of $|A-B|$, counted by trial division up to $\sqrt{|A-B|}$: each divisor $d \leq \sqrt{D}$ pairs with $D/d$, and the pair is counted once when $d^2 = D$. With $|A-B| < 10^8$ that is at most $10^4$ steps, so $T \leq 100$ is trivial.

The sign does not matter, since $p \mid (A-B)$ and $p \mid (B-A)$ are the same condition — take the absolute value before factoring.

The sample has $A = 2$ and $B = 6$, so $|A-B| = 4$ with divisors $1, 2, 4$, giving $3$. Checking $p = 4$: roll $2$ gets set $1 \bmod 4 = 1$ and roll $6$ gets set $5 \bmod 4 = 1$ — the same. But $p = 3$ fails: sets $1$ and $2$.

Note every difference has $p = 1$ among its divisors, so with $A \neq B$ the answer is at least $1$ — a single question set is always shared.
