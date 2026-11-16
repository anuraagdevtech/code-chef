---
topic: Dynamic Programming
subtopic: Memoised hash distributions per (length, number of A) with a max-convolution
time: $O(N \cdot A^2 \cdot H)$ in the worst case over all states, $H$ the largest hash value
space: $O(N \cdot A \cdot H)$ for the memo table
complexity_note: Auxiliary space excludes the buffered input and output.
---
The split depends only on the length, so the multiset of hash values of all strings with a given length $n$ and a given number $a$ of `A`s is a function of $(n, a)$ alone. Let `distribution(n, a)[v]` be the number of such strings with hash $v$.

For $n \le 1$ the hash equals $a$. Otherwise the left half has length $\lfloor n/2 \rfloor$; enumerate how many `A`s, $x$, go there. The hash is $a + \max(h_1, h_2)$, so we need the number of pairs (left string, right string) whose maximum hash is exactly $v$:

$$\#\{\max = v\} = f_v \cdot G_v + g_v \cdot F_{v-1},$$

with $F, G$ the running prefix sums of the two distributions. Only $O(\log N)$ distinct lengths ever appear, so the memo table is small and is shared by all test cases.

## Edge cases

- Requests with $V$ larger than any achievable hash, or with impossible counts, answer 0.
- The single-character and empty strings are base cases: hash 1 for `A`, 0 otherwise.
- In the max-count formula the tie $h_1 = h_2 = v$ must be counted once - one side uses the inclusive prefix sum, the other the exclusive one.
- Counts are taken modulo $10^9 + 7$.

## Dry run

`A = 1, E = 1, V = 2`. Length 2 splits into two single characters.

- `AE`: halves hash to 1 and 0, so the hash is $1 + \max(1, 0) = 2$.
- `EA`: halves hash to 0 and 1, so the hash is again 2.

`distribution(2, 1) = [0, 0, 2]`, so the answer is 2.
