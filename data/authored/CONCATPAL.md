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
