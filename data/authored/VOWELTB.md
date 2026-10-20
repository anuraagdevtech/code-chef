---
topic: Strings
subtopic: Membership test against a small set
time: $O(1)$
space: $O(1)$
---
A single uppercase letter is given; print `Vowel` if it is one of `A`, `E`, `I`, `O`, `U` and `Consonant` otherwise.

The direct expression is `c in "AEIOU"`, or `c in {"A","E","I","O","U"}` with a set. For five elements the difference is immaterial — the substring scan is if anything faster at this size — but the set version is the one that stays $O(1)$ as the collection grows, and it states "membership" rather than "is a substring of". For single characters the two agree; for multi-character needles they would not, which is worth keeping in mind before reusing the idiom.

Either way this beats a five-way `or` chain, which is longer and easy to mistype.

The constraints promise an uppercase English letter, so there is no need to normalise case or reject digits and punctuation. If that guarantee were absent, `c.upper() in "AEIOU"` would be the defensive form.

There is **no $T$** here — the input is a single character on one line, one test case. The expected output is `Vowel` or `Consonant`, capitalised exactly as shown, with the sample's `Z` producing `Consonant`.
