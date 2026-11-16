---
topic: Dynamic Programming
subtopic: Minimum prefix partition using rolling palindrome detection
time: $O(|S|^2)$ per test case
space: $O(|S|)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $best[r]$ be the minimum number of palindrome parts for the first $r$ characters, with $best[0]=0$. For each palindrome ending at the current right endpoint and starting at $l$, try `best[l]+1`.

Detect palindromes using one rolling array: equal endpoints form a palindrome if the length is at most two or the interior substring was a palindrome at the previous right endpoint. Scan left endpoints in ascending order to preserve that previous interior value until it is used. Every partition is considered by its final part.

## Edge cases

- A whole-string palindrome needs one part.
- A string with no longer palindrome may need one part per character.
- All characters are uppercase, but the recurrence does not depend on case.

## Dry run

For `ABCCBDA`, final parts can be `A | BCCB | D | A`, using four palindromes. The prefix DP finds no partition with fewer parts.
