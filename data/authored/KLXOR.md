---
topic: Bit Manipulation
subtopic: XOR prefix parity for each output position
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For zero-based output position $j$, the contributing characters are $S_j,S_{j+1},\ldots,S_{j+N-K}$. They form one contiguous window of length $N-K+1$ in the original string.

Build prefix XORs of the bits. The $j$-th output bit is the XOR of that window, found from two prefix values. Sum these bits over the $K$ output positions.

## Edge cases

- For $K=N$, each output bit is the original bit.
- For $K=1$, only the parity of all input bits matters.
- Substrings overlap but each contributes independently.

## Dry run

For `1001`, $K=2$, the contributing windows are `100` and `001`; both have XOR one. The output has two ones.
