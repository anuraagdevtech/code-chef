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
