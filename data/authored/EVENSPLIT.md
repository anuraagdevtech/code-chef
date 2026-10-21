---
topic: Strings
subtopic: Which orderings are reachable
time: $O(N)$ per test case
space: $O(N)$
---
The operation never changes **which** characters the string contains, only their order — so the count of `0`s and `1`s is invariant. The lexicographically smallest arrangement of a fixed multiset of bits is all the `0`s followed by all the `1`s, so the sorted string is the obvious target.

For $N \geq 3$ that target is reachable. The move is flexible enough to shuffle freely: choosing a subsequence of length $2k$ sends its first half to the front and its second half to the back, and repeating lets any character be driven to either end. For instance $\texttt{110} \to \texttt{101} \to \texttt{011}$ reaches the sorted form in two moves, and $\texttt{100} \to \texttt{010} \to \texttt{001}$ does the same.

**The exception is $N = 2$.** There the only non-empty even-length subsequence is the whole string, with $k = 1$: the first character moves to the front and the second to the end, leaving nothing in the middle. That is the identity, so a two-character string cannot be changed at all. Sample case 1 is precisely this — `10` stays `10`, even though `01` is smaller.

$N = 1$ is likewise frozen, having no even-length subsequence at all, but there the string is already sorted so it makes no difference.

So the rule is: output $S$ unchanged when $N \leq 2$, and the sorted string otherwise.

Sorting a binary string is just counting — emit $c_0$ zeros then $c_1$ ones — which is $O(N)$ and avoids a comparison sort entirely. With the sum of $N$ at $2 \times 10^5$ and $T$ up to $10^5$, that and bulk I/O are what keep this comfortable.

## Edge cases

- **$N = 2$ is a genuine exception, not an optimisation.** The only non-empty even-length subsequence is the whole string, and with $k = 1$ the move sends the first character to the front and the second to the end — the identity. So `10` stays `10` and must *not* become `01`. The first sample row exists to catch exactly this.
- **$N = 1$**: no even-length subsequence exists at all, so no move is possible and the string is returned unchanged.
- **$N \geq 3$ is fully sortable.** For `110`, one move gives `101` and a second gives `011`, and the same two-step pattern generalises — which is why every string of length $3$ or more can be fully sorted.
- **An already-sorted string** (the third row, all ones) comes back unchanged, and the count-and-rebuild path produces it correctly without detecting the case.
- **All characters identical**: every move is a no-op, as the statement's third explanation notes.
- **Sum of $N \leq 2 \cdot 10^5$**: counting the zeros and concatenating two runs is $O(N)$, cheaper than sorting the characters.

## Dry run

| $N$ | $S$ | zeros | $N \leq 2$? | output |
|---:|---|---:|:---:|---|
| 2 | `10` | 1 | **yes** | `10` (unchanged) |
| 4 | `1001` | 2 | no | `0011` |
| 5 | `11111` | 0 | no | `11111` |
| 7 | `0010100` | 5 | no | `0000011` |

Row 1 would be `01` under the general rule, which is why the length is checked first.
