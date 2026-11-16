---
topic: Bit Manipulation
subtopic: Column addition from the lowest bit - each bit of X is forced
time: $O(\log \max(A, B, C))$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Add $(A \oplus X)$ and $(B \oplus X)$ column by column from the lowest bit, with a carry. In column $k$ the sum bit is

$$(a_k \oplus x_k) \oplus (b_k \oplus x_k) \oplus \text{carry} = a_k \oplus b_k \oplus \text{carry},$$

which does not depend on $x_k$ at all. It has to equal the bit of $C \oplus X$, namely $c_k \oplus x_k$, so

$$x_k = a_k \oplus b_k \oplus c_k \oplus \text{carry}$$

is forced. The carry into the next column is then determined as well: it is 1 when at least two of $a_k \oplus x_k$, $b_k \oplus x_k$ and the old carry are 1.

So there is exactly one candidate $X$, built bit by bit. Above the highest bit of the inputs all three bits are 0: if the carry is 0 there, $x$ stays 0 and everything is consistent; if the carry is 1, then $x_k = 1$, both summands get a 1 and the carry is 1 again - it never dies, so no finite $X$ exists. The loop therefore runs a couple of bits past the input width and answers YES exactly when the carry has vanished.

## Edge cases

- $X = 0$ works whenever $A + B = C$, and the procedure finds it.
- $A = B = C = 0$: YES.
- A carry surviving past the top bit means NO, however many more bits are examined.
- The inputs are below $2^{27}$; 29 columns are processed.

## Dry run

`A = 1, B = 6, C = 6`:

| bit | a b c | carry in | x | summand bits | carry out |
|---:|---|---:|---:|---|---:|
| 0 | 1 0 0 | 0 | 1 | 0, 1 | 0 |
| 1 | 0 1 1 | 0 | 0 | 0, 1 | 0 |
| 2 | 0 1 1 | 0 | 0 | 0, 1 | 0 |

The carry is 0 at the end: YES with $X = 1$, and indeed $(1 \oplus 1) + (6 \oplus 1) = 0 + 7 = 7 = 6 \oplus 1$.
