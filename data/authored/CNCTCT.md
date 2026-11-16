---
topic: Disjoint Set Union
subtopic: Kruskal over bits - each bit is a clique of equal-weight edges
time: $O(30 \cdot N \cdot \alpha(N))$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A road of length $L$ between $X$ and $Y$ needs $L$ to be a non-empty submask of $A_X \mathbin{\&} A_Y$. The cheapest such road is a single bit, the lowest common set bit, and any other allowed length is at least as large; so only single-bit roads are useful, and a road of length $2^b$ exists between any two cities that both have bit $b$.

For each bit $b$ the cities having it therefore form a clique of edges of weight $2^b$. Run Kruskal's algorithm in increasing order of weight, i.e. bit by bit from the lowest. Within a clique all edges have the same weight, and joining every city of the clique to one representative produces the same components as processing all of its edges, so each bit needs only a linear scan with a disjoint-set union. Every successful union adds $2^b$.

If more than one component remains at the end, the cities cannot be connected.

## Edge cases

- A city with significance 0 can never be connected; with $N > 1$ the answer is $-1$.
- $N = 1$ needs no road: answer 0.
- Processing the bits from low to high is exactly the sorted edge order Kruskal requires.
- The total can exceed 32 bits.

## Dry run

`A = [2, 4, 6]`.

- bit 1 (weight 2): cities 1 and 3 have it - union, cost 2.
- bit 2 (weight 4): cities 2 and 3 have it - union, cost 4.

One component remains. Answer 6.
