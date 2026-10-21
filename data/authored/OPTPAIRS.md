---
topic: Number Theory
subtopic: The minimum is always N, attained by a divisor family
time: $O(\sqrt{N})$ per test case
space: $O(1)$
---
Write $d = \gcd(a,b)$, $a = d a'$, $b = d b'$ with $\gcd(a',b') = 1$ and $a' + b' = s = N/d$. Then $\mathrm{lcm} = d a' b'$ and

$$g(a,b) = d + d a' b' = d\,(1 + a'b')$$

For coprime positive $a', b'$ summing to $s$, the product $a'b'$ is smallest when they are as lopsided as possible, namely $\{1, s-1\}$, giving $a'b' = s - 1$. So $g \geq d \cdot s = N$, and therefore

$$f(N) = N$$

with equality exactly when $\{a', b'\} = \{1, s-1\}$ — that is, when $a$ and $b$ are $d$ and $d(s-1) = N - d$.

So the optimal pairs are indexed by the divisors: each divisor $d$ of $N$ with $d < N$ gives the pair $(d,\, N-d)$, and $\gcd(d, N-d) = d$ confirms that $d$ is recovered from the pair, so distinct divisors give distinct pairs. Counting **ordered** pairs:

$$\text{answer} = 2 \cdot \#\{\,d \mid N : d < N/2\,\} + [\,N \text{ even}\,]$$

The second term is the self-symmetric pair $d = N/2$, where $a = b$ and the two orderings coincide — the detail that makes the answers odd for even $N$.

Enumerating divisors up to $\sqrt{N}$ handles $N \leq 10^9$ in about $3 \times 10^4$ steps.

For $N = 4$ the divisors below $2$ are just $\{1\}$, giving $(1,3)$ and $(3,1)$, plus the symmetric $(2,2)$ — three pairs, and indeed all three have $g = 4$. For $N = 105$ the seven divisors $1, 3, 5, 7, 15, 21, 35$ each give two orderings and $N$ is odd, so the answer is $14$.
