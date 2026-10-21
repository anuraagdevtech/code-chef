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

## Edge cases

- **No legal move is a multiple of $6$.** A multiple of $6$ needs both $2$ and $3$ as factors, which no prime power $p^x$ has, and $1$ is not one either — so from a multiple of $6$ every move lands on a non-multiple.
- **Every non-zero remainder is itself a legal move.** Remainders $1, 2, 3, 4, 5$ correspond to taking $1$ coin, $2^1$, $3^1$, $2^2$ and $5^1$ — so from any non-multiple the mover can hand their opponent a multiple of $6$.
- **Together these make multiples of $6$ exactly the losing positions**, and since Chef moves first he loses precisely when $N \equiv 0 \pmod 6$.
- **$N = 0$ is unreachable** as input ($N \geq 1$), but it is the base losing position the argument rests on.
- **$N = 1$** (the first sample row): Chef takes the single coin and Misha cannot move.
- **$N$ up to $10^9$** — the closed form needs no table, whereas a Sprague–Grundy computation would be hopeless at this bound.

## Dry run

| $N$ | $N \bmod 6$ | Chef's move | outcome |
|---:|---:|---|---|
| 1 | 1 | take $1$, leaving $0$ | `Chef` |
| 8 | 2 | take $2 = 2^1$, leaving $6$ | `Chef` |
| 6 | 0 | every move leaves $1$–$5$ | `Misha` |

From $6$, whatever Chef takes, Misha can take the remainder and leave $0$.
