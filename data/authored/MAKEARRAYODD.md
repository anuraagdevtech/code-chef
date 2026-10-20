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
