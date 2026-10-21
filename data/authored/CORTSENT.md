---
topic: Strings
subtopic: Per-word alphabet membership
time: $O(\sum |S_i|)$ per test case
space: $O(1)$
---
Two alphabets: the first is lowercase `a`–`m`, the second is uppercase `N`–`Z`. A sentence is valid when **each word** draws entirely from one of them — different words may use different alphabets, but no word may mix.

So for every word, check that all its characters lie in the first range, or that all lie in the second.

Two traps, and the samples target both.

**Mixing within a word is the forbidden thing**, not mixing within a sentence. Sample case 2, `ab NO`, uses both alphabets and is valid, because each individual word is pure. A solution demanding one alphabet per sentence would reject it.

**The ranges are restricted, not just by case.** Lowercase stops at `m` and uppercase starts at `N` — so a lowercase `z` and an uppercase `A` both belong to *neither* alphabet. Sample case 3, `A N D`, fails on exactly this: `N` is fine, but `A` and `D` are uppercase letters below `N` and belong to no language at all. Checking merely `islower()` or `isupper()` would wrongly accept it.

Sample case 1, `aN`, is the within-word mix.

Comparing characters against the range bounds directly is cheap; with the summed length bounded by $10^5$ and $T$ up to $10^5$, bulk input reading matters more than the check itself. Note the word count $K$ and the words all share **one line**, which the flat token read handles naturally.

## Edge cases

- **The two alphabets are disjoint and incomplete**: lowercase `a`–`m` and uppercase `N`–`Z`. A letter outside both — `A` or `z`, say — belongs to neither language, which is what fails the third sample row on its lone `A`.
- **A word must sit entirely in one language.** `aN` mixes them and fails, even though each character is individually valid in some language.
- **Different words may use different languages**, as the second row does (`ab` then `NO`), so the test is per word rather than per sentence.
- **One bad word condemns the sentence**, and the loop breaks on the first failure.
- **A single-character word is still checked**, which is how the third row fails.
- **Bytes are compared as integer codes** against the four range bounds, avoiding a decode over up to $10^5$ characters.

## Dry run

| sentence | word | all in `a`–`m`? | all in `N`–`Z`? | verdict |
|---|---|:---:|:---:|---|
| `aN` | `aN` | no (`N`) | no (`a`) | `NO` |
| `ab NO` | `ab` | yes | — | continue |
| | `NO` | no | yes | `YES` |
| `A N D` | `A` | no | no (`A` < `N`) | `NO` |
