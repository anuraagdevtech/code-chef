---
topic: Constructive
subtopic: Divisibility chain, realised by the array itself
time: $O(N \log A)$ per test case
space: $O(N)$
---
Prefix GCDs only ever shrink, and they shrink by division: $B_{i} = \gcd(B_{i-1}, A_i)$, so

$$B_i \mid B_{i-1}$$

is necessary. If that chain ever breaks — as in the sample's $B = [1, 3]$, where $3 \nmid 1$ — no array exists and the answer is $-1$.

When the chain holds, the construction is as short as it gets: take $A = B$. The divisibility chain means $B_i$ divides every earlier $B_j$, so

$$\gcd(B_1, B_2, \ldots, B_i) = B_i$$

and the prefix GCDs of $A$ reproduce $B$ exactly. The range condition is free as well, since $B_i \leq 10^9$ is given.

It is worth seeing why nothing cleverer is needed. One might try to make $A_i$ a multiple of $B_i$ that avoids extra common factors — the sample's `4 26` does this, with $26 = 2 \cdot 13$ — but the earlier prefix already caps the GCD at $B_{i-1}$, so any extra factors in $A_i$ beyond $B_i$ are harmless *and* unnecessary. Echoing $B$ is both valid and simplest.

Note the chain condition is only about consecutive terms: $B_i \mid B_{i-1}$ for every $i$ implies $B_i \mid B_j$ for all $j < i$ by transitivity, so one pass suffices.

Our output for the first sample is `4 2` where the sample prints `4 26`; both have prefix GCDs $4, 2$, and the problem accepts any valid array.

## Edge cases

- **Prefix GCDs form a divisibility chain.** $B_i = \gcd(B_{i-1}, A_i)$, so $B_i$ always divides $B_{i-1}$ — making that the one necessary condition, and the second row fails it ($1$ is not divisible by $3$).
- **The condition is also sufficient, and $B$ realises itself.** Taking $A = B$ gives $\gcd(B_1, \dots, B_i) = B_i$, because every earlier $B_j$ is a multiple of $B_i$ — so no construction is needed beyond echoing the input.
- **$B_i \leq 10^9$ is given**, so echoing $B$ automatically respects the bound on $A_i$.
- **The chain must be checked in the right direction**: $B_{i-1} \bmod B_i$, not the reverse. The reverse test would accept the second row.
- **$N = 1$** has no constraint at all, and $A = B$ works trivially.
- **A constant $B$** is a valid chain (every value divides itself), as is any strictly decreasing chain of divisors.
- **This answer differs from the sample's** (`4 2` against `4 26`), and both produce the same $B$; the statement asks for any such $A$, so a special judge recomputes the prefix GCDs.

## Dry run

First sample: $B = 4, 2$.

| check | value |
|---|---|
| $4 \bmod 2$ | $0$ ✓ |

So output $A = 4, 2$ and verify:

| $i$ | $\gcd(A_1 \dots A_i)$ | required $B_i$ |
|---:|---:|---:|
| 1 | $\gcd(4) = 4$ | 4 ✓ |
| 2 | $\gcd(4, 2) = 2$ | 2 ✓ |
