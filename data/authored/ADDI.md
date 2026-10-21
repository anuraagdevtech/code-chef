---
topic: Bit Manipulation
subtopic: Zero bits inside the binary width
time: $O(1)$ per test case
space: $O(1)$
---
"Unset bits" means the zeros in $N$'s binary representation **as written**, i.e. within its own width — leading zeros do not count, otherwise every answer would depend on an arbitrary word size.

The width is $\mathrm{bitlen}(N) = \lfloor \log_2 N \rfloor + 1$, and the number of ones is the population count, so

$$\text{answer} = \mathrm{bitlen}(N) - \mathrm{popcount}(N)$$

Python gives both directly: `n.bit_length()` and `n.bit_count()`.

For $N = 10 = 1010_2$ the width is $4$ and two bits are set, giving $2$. For $N = 1 = 1_2$ the width is $1$ with one bit set, giving $0$ — the smallest case, and the one that shows why counting against a fixed 64-bit word would be wrong (it would report $63$).

Since $N \leq 10^{18} < 2^{60}$, the answer never exceeds $59$. In C++ this is `63 - __builtin_clzll(n) + 1 - __builtin_popcountll(n)`; Python's arbitrary-precision integers make the width query exact without any clz juggling.

The statement's input description is garbled — it says the second line holds a single $N$ — but the actual format is $T$ followed by $T$ lines, each with one $N$, as the sample shows.
