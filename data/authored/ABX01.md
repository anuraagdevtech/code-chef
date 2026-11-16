---
topic: Number Theory
subtopic: Digital root from modular exponentiation
time: $O(\log N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
A number and its digit sum have the same residue modulo nine. Repeating the digit sum therefore returns the unique digit from 1 through 9 with the same residue for a positive number.

Since $A$ and $N$ are positive, $A^N$ is positive. Compute its residue with modular exponentiation, and map residue zero to digit nine.

## Edge cases

- A positive multiple of nine has digital root nine, not zero.
- Never construct $A^N$.
- The original bounds exclude zero bases and zero exponents.

## Dry run

For `A=5,N=2`, `pow(5,2,9)=7`, so the answer is 7. For `7,2`, the residue is 4.
