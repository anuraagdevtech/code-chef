---
topic: Strings
subtopic: Several predicates, one with a positional restriction
time: $O(|S|)$ per test case
space: $O(1)$
---
Five conditions must all hold, and the one that makes this more than a checklist is **where** each character is allowed to count.

- **Lowercase** — anywhere in the string.
- **Uppercase**, **digit**, **special** — each must appear *strictly inside*, meaning the first and last characters do not count.
- **Length** at least $10$.

So the interior is the slice `s[1:-1]`, and three of the four character tests run against that slice while the lowercase test runs against the whole string. Taking the interior once and reusing it keeps the four tests symmetrical and avoids repeating the index arithmetic.

Sample case 1, `#cookOff#P1`, is built precisely on this distinction. It is long enough, has lowercase letters, has an uppercase `O` inside and a special `#` inside — but its only digit is the final `1`, which sits on the boundary and therefore does not count. The answer is `NO`.

Sample case 3, `gR3@tPWD`, satisfies every character rule inside but is only $8$ characters long, failing the length check alone.

Sample case 2 passes all five.

The length check should come first in practice: for a string shorter than $3$ the interior slice is empty, and while that merely makes the other tests false rather than erroring, checking the cheap condition first is the clearer order.

The special set is exactly $\{$ `@`, `#`, `%`, `&`, `?` $\}$ — five characters, no more.

## Edge cases

- **The lowercase rule applies to the whole string; the other three apply strictly inside.** That asymmetry is in the statement, and the code mirrors it — `islower` is tested over `s` while the rest are tested over `s[1:-1]`.
- **The interior exclusion is what fails the first row.** `#cookOff#P1` has a digit, but it is the final character, so it does not count and the answer is `NO`.
- **The length bar is $10$**, and the third row (`gR3@tPWD`, eight characters) fails on that alone despite satisfying every other rule.
- **The length check must come first**, or `s[1:-1]` on a very short string would be tested — harmlessly here, but the ordering keeps the logic honest.
- **The special set is exactly `@#%&?`**, so a character like `!` or `$` does not qualify even though it looks special; it also cannot appear, since the constraints limit the alphabet.
- **Sum of lengths up to $10^6$**: each predicate short-circuits, and the slice is taken once rather than per rule.

## Dry run

| password | length | lower (whole) | upper (inside) | digit (inside) | special (inside) | output |
|---|---:|:---:|:---:|:---:|:---:|---|
| `#cookOff#P1` | 11 | yes | `O`, `P` | **none** (the `1` is last) | `#` | `NO` |
| `U@code4CHEFINA` | 14 | yes | `C`,`H`,… | `4` | `@` | `YES` |
| `gR3@tPWD` | 8 | — | — | — | — | `NO` (too short) |

The first row's interior is `cookOff#P`, which has no digit at all.
