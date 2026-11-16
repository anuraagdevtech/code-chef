---
topic: Graphs
subtopic: Flood-fill nonprime parity components in row-major order
time: $O(V\log\log V+\pi(V)+K\log\pi(V)+\sum N^2)$ overall for $K$ prime cells and maximum password $V$
space: $O(V+\pi(V)+\sum N^2)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Sieve the primes up to the maximum input password. Prime servers must each be cracked individually; a prime's unsuccessful-try count is its zero-based index in the sorted prime list.

An even nonprime password $p$ costs $p/2$ failed tries. An odd nonprime password costs $\lfloor p/2\rfloor+2$, since the next even guess overshoots and is followed by the correct odd guess. Scan cells in row-major order. The first uncracked nonprime cell pays its own cost, then flood-fill and mark its entire four-neighbour component of the same nonprime parity. The component's minimum password is irrelevant: the mandated first cell determines the cost.

## Edge cases

- Two is a prime, not an even server.
- Zero is an even nonprime; one is an odd nonprime.
- Prime cells block parity-component propagation.
- Components pay the cost of their first row-major cell.

## Dry run

In sample two, password 8 is the first cell of the even component and costs four tries. It cracks both password-4 cells as well. Password 15 costs nine tries, giving total 13.
