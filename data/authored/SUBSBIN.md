---
topic: Constructive
subtopic: Fix the imbalance one unit per operation, then collapse the whole string
time: $O(N^2)$ per test case with $N \le 1000$
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
An operation removes a balanced substring and inserts one bit, so it changes (number of zeros $-$ number of ones) by exactly one, in either direction.

If the string contains only one kind of bit, no balanced substring exists and nothing can be done: the answer is the length itself with 0 operations.

Otherwise the string can be reduced to length 1: the last operation must take the whole current string, which therefore has to be balanced. If the initial imbalance is $d$, at least $d$ operations are needed before that, for a total of at least $d + 1$. This bound is reached: while the string is unbalanced it still contains both bits, hence an adjacent pair `01` or `10`; replace that pair by the minority bit, which removes one majority bit and lowers the imbalance by one. After $d$ such steps the string is balanced and one final operation replaces it by a single bit.

## Edge cases

- A uniform string (including length 1) prints its length and 0 operations.
- An already balanced string needs exactly one operation.
- Indices in later operations refer to the current, already shortened string.
- Many operation sequences are optimal, so the output is validated by a checker.

## Dry run

`S = 11000`: two ones, three zeros, imbalance 1, minority bit `1`.

- The first unequal adjacent pair is at positions 2-3 (`10`); replace it by `1`: the string becomes `1100`. Operation `2 3 1`.
- Now balanced: replace positions 1-4 by `0`. Operation `1 4 0`.

Output `1 2` followed by the two operations.
