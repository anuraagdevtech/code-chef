---
topic: Number Theory
subtopic: GCD of the displacements
time: $O(N \log N)$ per test case
space: $O(1)$
---
A swap at distance $K$ moves an element by $K$ positions, so an element can only ever reach indices **congruent to its own mod $K$**. The index classes mod $K$ are therefore independent, and within one class the distance-$K$ swaps act as adjacent transpositions, which generate every permutation of that class. So sorting is possible exactly when every element's target index matches its current index mod $K$:

$$K \mid (P_i - i) \quad \text{for every } i$$

That makes $K$ a common divisor of all the displacements, so the largest workable value is

$$K = \gcd_i \bigl(|P_i - i|\bigr)$$

taking $\gcd(0, x) = x$ so that already-correct positions impose nothing. The permutation is guaranteed unsorted, so at least one displacement is non-zero and the GCD is positive — and since $|P_i - i| \leq N-1$, the result never exceeds $N-1$, which is the largest $K$ for which a swap even exists.

Note the two directions matter equally: divisibility is *necessary* because of the residue classes, and *sufficient* because each class can be sorted internally — neither half alone would justify taking the GCD.

The samples show the range. $[4,2,3,1]$ displaces only the ends, by $3$ each, so $K = 3$: one swap of positions $1$ and $4$ sorts it. $[1,4,3,2,5]$ displaces two elements by $2$, giving $K = 2$. And $[2,1]$ has displacements $1$ and $1$, so $K = 1$ — adjacent swaps, the weakest operation, are all that works.
