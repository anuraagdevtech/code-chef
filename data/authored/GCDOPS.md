---
topic: Constructive
subtopic: Each reduction has a self-fixing pivot
time: $O(N)$ per test case
space: $O(1)$
---
The whole problem reduces to one test:

$$B_i \mid i \quad \text{for every } i$$

**Necessity.** Initially $A_i = i$, and an operation replaces a value by a gcd of it with something else, which still divides the old value. So $A_i \mid i$ is an invariant, and $B_i$ must divide $i$. (The given bound $B_i \leq i$ is weaker — sample 1 fails on $B_3 = 2$, which is below $3$ but does not divide it.)

**Sufficiency** is the constructive half, and the trick is choosing the partner well. To reduce index $i$ to $B_i < i$, operate on $i$ and the index $p = B_i$. Since $A_p = p = B_i$ divides $i$,

$$\gcd(A_i, A_p) = \gcd(i, B_i) = B_i$$

so $A_i$ lands on $B_i$ — and $A_p$ is set to $B_i = p$, i.e. **unchanged**. One operation per index, with no collateral damage. The partner is valid because $p = B_i < i$, so $p \neq i$, and $p \leq N$.

The one ordering subtlety: the pivot $p$ must still hold its original value $p$. It loses that only when $p$ itself gets reduced, and $B_p < p$ then. So process indices in **decreasing** order — every pivot is smaller than its target, hence reduced only later. The dependency graph $i \to B_i$ points strictly downward, so there is never a cycle.

Sample 2 is this construction in one step: $B = [1,2,3,2]$ needs only index $4$ lowered to $2$, and operating on indices $4$ and $2$ gives $\gcd(4,2) = 2$, leaving $A_2$ at $2$. Sample 1 fails the divisibility test outright.

Note $B_1 = 1$ is forced by the constraints, which is consistent — $A_1$ can never move.
