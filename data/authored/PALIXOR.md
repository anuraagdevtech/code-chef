---
topic: Bit Manipulation
subtopic: Counting pairs by xor value, directly or with a Walsh-Hadamard transform
time: $O(\min(D \cdot P,\; U \log U))$ per test case with $D$ distinct values, $P$ palindromes below $U = 2^{15}$
space: $O(U)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
All values are below $2^{15}$, so the xor of a pair is too, and there are only a few hundred decimal palindromes in that range. Count the ordered pairs $(i, j)$ whose xor is a palindrome; the pairs with $i = j$ have xor 0, a palindrome, and are counted once, while every other unordered pair is counted twice. Hence the required number of pairs with $i \le j$ is (ordered $+ N$) / 2.

Two ways to count the ordered pairs, chosen by size:

- few distinct values: for every distinct value $x$ and every palindrome $p$, add `freq[x] * freq[x ^ p]`;
- many distinct values: the xor-convolution of the frequency array with itself gives the number of ordered pairs for every xor value at once. It is computed with the Walsh-Hadamard transform - transform, square pointwise, transform again, divide by $U$ - and then summed over the palindromes.

## Edge cases

- 0 is a palindrome, so every element pairs with itself and equal elements pair with each other.
- The inverse Walsh-Hadamard transform is the same transform followed by a division by the size.
- Single-digit xor values are palindromes too.
- The direct method is used whenever it is cheaper, which keeps small tests fast.

## Dry run

`A = [2, 2, 2]`. One distinct value with frequency 3.

Ordered pairs with a palindromic xor: only $p = 0$ contributes, $3 \cdot 3 = 9$.

Answer $(9 + 3) / 2 = 6$ - all pairs $i \le j$.
