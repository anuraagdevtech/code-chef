---
topic: Number Theory
subtopic: Largest multiplier coprime to the ratio of consecutive prefix gcds
time: $O(N \log M)$ per test case plus the short downward searches
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
$B_1 = A_1$ is forced. For $i \ge 2$, $A_i$ must divide $B_i$, so write $B_i = A_i \cdot t$. The condition $\gcd(A_{i-1}, B_i) = A_i$ then becomes

$$\gcd\Bigl(\frac{A_{i-1}}{A_i},\; t\Bigr) = 1.$$

The prefix gcds are given, so the choice of $B_i$ does not influence any later position; each position can be maximised on its own, which also gives the lexicographically largest array. Start from the largest possible multiplier $t = \lfloor M / A_i \rfloor$ and decrease it until it is coprime to the ratio $A_{i-1} / A_i$.

The search is short: $t = 1$ always works, and coprime values are dense - consecutive integers are coprime to each other, so the gaps between admissible $t$ stay small in practice.

## Edge cases

- $A_i = A_{i-1}$: the ratio is 1 and the largest multiple of $A_i$ not exceeding $M$ is taken.
- The first element has no freedom at all.
- $t = 1$ (i.e. $B_i = A_i$) is always valid, so the loop terminates.
- The input guarantees $A_i$ divides $A_{i-1}$.

## Dry run

`M = 5, A = [2, 2, 2, 2]`.

$B_1 = 2$. For the other positions the ratio is $2/2 = 1$ and the largest multiplier is $\lfloor 5/2 \rfloor = 2$, coprime to 1, so $B_i = 4$.

Output `2 4 4 4`. With `M = 2, A = [2, 1]`: ratio 2, multiplier starts at 2 (not coprime) and drops to 1, giving `2 1`.
