---
topic: Brute Force
subtopic: Residues repeat with period three - try all nine patterns
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If windows $[i, i+2]$ and $[i+1, i+3]$ both have sums divisible by 3, subtracting them gives $A_{i+3} \equiv A_i \pmod 3$. So in a valid array the residues are periodic with period 3, and the three residues $r_0, r_1, r_2$ of one period must satisfy $r_0 + r_1 + r_2 \equiv 0$. Conversely any such periodic pattern is valid.

Only increments are allowed, so bringing an element with residue $a$ to residue $v$ costs $(v - a) \bmod 3$. For each position class $i \bmod 3$ and each target residue accumulate the total cost in a $3 \times 3$ table. Then try all nine choices of $(r_0, r_1)$, with $r_2 = (-r_0 - r_1) \bmod 3$ forced, and take the cheapest.

## Edge cases

- Only additions are allowed; lowering a residue by 1 costs 2.
- $N = 3$ has a single window but the same formula applies.
- The values themselves are irrelevant beyond their residues.
- The cost can be as large as $2N$.

## Dry run

`A = [1, 2, 3]`: residues `1 2 0`.

Choosing the pattern $(1, 2, 0)$ costs nothing and $1 + 2 + 0 \equiv 0$, so the answer is 0.

For `A = [1, 1, 1, 2]` (residues `1 1 1 2`): the pattern $(1, 1, 1)$ is valid and only the last element, in class 0, has to move from 2 to 1, costing 2; the pattern $(2, 0, 1)$ costs $1 + 2 + 0 + 0 = 3$. The answer is 2.
