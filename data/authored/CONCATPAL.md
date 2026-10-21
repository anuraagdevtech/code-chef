---
topic: Strings
subtopic: Multiset containment forced by mirroring
time: $O(N + M)$ per test case
space: $O(1)$ — 26 counters
---
Both halves may be permuted freely, but a character cannot move **between** them: the first $N$ positions hold exactly the letters of $A$ and the last $M$ hold those of $B$.

Suppose $N \leq M$. In a palindrome of length $N + M$, position $i$ mirrors to position $N + M + 1 - i$. For every $i \leq N$ that mirror index is at least $M + 1 > N$, so **every position of $A$ mirrors into $B$**. Each letter of $A$ therefore needs a matching partner inside $B$, which means

$$\text{multiset}(A) \subseteq \text{multiset}(B)$$

What is left of $B$ after removing one copy of each letter of $A$ sits in the centre of the palindrome and mirrors onto itself — so that remainder must itself be rearrangeable into a palindrome, i.e. have **at most one odd count**.

Those two conditions together are exactly right, and symmetric: if $M < N$ simply swap the roles.

The subset test is the part that is easy to miss, and sample case 2 shows why it matters — `abc` and `xyz` have the same length and a combined multiset with six odd counts, but even a shared-count check would not capture that *none* of $A$'s letters can find a partner.

Sample case 4 is the second condition biting: $A = $ `a` fits inside $B = $ `aax`, but the remainder `ax` has two odd counts and cannot be a palindromic centre.

Sample case 3 passes both: `aa` sits inside `aaaa`, leaving `aa`, which is already a palindrome.

Counting with two 26-element arrays keeps this linear, which matters at $\sum (N+M) = 2\times10^5$.

## Edge cases

- **Every position of the shorter string mirrors into the longer one.** If $|A| \leq |B|$, then position $i \leq |A|$ maps to position $|A| + |B| + 1 - i \geq |B| + 1 > |A|$ — so each character of $A$ needs a partner in $B$, making multiset containment necessary.
- **The leftover of the longer string forms the centre** and must itself be a palindrome, so at most one of its character counts may be odd. The first row leaves `b` and two `d`s, which is fine.
- **Which string is shorter must be determined first**, hence the swap; assuming $A$ is the shorter one fails whenever $N > M$, as in the first sample row.
- **Containment can fail outright** (the second row, `abc` against `xyz`) with no shared letter at all.
- **Equal lengths** make the leftover empty, so the test reduces to the two multisets being identical.
- **Identical letters on both sides** (the third row, `aa` and `aaaa`) leave two `a`s in the middle, an even count, so it works.
- **One extra character of the wrong kind** breaks it: the fourth row leaves `a` and `x`, two odd counts.

## Dry run

First sample: $A = $ `abcdd` ($N = 5$), $B = $ `ac` ($M = 2$). Since $N > M$ the roles swap, so the shorter side is `ac`.

| letter | shorter side | longer side | contained? |
|---|---:|---:|:---:|
| a | 1 | 1 | yes |
| c | 1 | 1 | yes |

Leftover of the longer side: `b` $\times 1$, `d` $\times 2$ — one odd count, which the centre can absorb. Output `YES`, e.g. `ca` $+$ `dbdac`… or more simply `ac` $+$ `dbdca` reads as `acdbdca`.
