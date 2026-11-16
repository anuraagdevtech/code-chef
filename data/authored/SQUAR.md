---
topic: Number Theory
subtopic: Group by square-free kernel and take the largest non-trivial group
time: $O(V \log \log V + N \log V)$, $V$ the largest value in the input
space: $O(V + N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The square-free kernel of a number is the product of the primes that occur in it with an odd exponent; a number is a perfect square exactly when its kernel is 1, and a product of two numbers is a perfect square exactly when their kernels are equal.

Apply the conditions to subsequences of length 1 and 2: no element may be a perfect square, and every two elements must have the same kernel. Conversely, if all elements share a kernel $k \ne 1$, then a product of $m$ of them is $k^m$ times a perfect square - a square for even $m$ and a non-square for odd $m$. So squarified subsequences are exactly the sets of elements with one common kernel different from 1.

Compute every kernel with a smallest-prime-factor sieve and print the largest multiplicity among the kernels other than 1 (0 if there is none). The sieve is sized by the largest number in the whole input, which is read up front.

## Edge cases

- Perfect squares, including 1, can never be used.
- If every element is a perfect square the answer is 0.
- A single non-square element gives a valid subsequence of length 1.
- The sieve only stores a factor for composites; a zero entry means the number is prime.

## Dry run

`A = [27, 8, 12, 16, 12]`.

Kernels: $27 = 3^3 \to 3$, $8 = 2^3 \to 2$, $12 = 2^2 \cdot 3 \to 3$, $16 = 2^4 \to 1$, $12 \to 3$.

Kernel 3 occurs three times, kernel 2 once, and the kernel 1 is ignored. Answer 3 (`27, 12, 12`).
