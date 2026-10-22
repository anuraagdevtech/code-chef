---
topic: Basic Math
subtopic: Parity invariant plus a counting identity
time: $O(1)$ per test case
space: $O(1)$
---
Each operation shifts two numbers up and one down, so the **sum rises by exactly $1$** and every pairwise difference changes by $0$ or $\pm 2$. That gives the feasibility test immediately: the differences keep their parity forever, so all three numbers must already be congruent mod $2$. Otherwise print $-1$ — as in $1\,1\,2$ and $1\,2\,3$.

Now count. Suppose $k$ operations end with all three equal to $v$; then $3v = S + k$. If $A$ is the *decremented* number $d_A$ times, it is incremented the other $k - d_A$ times, so

$$v = A + (k - d_A) - d_A \quad\Longrightarrow\quad d_A = \frac{A + k - v}{2}$$

and likewise for $B, C$. These automatically sum to $k$, so the only requirements are that each is a non-negative integer. Integrality is exactly the parity condition again. Non-negativity binds hardest on the **smallest** number $m$:

$$m + k - v \geq 0 \quad\Longleftrightarrow\quad 2k \geq S - 3m$$

So the answer is the smallest $k \geq \max\!\left(0, \left\lceil \frac{S - 3m}{2} \right\rceil\right)$ with $k \equiv -S \pmod 3$. Once the $d$ values are fixed, any interleaving of the operations realises them, so no scheduling is needed.

For $3\,7\,3$: $S = 13$ forces $k \equiv 2 \pmod 3$, and $S - 3m = 4$ needs $k \geq 2$, so $k = 2$ — decrement the $7$ twice to reach $5\,5\,5$. For $4\,4\,4$ both conditions give $k = 0$.

The second bound genuinely matters: $1\,1\,11$ also has $k \equiv 2 \pmod 3$, but $S - 3m = 10$ forces $k \geq 5$, and indeed five operations give $6\,6\,6$.

## Edge cases

- **Pairwise parities never change.** Adding $1$ to two numbers and subtracting $1$ from the third shifts each difference by $0$ or $\pm 2$, so $A$, $B$ and $C$ must already share a parity — otherwise `-1`.
- **The total rises by exactly $1$ per operation**, so after $k$ operations $3V = A+B+C+k$ — which forces $k \equiv -(A+B+C) \pmod 3$.
- **A second bound comes from non-negativity.** The number subtracted from $s_X$ times satisfies $V = X + k - 2 s_X$, so $s_X \geq 0$ needs $V \leq \min + k$, giving $k \geq (\text{total} - 3\min)/2$.
- **So the answer is the smallest $k$ meeting both**: the ceiling of that bound, then raised to the right residue mod $3$.
- **Already equal** (the third row, $4,4,4$) → $0$, which both conditions allow.
- **The bound can be negative**, as when the numbers are already close, hence the clamp at $0$.
- **The residue adjustment can add up to $2$**, which is exactly what the second row needs: the bound gives $2$ and the residue happens to match.

## Dry run

Second sample: $A, B, C = 3, 7, 3$ — all odd, so feasible. Total $13$, minimum $3$.

| step | value |
|---|---|
| lower bound $\lceil (13 - 9)/2 \rceil$ | 2 |
| required residue $k \equiv -13 \equiv 2 \pmod 3$ | 2 ✓ |
| answer | `2` |

Check: $V = (13+2)/3 = 5$, with $s_B = 2$ and $s_A = s_C = 0$ — two operations, each adding to $A$ and $C$ and subtracting from $B$: $3,7,3 \to 4,6,4 \to 5,5,5$.
