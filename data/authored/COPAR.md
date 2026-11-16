---
topic: Number Theory
subtopic: Each prime spans an interval - find the first position no interval crosses
time: $O(V \log \log V + N \log V)$, $V$ the largest value
space: $O(V + N \log V)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The two products are coprime exactly when no prime divides an element on both sides of the cut. For each prime $p$ look at the first and the last index where it divides an element: a cut is valid when it does not fall strictly inside any such span.

Factorise every element with a smallest-prime-factor sieve and record the last index of each prime. Then scan from the left keeping `end`, the furthest last-occurrence of any prime seen so far. The prefix ending at $i$ is a valid piece exactly when $i = \text{end}$: no prime that appears in the prefix appears later. The first such $i$ gives the smallest valid $l$, which is what is asked; the statement guarantees that one exists before the end of the array.

## Edge cases

- Elements equal to 1 have no primes and never extend the span.
- The cut must leave both pieces non-empty; the guaranteed answer satisfies this.
- Repeated prime factors of one element are recorded once.
- Products are never formed - they would be astronomically large.

## Dry run

`A = [2, 3, 4, 5]`. Last occurrences: prime 2 at index 3 (the 4), prime 3 at index 2, prime 5 at index 4.

- $i = 1$ (value 2): `end = 3`.
- $i = 2$ (value 3): `end` stays 3.
- $i = 3$ (value 4): `end = 3 = i` - cut here.

Answer $l = 3$: $2 \cdot 3 \cdot 4 = 24$ and 5 are coprime.
