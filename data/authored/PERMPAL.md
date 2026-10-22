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

## Edge cases

- **At most one letter may have an odd count**, the usual palindrome condition — and that one takes the middle position. Two or more odd counts is `-1` (the third sample, `abc`).
- **The output is the permutation of *indices*, not the palindrome itself**, with $t_i = s_{P_i}$ — so the answer records where each output character comes from.
- **Each pair of equal letters fills the two outermost free slots**, which keeps the string a palindrome as the pointers close inward.
- **The odd leftover is held back and placed last**, at whatever slot the two pointers meet — which is the exact centre once all pairs are seated.
- **The pointers meet correctly for both parities**: an even length exhausts them in pairs, and an odd length leaves exactly one slot for the middle letter.
- **A single-character string** has one odd count and is trivially a palindrome.
- **The letters are grouped by a dictionary over the raw bytes**, so no 26-slot table or sorting is needed.
- **This permutation differs from the sample's** on `baa` (`2 1 3` matches, but longer inputs will diverge), and any permutation producing a palindrome is accepted.

## Dry run

The string `abab`, with `a` at positions $1, 3$ and `b` at positions $2, 4$ (1-based).

| step | slot pair filled | source indices | perm so far |
|---|---|---|---|
| pair of `a` | slots 1 and 4 | 1 and 3 | $1, \_, \_, 3$ |
| pair of `b` | slots 2 and 3 | 2 and 4 | $1, 2, 4, 3$ |

Applying it: $t = s_1 s_2 s_4 s_3 = $ `abba`, a palindrome.
