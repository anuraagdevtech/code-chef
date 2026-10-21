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

## Edge cases

- **Two troops always suffice.** The alphabet has only two letters, so all the `a`s form one palindromic subsequence and all the `b`s another — meaning the answer is never more than $2$, whatever the string.
- **One troop suffices exactly when $H$ is a palindrome**, since a single troop deletes one palindromic subsequence and must take the whole string.
- **Zero is impossible**, because $|H| \geq 1$ is guaranteed — an empty castle is already ruined and never appears as input.
- **The deleted part is a *subsequence*, not a substring**, so the characters need not be adjacent — which is what makes "all the `a`s" a legal single move.
- **A single character** is a palindrome, so $|H| = 1$ answers $1$.
- **Subtask 1 guarantees every $H$ is a palindrome**, so it tests only the easy branch; the reversal check handles both subtasks identically.
- **$|H|$ up to $10^5$**: the reversal and comparison happen on bytes at C speed.

## Dry run

| $H$ | reversed | palindrome? | output |
|---|---|:---:|---:|
| `abbabaab` | `baababba` | no | `2` |
| `aba` | `aba` | yes | `1` |

For the first row, one troop takes `aaaa` (positions $1, 4, 7, 8$) and a second takes the remaining `bbbb`.
