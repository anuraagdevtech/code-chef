---
topic: Sorting
subtopic: Two candidate offsets, verified by a merge
time: $O(N \log N)$ per test case
space: $O(N)$
---
Sort both arrays. $B$ is $A$ with one element dropped and $X$ added to the rest, so sorting preserves the correspondence: $B_0$ must come from either $A_0$ or $A_1$ — the only two possibilities for "smallest surviving element", depending on whether $A_0$ was the one removed.

That gives just **two candidate offsets**:

$$X = B_0 - A_1 \qquad\text{or}\qquad X = B_0 - A_0$$

Since $A_1 > A_0$, the first is the smaller, so try it first and take the first that validates.

**Validation** is a two-pointer merge: walk $A$ and $B$ together, consuming a $B$ element whenever $A_i + X$ matches it and otherwise skipping that $A_i$. The candidate is valid when at most **one** skip occurs and all of $B$ is consumed.

The constraint $X > 0$ must also be checked — $B_0 - A_1$ can easily be zero or negative, as in sample case 3 where $A = [2,4]$ and $B = [3]$ give $3 - 4 = -1$, rejecting that candidate and leaving $X = 1$.

Sample case 1 shows the larger candidate winning: $A = [1,3,4,8]$ and $B = [8,11,15]$ reject $X = 5$ (which would need an $11$ that $A+5$ does not produce) and accept $X = 7$, dropping the $3$.

Sample case 2 takes the smaller candidate, $X = 2$, dropping the $4$ — and it is genuinely smaller than the alternative $X = 6$, which is why the order of trying matters for the "smallest $X$" requirement.

Values reach $2 \times 10^9$, so this needs **64-bit** arithmetic outside Python.

## Edge cases

- **Exactly one element of $A$ is dropped**, so after sorting both arrays, $B_1$ must come from either $A_1$ or $A_2$ — nothing further along, since at most one element before it can be missing.
- **Trying $A_2$ first yields the smaller $X$**, because $A_2 > A_1$ makes $B_1 - A_2 < B_1 - A_1$ — and the problem asks for the smallest. Checking $A_1$ first would return the larger offset whenever both work.
- **$X$ must be strictly positive**, which the guard enforces; $B_1 - A_2$ can easily come out negative or zero.
- **The candidate is verified by a merge**, allowing exactly one skip in $A$ — which rejects an offset that matches the first element by accident.
- **The merge must also confirm $B$ is exhausted**, hence the `j == len(b)` check; running out of $A$ early is a failure.
- **$N = 2$ leaves a single element in $B$** (the second and third rows), where both candidates are worth trying.
- **The values are pairwise distinct within each array**, so the sorted merge never faces ties.
- **$B_i$ can reach $2 \times 10^9$** while $A_i$ caps at $10^9$, so the offset can be as large as the values themselves.

## Dry run

First sample: $A = 1, 3, 4, 8$ and $B = 8, 11, 15$ (both sorted).

| candidate $X$ | from | merge |
|---:|---|---|
| $8 - 3 = 5$ | $A_2$ | $1{+}5 = 6 \neq 8$ (skip), $3{+}5 = 8$ ✓, $4{+}5 = 9 \neq 11$ → second skip, **fails** |
| $8 - 1 = 7$ | $A_1$ | $1{+}7 = 8$ ✓, $3{+}7 = 10 \neq 11$ (skip), $4{+}7 = 11$ ✓, $8{+}7 = 15$ ✓ → **works** |

Output `7`: Bob dropped the $3$.
