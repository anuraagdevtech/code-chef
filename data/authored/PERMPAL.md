---
topic: Strings
subtopic: Pairing equal letters inward from both ends
time: $O(n)$ per test case
space: $O(n)$
---
A multiset of letters can be arranged into a palindrome exactly when **at most one letter has an odd count** — every other letter must split evenly between the two halves. That is the feasibility test; otherwise print $-1$.

The construction then emits *indices* rather than letters, since $P$ answers "which original position supplies position $i$". Group the positions of each letter, then walk two pointers inward: for each pair of positions holding the same letter, send one to the left pointer and its partner to the right pointer. The lone odd position, if any, lands in the exact middle, which is the only slot a palindrome leaves unpaired.

$$t[i] = s[P_i] \implies t[i] = t[n+1-i]$$

holds by construction, because the two slots filled in each step hold the same letter.

Note the problem's convention: $P$ indexes *into* $s$, so $P$ is a permutation of $1 \ldots n$ and the output is those source indices in target order. It is easy to accidentally produce the inverse permutation, which is a different (and generally wrong) answer.

Many permutations work. For `abab` our pairing gives `1 2 4 3`, which happens to match the sample and yields `abba`. For `baa` the single `b` is the odd letter and goes to the middle, giving `2 1 3` and the palindrome `aba`. And `abc` has three odd counts, so $-1$.

The empty-middle case matters too: for even $n$ with all counts even, the two pointers meet exactly, and no middle slot is written.
