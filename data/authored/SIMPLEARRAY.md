---
topic: Combinatorics
subtopic: Independent choices per pair of complementary remainders
time: $O(N + K)$ per test case
space: $O(K)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Two elements have a sum divisible by $K$ exactly when their remainders $r$ and $s$ satisfy $r + s \equiv 0 \pmod K$. So group the elements by remainder; a conflict only ever involves the classes $r$ and $K - r$.

- Remainder 0 (and remainder $K/2$ when $K$ is even) conflicts with itself: at most one element of the class may be chosen, $c + 1$ possibilities.
- For $0 < r < K/2$ the classes $r$ and $K - r$ conflict with each other but not internally: choose any subset of one class or any subset of the other. That is $2^{c_r} + 2^{c_{K-r}} - 1$ possibilities, the empty choice being counted once.

Different pairs of classes are independent, so the answer is the product of these factors; the empty subsequence is included automatically.

## Edge cases

- $K = 1$: every pair conflicts, so the answer is $N + 1$.
- $K = 2$: both classes are self-conflicting.
- Equal values at different indices are different elements.
- Powers of two are taken modulo $10^9 + 7$.

## Dry run

`A = [4, 5, 7]`, `K = 4`: remainders `0, 1, 3`.

- remainder 0: one element, factor $1 + 1 = 2$.
- pair (1, 3): one element each, factor $2 + 2 - 1 = 3$.

Answer $2 \cdot 3 = 6$ - all subsets except those containing both 5 and 7.
