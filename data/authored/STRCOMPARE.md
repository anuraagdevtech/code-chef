---
topic: Strings
subtopic: Suffix comparison answered by one backward pass
time: $O(N)$ per test case
space: $O(1)$
---
The two suffixes $A[i..N]$ and $B[i..N]$ have the same length, so the comparison is settled by the **first position where they differ**. That makes the answers chain backwards:

$$\mathrm{less}[i] = \begin{cases} [\,A_i < B_i\,] & A_i \neq B_i \\ \mathrm{less}[i+1] & A_i = B_i \end{cases}$$

with $\mathrm{less}[N+1] = \text{false}$, since two empty suffixes are equal rather than strictly ordered. So a single right-to-left sweep decides every index in $O(1)$, and the answer is the number of true entries.

The recurrence is the whole algorithm — there is no need for suffix arrays, hashing, or any comparison beyond one character per index, which matters with $\sum N$ up to $10^6$.

Note the `false` base case: a tie all the way to the end means the suffixes are equal, and equality does not count as "less than". That is why the shorter sample answers are what they are.

For $A = \texttt{ab}$ and $B = \texttt{bb}$: position $2$ has `b` against `b`, so it inherits `false` from the empty suffix; position $1$ has `a < b`, so it is true. Answer $1$.

For $A = \texttt{aaa}$ and $B = \texttt{aab}$: position $3$ has `a < b`, true; positions $2$ and $1$ tie and inherit that truth. All three indices qualify, giving $3$ — the single difference at the very end propagates all the way left.

## Edge cases

- **One backward pass answers every suffix.** Suffixes of equal length compare on their first differing character, so scanning right to left and remembering the verdict at the most recent mismatch gives each index's answer in constant time.
- **Equal suffixes do not count**, which is why the carried verdict starts as false — a run of matching characters at the tail contributes nothing until a mismatch appears.
- **A mismatch overwrites the verdict**, it does not combine with it: the character at position $i$ decides outright, and everything to its right becomes irrelevant.
- **Identical strings give $0$**, since no mismatch ever sets the flag.
- **A mismatch at the very front flips only one suffix**, while one at the very back flips all $N$ — which is the second sample, where `aaa` against `aab` differs only at the last character and answers $3$.
- **The comparison is on bytes**, so no decoding is needed over up to $10^6$ characters.
- **Sum of $N \leq 10^6$**: one pass, with the running total accumulated as a boolean.

## Dry run

Second sample: $A = $ `aaa`, $B = $ `aab`.

| $i$ | $A_i$ | $B_i$ | mismatch? | verdict after | counted |
|---:|---|---|:---:|---|---:|
| 3 | `a` | `b` | yes | `a` $<$ `b` → true | 1 |
| 2 | `a` | `a` | no | carried: true | 2 |
| 1 | `a` | `a` | no | carried: true | 3 |

Output `3` — every suffix of `aaa` is smaller, decided by that final character.
