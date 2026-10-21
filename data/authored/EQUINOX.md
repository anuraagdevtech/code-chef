---
topic: Strings
subtopic: First-character membership test
time: $O(N)$ per test case
space: $O(1)$
---
For each string, only its **first character** matters: if it is one of the letters of `EQUINOX`, Sarthak scores $A$, otherwise Anuradha scores $B$. Tally both and compare.

The letter set is $\{$`E`, `Q`, `U`, `I`, `N`, `O`, `X`$\}$ — the *distinct* letters of the word, which conveniently has no repeats. Holding it as a `set` makes each test $O(1)$.

The trap is treating this as a scoring race by *count* rather than by points. $A$ and $B$ differ, so the side with more strings need not lead. Sample case 2 shows it: Sarthak wins one string and Anuradha one, but at $5$ against $7$ points Anuradha takes it.

Sample case 1 is the draw, and worth tracing: `ABBBCDDE` starts with `A`, which is **not** in `EQUINOX` despite the string containing `E` later. Only the first character counts. So Anuradha scores $3$ once, while Sarthak scores $1$ three times from `EARTH`, `INDIA` and `UUUFFFDDD` — level at $3$ apiece.

That last string is a good check too: `U` is in the set, so the rest of the string is irrelevant.

All strings are uppercase by guarantee, so no case folding is needed. With $A, B$ up to $10^9$ and $N$ up to $100$, totals reach $10^{11}$ — past 32 bits, so a C solution would need a 64-bit accumulator.

## Edge cases

- **Only the first character is consulted.** `UUUFFFDDD` scores for Sarthak on its leading `U` even though most of it is not an equinox letter, and `ABBBCDDE` scores for Anuradha despite containing `C`, `D` and `E`.
- **A draw is possible and must be printed as `DRAW`** — the first case ties at $3$ each, and does so with *unequal* per-word values ($A = 1$ against $B = 3$), so the tie is in the totals, not in the word counts.
- **More words does not mean winning.** The second case gives each player one word, and the larger $B = 7$ beats $A = 5$.
- **`EQUINOX` has seven distinct letters** including `X`, which the second case's `XOXOXOXO` relies on — a set built from the literal word covers them all without hand-listing.
- **$A, B \leq 10^9$ with $N \leq 100$** puts the totals up to $10^{11}$, past 32-bit but native in Python.
- Bytes are compared throughout, so the first character is an integer code and the lookup set is built from the byte string.

## Dry run

First sample: $A = 1$, $B = 3$.

| word | first char | in `EQUINOX`? | Sarthak | Anuradha |
|---|---|:---:|---:|---:|
| `ABBBCDDE` | `A` | no | 0 | 3 |
| `EARTH` | `E` | yes | 1 | 3 |
| `INDIA` | `I` | yes | 2 | 3 |
| `UUUFFFDDD` | `U` | yes | **3** | **3** |

Equal totals, so `DRAW`.
