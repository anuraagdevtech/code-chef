---
topic: Strings
subtopic: Palindrome check by reversal
time: $O(d)$ per test case, $d$ = number of digits
space: $O(d)$
---
A number is a palindrome when it reads the same forwards and backwards. In Python the cleanest test converts to a string and compares against its reverse:

```python
s == s[::-1]
```

The slice `[::-1]` walks the string with step $-1$, producing the reversal, and the comparison is a single pass. For $N \leq 20000$ that is at most five characters.

The alternative avoids strings by reversing arithmetically — peel digits with `n % 10` and rebuild with `rev = rev * 10 + digit` — then compare `rev == n`. It is the version to use in a language without cheap string conversion, and it is the same routine as the Reverse The Number problem. Note the crucial difference between the two problems though: there, reversing `2300` had to yield `32` with leading zeros dropped; here, `n` has no leading zeros to begin with, so the two approaches agree.

A common misstep is to compare only half the string, or to use a two-pointer loop with an off-by-one in the midpoint. The slice sidesteps both; a middle character in an odd-length number compares against itself and is always equal, so no special case is needed.

Output is lowercase `wins` for a palindrome and `loses` otherwise — note that the winning case is the palindrome, which is easy to invert when skimming.

## Edge cases

- **A single digit** ($N \leq 9$): trivially a palindrome, so `wins`.
- **Even length** ($N = 1221$): a palindrome with no middle digit, so the check must not assume an odd length.
- **A trailing zero** ($N = 100$): reversing gives `001`, which differs from `100`, so `loses`. Comparing the *strings* is what makes this right — the reversal has to preserve length.
- **Largest input** ($N = 20000$): five digits, `02002` reversed, so `loses`.
- Reversing the digit string is simpler and safer than rebuilding the number arithmetically, and at $N \leq 20000$ there is no performance reason to prefer the latter.

## Dry run

| $N$ | digits reversed | equal? | output |
|---:|---|:---:|---|
| 331 | `133` | no | `loses` |
| 666 | `666` | yes | `wins` |
| 343 | `343` | yes | `wins` |
