---
topic: Strings
subtopic: Forcing a palindrome to be impossible
time: $O(N)$ per test case
space: $O(1)$
---
A multiset rearranges into a palindrome exactly when at most one character has an odd count. So an **anti**-palindrome needs at least two odd counts — and since the counts sum to $N$, the number of odd counts $k$ has the same parity as $N$. The targets are therefore:

- $N$ even → need $k \geq 2$ (and $k$ is even, so $k = 0$ is the only failure)
- $N$ odd → need $k \geq 3$ (and $k$ is odd, so $k = 1$ is the only failure)

**$N$ even, $k = 0$.** One edit fixes it: take a character from some letter with a positive even count and write a letter not yet used. Both counts flip to odd, giving $k = 2$.

**$N$ odd, $k = 1$.** Here the answer depends on what else is present. An edit changes two counts, each flipping parity, so $k$ moves by $-2$, $0$ or $+2$ — and reaching $3$ needs a $+2$, which requires taking from a letter whose count is **even**. If some even-count letter exists (necessarily with count $\geq 2$), one edit does it.

But if the string is a **single repeated letter**, the only non-zero count is the odd one, and there is nothing even to draw from. The first edit merely moves the oddness around, leaving $k = 1$; a second then reaches $k = 3$. That is sample case 4, `aaa`, which costs $2$ — the case that defeats a naive "$\lceil (3-k)/2 \rceil$" formula.

The remaining samples cover the rest: `ab` and `abc` are already anti-palindromes at $k = 2$ and $k = 3$; `aa` is the even-$N$ repair at $1$; and `abb` has an even-count `b` to draw from, so also $1$.
