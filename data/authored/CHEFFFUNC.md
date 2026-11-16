---
topic: Bit Manipulation
subtopic: Closed forms for f and g, and only O(log R) candidates
time: $O(\log R)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Unrolling the recursions over the binary digits of $x$ (a $k$-bit number):

- $f$ adds 1 for every 0 digit below the leading one: $f(x) = k - \text{popcount}(x)$.
- $g$ rebuilds the number with all digits below the leading one flipped: $g(x) = 3 \cdot 2^{k-1} - 1 - x$.

So within a fixed bit length we want to minimise $x + \text{popcount}(x)$, and longer numbers have a much larger constant term.

Take any $x > L$ in the range and look at the highest bit where $x$ and $L$ differ; $x$ has a 1 there and $L$ a 0. Clearing all lower bits of $x$ keeps it above $L$, keeps its bit length, and reduces both $x$ and its popcount. Hence some optimum is either $L$ itself or $L$ rounded up to a multiple of $2^j$ for some $j$. These are $O(\log R)$ candidates - they include the powers of two where the bit length changes - and each one that does not exceed $R$ is evaluated with the closed forms.

## Edge cases

- $L = R$: only one candidate.
- Rounding up with $j = 0$ gives $L$ itself.
- A power of two inside the range is usually the best choice for its bit length: $x$ and the popcount are both minimal.
- Candidates beyond $R$ are discarded.

## Dry run

`L = 1, R = 20`. Candidates are 1 rounded up to multiples of 1, 2, 4, 8, 16, 32: `1, 2, 4, 8, 16` (32 is too large).

For $x = 16$ ($k = 5$): $g = 3 \cdot 16 - 1 - 16 = 31$ and $f = 5 - 1 = 4$, total 35. The other candidates give 1, 4, 9 and 18.

Answer 35.
