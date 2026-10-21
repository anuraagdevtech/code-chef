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
