---
topic: Hashing
subtopic: Sliding window over the prefix xors of the doubled array
time: $O(N)$ expected per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Write the array twice and let $P$ be the prefix-xor array of the doubled array, $P_0 = 0$. The rotation that starts at position $i$ has prefix xors

$$P_{i+1} \oplus P_i,\; P_{i+2} \oplus P_i,\; \dots,\; P_{i+N} \oplus P_i .$$

Xor with the fixed value $P_i$ is a bijection, so the number of distinct values among them equals the number of distinct values in the window $P_{i+1}, \dots, P_{i+N}$.

So the answer is the maximum number of distinct values in a window of length $N$ sliding over $P_1, \dots, P_{2N-1}$. Maintain a frequency table of the window: when it moves by one, decrement the outgoing value (deleting it when it reaches zero) and increment the incoming one; the number of keys is the current count. Every right shift is one of these $N$ rotations.

## Edge cases

- All elements 0: every prefix xor is 0 and the answer is 1.
- Values go up to $2^{60}$, so a hash map is used rather than an array.
- Only $N$ different rotations exist.
- The common xor constant can be ignored entirely.

## Dry run

`A = [1, 2, 2, 8]`. Doubled prefix xors $P_1 \dots P_8$: `1 3 1 9 8 10 8 0`.

- window $P_1..P_4$ = `1 3 1 9`: 3 distinct
- window $P_2..P_5$ = `3 1 9 8`: 4 distinct

Four is the maximum possible for $N = 4$. Answer 4.
