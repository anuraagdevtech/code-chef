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
