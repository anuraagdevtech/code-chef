---
topic: Strings
subtopic: Divisibility decided by one digit
time: $O(D)$ per test case
space: $O(1)$
---
A number is divisible by $5$ exactly when its **last digit** is $0$ or $5$. Since the digits may be rearranged freely, the question becomes simply: does $N$ contain a $0$ or a $5$ anywhere?

If it does, move that digit to the end and the result is a multiple of $5$. If it does not, no arrangement can end in $0$ or $5$, so the answer is `No`.

So the whole solution is `"0" in s or "5" in s` — a scan of the digit string, with no arithmetic at all. That matters here: $D$ reaches $1000$, so $N$ can be up to $10^{1000}$, far beyond any fixed-width integer. Python could parse it as a big integer, but there is no need — treating the input as **text** is both simpler and faster, and is the right instinct whenever a problem's bounds are given as a digit count rather than a value.

One subtlety deserves a mention: a valid number should not have leading zeros. If the chosen digit to move is a $0$, something non-zero must remain to lead. That is always possible, because the input is guaranteed to have no leading zeros and $N \geq 1$, so at least one non-zero digit exists — and moving a single $0$ to the back leaves it available to lead. The example $108 \to 180$ is exactly this.

Sample case 2 ($103$) relies on the $0$; case 1 ($115$) on the $5$; case 3 ($119$) has neither and fails.

The $D$ given on its own line is redundant for Python, since the string carries its own length, but the token must still be consumed.

## Edge cases

- **Any digit $0$ or $5$ suffices**, because it can be moved to the last position and the rest arranged freely.
- **Leading zeros are not a problem**, which is worth checking. $N = 50$ has digits $\{5, 0\}$: putting the $5$ last would give `05`, but putting the $0$ last gives `50`, so a valid arrangement always exists. Since $N \geq 1$ has no leading zeros, at least one nonzero digit is available to lead.
- **A single digit** ($N = 5$): already a multiple of $5$.
- **Neither digit present** ($119$): no rearrangement can end in $0$ or $5$, so `No`.
- **$N$ can have up to $1000$ digits**, so it must be handled as text; and the length line $D$ has to be consumed even though Python never needs it.

## Dry run

| $N$ | digits | contains $0$ or $5$? | a working arrangement | output |
|---:|---|:---:|---|---|
| 115 | $1,1,5$ | yes ($5$) | $115$ | `Yes` |
| 103 | $1,0,3$ | yes ($0$) | $130$ | `Yes` |
| 119 | $1,1,9$ | no | — | `No` |
