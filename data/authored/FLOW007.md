---
topic: Strings
subtopic: Digit reversal and leading zeros
time: $O(d)$ per test case, $d$ = number of digits
space: $O(d)$
---
Reversing the digits of $N$ has a one-line form in Python: turn the number into a string, slice it backwards with `[::-1]`, and convert back with `int`.

The conversion back to `int` is doing real work, not just restoring the type. Reversing `2300` as text gives the string `"0032"`, and the expected answer is `32` — the leading zeros must disappear. Calling `int` strips them automatically, which is exactly why the round trip through `int` is the right move rather than printing the reversed string directly. Sample case 4 exists specifically to catch this.

The arithmetic alternative avoids strings altogether:

```
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
```

peeling the last digit with `n % 10` and pushing it onto `rev`. This also drops leading zeros for free, because a leading zero in the reversed number is simply never added to a non-zero `rev`. It is the version to reach for in a language without cheap string conversion; in Python the slice is faster to write and no slower in practice.

Both run in time proportional to the digit count, which is $O(\log_{10} N)$ — at most $7$ digits here.
