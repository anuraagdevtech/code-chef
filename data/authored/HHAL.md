---
topic: Strings
subtopic: Covering a two-letter string with palindromes
time: $O(|H|)$ per test case
space: $O(1)$
---
The alphabet has only two letters, and that makes the answer one of three values.

- **Empty string** → $0$ troops.
- **Already a palindrome** → $1$: delete the whole thing in one go, since a string is a subsequence of itself.
- **Anything else** → $2$.

The upper bound of $2$ is the key observation. A subsequence consisting of *all* the `a`s is a run of identical characters, which is trivially a palindrome; deleting it leaves only `b`s, which is likewise a palindrome. So two troops always suffice, no matter how tangled the string is.

And a non-palindrome clearly cannot be cleared in one, since the single deleted subsequence would have to be the entire string.

That makes the whole problem a palindrome check, `h == h[::-1]`, in $O(|H|)$ with no search at all. The elaborate framing about choosing palindromic subsequences is a distraction — the structure of the string beyond "is it a palindrome" never matters.

The sample, `abbabaab`, reverses to `baababba` and so is not a palindrome, giving $2$. One valid pair of troops is the subsequence `ababa` followed by the remaining `bab` — but the simpler all-`a`s-then-all-`b`s split works equally well.

Note the constraint $|H| \geq 1$, so the empty case never actually arises in the input; it is worth stating only because it completes the reasoning.
