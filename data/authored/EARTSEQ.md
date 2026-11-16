---
topic: Constructive
subtopic: Distinct large primes interleaved with a small cyclic colouring
time: $O(V\log\log V+\sum N)$ overall for fixed sieve bound $V=400000$
space: $O(V+\max N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Choose a circular sequence of edge primes $p_i$ such that every three consecutive edge primes are distinct, and assign vertex value $A_i=p_i p_{i+1}$. Neighbouring values share one edge prime. Three consecutive values have GCD one because no edge prime can appear in all three when the edge-prime sequence has no repeats within distance two.

For even lengths, alternate small primes with pairwise distinct large primes. Colour the circular small-prime positions alternately with two and three, using five at the final position when needed to avoid a repeated colour at the wraparound. Every large prime occurs once and has two different small neighbours, so all products are distinct.

For odd lengths at least five, first construct the even sequence of length $N-1$, then insert a small prime between the first large prime and its following small prime. Choose the inserted prime different from the small primes on either side of that large prime. This preserves distance-two distinctness. Length three uses edge primes two, three, and five directly. The largest large prime needed is below 400000, and every product is below two million.

## Edge cases

- Check the pair and triple conditions cyclically, including wraparound.
- Distinctness is required for all output values.
- The smallest case $N=3$ uses a separate construction.
- Every value remains below $10^9$.

## Dry run

For `N=5`, edge primes `[2,7,5,3,11]` yield values `[14,35,15,33,22]`. Adjacent GCDs are respectively `7,5,3,11,2`, while every cyclic triple has GCD one.
