---
topic: Arrays
subtopic: Odd counts and palindrome feasibility
time: $O(N)$ per test case
space: $O(1)$
---
A multiset of characters can be arranged into a palindrome exactly when **at most one** character has an odd count — that one sits in the middle, and the rest pair off symmetrically.

So let $k$ be the number of indices with $A_i$ odd. If $k \leq 1$, nothing needs doing.

Otherwise, consider what one operation achieves. Converting every occurrence of character $i$ into character $j$ adds $A_i$ to $A_j$ and zeroes $A_i$. Picking two characters that **both** have odd counts is the productive move: the emptied one is no longer odd, and the receiver's count becomes odd + odd = even. One operation removes **two** odd counts at a stroke.

Repeating until at most one remains costs

$$\left\lfloor \frac{k}{2} \right\rfloor$$

operations. The floor handles both parities: an even $k$ collapses to $0$ odd counts, and an odd $k$ collapses to exactly $1$ — which is still a valid palindrome.

The bound is tight because no operation can reduce the odd count by more than two: it touches only two characters.

Sample case 2 has $A = [4, 3, 1]$ with $k = 2$. Merging the count-$1$ character into the count-$3$ one gives $[4, 4, 0]$, so $k = 0$ and one operation suffices. Sample case 1 has a single even count and needs none.

Note the requirement to use **every** character, which is what makes the count parities the whole story — discarding characters would make this trivial instead.

Only the parities matter, so the $A_i$ themselves never need summing; with $\sum N = 2\times10^5$ the single pass is comfortable.

## Edge cases

- **One operation removes two odd counts at once.** Converting every occurrence of character $i$ into character $j$ adds the two counts, and odd $+$ odd $=$ even — so a single merge fixes both.
- **A palindrome tolerates one odd count**, the middle character, which is why the target is "at most one" and the answer is $\lfloor \text{odds}/2 \rfloor$ rather than requiring zero.
- **The parity of the odd count is fixed** by the total number of characters, so an odd `odds` can never be driven to zero — and need not be, since one is allowed. The floor division handles both cases with the same expression.
- **No odd counts** (the first row, a single character with count $4$) → $0$ operations.
- **The operation converts *all* occurrences**, not one, which is what makes each merge worth exactly two odd counts; a per-character edit would be a different problem.
- **$A_i \geq 1$**, so every listed character is actually present, and sum of $N \leq 2 \cdot 10^5$.

## Dry run

Second sample: counts $4, 3, 1$.

| character | count | parity |
|---:|---:|---|
| 1 | 4 | even |
| 2 | 3 | **odd** |
| 3 | 1 | **odd** |

Two odd counts, so one merge: convert all of character $3$ into character $2$, giving counts $4, 4, 0$. Output `1` — the string can now be arranged as a palindrome.
