---
topic: Combinatorics
subtopic: Ordered pairs (permutations)
time: $O(1)$ per test case
space: $O(1)$
---
Chef picks a captain and a vice-captain from $N$ players. The two roles are **distinct**, so choosing Alice as captain and Bob as vice-captain is a different outcome from the reverse — the order matters.

There are $N$ ways to fill the captaincy and, with that player used up, $N - 1$ remaining for vice-captain:

$$N \cdot (N-1)$$

This is the permutation count $P(N, 2) = \frac{N!}{(N-2)!}$, not the combination count $\binom{N}{2} = \frac{N(N-1)}{2}$. Halving is the classic error here, and the sample pins it down: $N = 3$ gives $6$, not $3$. The division by $2$ in $\binom{N}{2}$ exists precisely to discard orderings, which is the wrong thing to do when the two slots mean different jobs.

The rule of thumb: ask whether swapping the two chosen items changes the answer. If it does, count permutations; if it does not, count combinations.

The team size of $11$ is scenery — only $N$, the shortlist, enters the formula. The constraint $N \geq 2$ guarantees at least one valid choice, so no empty case arises.
