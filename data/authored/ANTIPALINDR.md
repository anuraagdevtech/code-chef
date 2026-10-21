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

## Edge cases

- **A multiset can be arranged into a palindrome exactly when at most one character has an odd count**, so the goal is to push the odd-count total to $2$ or more.
- **The parity of the odd-count total is fixed by $N$.** For even $N$ it is always even, so the only bad value is $0$ and one edit lifts it straight to $2$ (one count drops to odd, a new one rises to odd). For odd $N$ it is always odd, so the only bad value is $1$ and the target is $3$.
- **A single repeated character is the hard case.** With odd $N$ and one distinct letter — `aaa` — any single edit leaves counts $\{N-1, 1\}$, which is still one odd count, so it takes two edits. This is the only input needing more than one.
- **Two or more distinct letters with one odd count always costs one edit**: some letter has an even count of at least $2$, and changing one of its occurrences to a fresh letter creates two new odd counts. The fifth row (`abb`) is this case.
- **Already anti-palindromic** → $0$ (rows $1$ and $3$).
- **Twenty-six letters are available**, so a fresh letter for the edit always exists.
- **The test count is named $C$** rather than $T$, and there is no separate bound on it beyond $5 \cdot 10^5$.

## Dry run

| $N$ | $S$ | counts | odd counts | needed | output |
|---:|---|---|---:|---|---:|
| 2 | `ab` | $1, 1$ | 2 | $\geq 2$ ✓ | `0` |
| 2 | `aa` | $2$ | 0 | $\geq 2$ | `1` |
| 3 | `abc` | $1,1,1$ | 3 | $\geq 3$ ✓ | `0` |
| 3 | `aaa` | $3$ | 1 | $\geq 3$, one letter only | `2` |
| 3 | `abb` | $1, 2$ | 1 | $\geq 3$, `b` has an even count | `1` |

For row 4, one edit gives `aab` (counts $2, 1$, still one odd); two edits give `abc`.
