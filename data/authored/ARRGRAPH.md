---
topic: Constructive
subtopic: Check coprime connectivity, then add a universal prime
time: $O(N^2\log V)$ per test case with $V=50$
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
First traverse the implicit graph, adding an edge whenever two values have GCD one. If it is connected, no changes are necessary.

Otherwise one change always suffices. If 47 is absent, replace one value by 47: among allowed values 2 through 50, only 47 itself shares a factor with 47, so the new vertex is adjacent to every other vertex. If 47 is already present in a disconnected graph, every value must be 47, since any other value would connect all 47 vertices. Replace one occurrence by 43, producing a connected star. Thus the minimum is exactly zero or one.

## Edge cases

- A single vertex is connected without changes.
- Every output value must stay between 2 and 50.
- Merely checking the GCD of all elements is insufficient for graph connectivity.

## Dry run

For `[2,3]`, the GCD-one edge already connects both vertices. For `[2,4]`, replace one value by 47; it is coprime with the other, so one change suffices.
