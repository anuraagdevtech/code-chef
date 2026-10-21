---
topic: Constructive
subtopic: Fixing the digit sum, then the last digit
time: $O(N)$ per test case
space: $O(N)$
---
Three requirements, and each pins down one feature of the number.

**Divisible by $3$ but not $9$.** By the digit-sum rules, a number is divisible by $3$ when its digit sum is, and by $9$ when the digit sum is. So the digit sum must be a multiple of $3$ that is **not** a multiple of $9$ — the smallest useful choice being $6$.

**Odd.** The last digit must be odd.

**No leading zero.** The first digit must be non-zero.

All three are satisfied by putting the weight at the two ends and padding the middle with zeros:

$$1\underbrace{00\cdots0}_{N-2}5$$

The digit sum is $1 + 5 = 6$ — divisible by $3$, not by $9$ — the last digit $5$ is odd, and the leading $1$ is non-zero.

$N = 1$ needs its own answer, since the pattern requires two digits. A single digit that is odd and has digit sum $6$ is impossible, so take $3$ instead: divisible by $3$, not by $9$, and odd.

The construction reproduces both multi-digit samples ($15$ and $105$ against the published $15$ and $123$, the latter differing but equally valid), so this is judged by a checker.

Note that padding with zeros rather than, say, repeating digits keeps the digit sum fixed at $6$ regardless of $N$ — which matters because $N$ reaches $10^4$ and a growing digit sum would eventually hit a multiple of $9$.

## Edge cases

- **Digit sum $6$ satisfies both halves of the divisibility requirement at once**: divisible by $3$ and not by $9$. A digit sum of $3$ would also work, and $9$ would not.
- **$N = 1$ needs its own answer**, because `1` followed by `5` is already two digits. The single digit `3` works: sum $3$, odd, no leading zero.
- **$N = 2$** gives `15` with no zeros in between, which the general form produces since `"0" * 0` is empty.
- **The last digit must be odd** — `5` here — so a trailing `0` or `6` would fail even with the right digit sum.
- **No leading zero**, which the leading `1` guarantees; `0...06` has the right digit sum and is invalid.
- **This answer differs from the sample's** at $N = 3$ (`105` against `123`), and both are valid: the statement allows any such $X$, so a special judge checks the three properties.
- **Sum of $N$ up to $10^5$**, so each number is built once by string repetition rather than digit by digit.

## Dry run

| $N$ | output | digits | digit sum | $\div 3$ | $\div 9$ | odd | leading zero |
|---:|---|---|---:|:---:|:---:|:---:|:---:|
| 1 | `3` | $3$ | 3 | yes | no | yes | no |
| 2 | `15` | $1, 5$ | 6 | yes | no | yes | no |
| 3 | `105` | $1, 0, 5$ | 6 | yes | no | yes | no |
| 6 | `100005` | $1,0,0,0,0,5$ | 6 | yes | no | yes | no |

The interior zeros never affect the digit sum, so the pattern scales to any $N$.
