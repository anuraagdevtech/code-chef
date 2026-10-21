---
topic: Bit Manipulation
subtopic: Tracking a single bit through XOR and OR
time: $O(N)$ per test case
space: $O(1)$
---
Only the lowest bit matters, so look at what the operation does to it. Setting both entries to $(A_i \oplus A_j) \mid X$ gives a result whose parity is

$$\bigl(\mathrm{lsb}(A_i) \oplus \mathrm{lsb}(A_j)\bigr) \;\lor\; \mathrm{lsb}(X)$$

That splits cleanly on the parity of $X$.

**$X$ odd.** The OR forces the low bit to $1$ regardless of the operands, so *any* operation makes both chosen elements odd. Each move can fix two evens at once, so with $e$ even elements the answer is $\lceil e/2 \rceil$. When $e$ is odd the final move pairs the last even with an already-odd element — harmless, since that element stays odd.

**$X$ even.** The OR contributes nothing to the low bit, so the result is odd only when exactly **one** of the two operands is odd. Each operation therefore consumes one odd partner and converts one even element, reducing the even count by exactly one: the answer is $e$. And if the array contains no odd element at all, no operation can ever produce one — the parity is stuck — so the answer is $-1$.

The all-even, even-$X$ case is the only impossible one, and it is the thing to check for.

Sample case 1 has every element odd already, so $0$ operations regardless of $X$. Sample case 2 has $X = 4$ (even) with two evens and three odds, giving $2$ — one operation per even element.

Counting parities is a single pass; nothing else about the values matters, which is what keeps this $O(N)$ at $\sum N = 10^5$.

## Edge cases

- **Everything already odd** → $0$ operations, which must be checked before anything else.
- **$X$ odd**: the `| X` forces the low bit on regardless of the XOR, so *any* pair becomes odd — including a pair of two evens. One operation therefore fixes two elements, giving $\lceil \text{evens}/2 \rceil$, and a lone leftover even can be paired with an already-odd element at no extra cost.
- **$X$ even with every element even** → $-1$. The low bit of the result is $a_0 \oplus b_0 = 0$, so two evens stay even and no odd can ever be created.
- **$X$ even with at least one odd**: pairing an even with an odd gives a low bit of $0 \oplus 1 = 1$, so both come out odd — one operation per even element, and the odd count only grows, so a partner is always available. The answer is exactly the number of evens.
- **The two indices must be distinct**, which matters only for $N = 1$; the constraints guarantee $N \geq 2$.
- **Only the low bit of $X$ matters**, so the other $29$ bits never enter the reasoning.

## Dry run

Second sample: $X = 4$ (even), $A = 2, 3, 4, 17, 9$.

| element | parity |
|---:|---|
| 2 | even |
| 3 | odd |
| 4 | even |
| 17 | odd |
| 9 | odd |

Two evens, and odd partners exist, so two operations:

| operation | result |
|---|---|
| pair $2$ with $3$: $(2 \oplus 3) \mid 4 = 1 \mid 4 = 5$ | both become $5$ (odd) |
| pair $4$ with $9$: $(4 \oplus 9) \mid 4 = 13 \mid 4 = 13$ | both become $13$ (odd) |

Output `2`.
