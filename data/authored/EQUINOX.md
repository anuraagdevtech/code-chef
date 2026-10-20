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
