---
topic: Constructive
subtopic: Parity of the edge count and vertex degrees
time: $O(N+M)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If $M$ is even, one part already works. If $M$ is odd and some vertex has odd degree, place it alone: removing its incident odd number of edges leaves an even number in the other part.

If every degree is even, two parts cannot work: any cut has even size, so its two induced edge counts sum to an odd number. Three parts suffice. Choose any edge $(u,v)$ and put its endpoints in separate singleton parts. Removing their incident edges deletes $deg(u)+deg(v)-1$ edges, an odd number, leaving an even edge count in the remaining part.

## Edge cases

- Singleton parts have zero edges, which is even.
- Use any input edge when all degrees are even and $M$ is odd.
- Isolated vertices may remain in the main part.

## Dry run

In the sample, $M=5$ and vertex 2 has degree three. Put vertex 2 alone; the other part retains two edges, so two parts suffice.
