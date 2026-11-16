---
topic: Number Theory
subtopic: Reduce scaled triples to divisor summatory counts
time: $O(V\log V+T\sqrt V)$ overall for $V=\max N$
space: $O(V+T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Fix $C$ and write $B=kC$ with $k\ge2$. The congruence $A\bmod B=C$ means $A=C+qB$. With $m=\lfloor N/C\rfloor$, there are $\lfloor(m-1)/k\rfloor+1$ choices for $A$. Summing over $k=2$ through $m$ simplifies to $D(m-1)=\sum_{j=1}^{m-1}\lfloor(m-1)/j\rfloor$.

Precompute $D$ as the prefix sum of ordinary divisor counts using a divisor sieve. The answer is $\sum_{C=1}^{\lfloor N/2\rfloor}D(\lfloor N/C\rfloor-1)$. Group consecutive $C$ values having the same quotient $N//C$, giving only square-root many groups per query.

## Edge cases

- $C$ is positive and strictly smaller than $B$.
- $A=C$ is valid when $A<B$; it corresponds to $q=0$.
- Triple counts are exact integers without a modulus.

## Dry run

For `N=4`, `C=1` contributes `D(3)=5` triples and `C=2` contributes `D(1)=1`, giving six.
