---
topic: Constructive
subtopic: A single cyclic shift
time: $O(N)$ per test case
space: $O(N)$
---
The requirement is that $i \nmid P_i$ for every $i \geq 2$. Index $1$ is deliberately excluded, because $1$ divides everything and no permutation could satisfy it there.

The simplest construction is a **cyclic shift by one**:

$$P = [N, 1, 2, 3, \ldots, N-1]$$

so that $P_i = i - 1$ for every $i \geq 2$.

Why it works: for $i \geq 2$ we have $0 < i - 1 < i$, and a positive integer strictly smaller than $i$ can never be a multiple of $i$. So $i \nmid P_i$ holds for every index at once, with no case analysis.

The wrapped value $N$ lands at index $1$, which is exactly the index with no constraint — the shift puts the one problematic value in the one position where nothing is required.

Contrast this with the identity permutation, which fails at **every** index since $i \mid i$ always. Shifting by one is the minimal perturbation that fixes all of them simultaneously.

For $N = 2$ this gives `2 1`, matching the sample exactly. For $N = 3$ it gives `3 1 2` where the sample prints `1 3 2` — both satisfy the condition ($2 \nmid 3$ and $3 \nmid 2$), so **any indivisible permutation is accepted** and this is judged by a checker.

The guarantee $N \geq 2$ means the shift always has somewhere to wrap to.
