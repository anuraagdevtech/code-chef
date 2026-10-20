---
topic: Game Theory
subtopic: Losing positions form a residue class
time: $O(1)$ per test case
space: $O(1)$
---
A move removes $1$ coin or $p^x$ coins for a prime $p$. The answer is that Chef loses exactly when $N$ is a **multiple of $6$**.

**No legal move is a multiple of 6.** A number divisible by $6$ has both $2$ and $3$ as prime factors, so it cannot be a prime power; and $1$ is not divisible by $6$ either. So from a multiple of $6$, every move lands on a non-multiple.

**Every non-multiple of 6 can reach a multiple of 6.** If $N \equiv r \pmod 6$ with $r \in \{1,2,3,4,5\}$, removing exactly $r$ coins works — because each of $1, 2, 3, 4, 5$ is legal: $1$ by the special rule, $2, 3, 5$ as primes, and $4 = 2^2$ as a prime power.

Those two facts make the multiples of $6$ precisely the losing positions. From one you must hand your opponent a winning position; from anything else you can hand them a losing one. Since $N = 0$ (no move available, so a loss) is a multiple of $6$, the induction is anchored.

So Chef wins iff $N \bmod 6 \neq 0$, which is $O(1)$ — essential at $N$ up to $10^9$, where computing Sprague–Grundy values directly is impossible.

The samples are both Chef wins: $N = 1$ removes the single coin, and $N = 8 = 2^3$ is itself a prime power, so Chef takes the whole pile at once. The first losing position is $N = 6$, which is neither $1$ nor a prime power and whose every move leaves a winning remainder.
