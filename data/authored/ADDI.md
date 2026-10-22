---
topic: Bit Manipulation
subtopic: Zero bits inside the binary width
time: $O(1)$ per test case
space: $O(1)$
---
"Unset bits" means the zeros in $N$'s binary representation **as written**, i.e. within its own width — leading zeros do not count, otherwise every answer would depend on an arbitrary word size.

The width is $\mathrm{bitlen}(N) = \lfloor \log_2 N \rfloor + 1$, and the number of ones is the population count, so

$$\text{answer} = \mathrm{bitlen}(N) - \mathrm{popcount}(N)$$

Python gives both directly: `n.bit_length()` and `n.bit_count()`.

For $N = 10 = 1010_2$ the width is $4$ and two bits are set, giving $2$. For $N = 1 = 1_2$ the width is $1$ with one bit set, giving $0$ — the smallest case, and the one that shows why counting against a fixed 64-bit word would be wrong (it would report $63$).

Since $N \leq 10^{18} < 2^{60}$, the answer never exceeds $59$. In C++ this is `63 - __builtin_clzll(n) + 1 - __builtin_popcountll(n)`; Python's arbitrary-precision integers make the width query exact without any clz juggling.

The statement's input description is garbled — it says the second line holds a single $N$ — but the actual format is $T$ followed by $T$ lines, each with one $N$, as the sample shows.

## Edge cases

- **Only the zeros *inside* $N$'s own binary width count**, so the measure is against `bit_length` rather than a fixed $64$ — otherwise every small number would report dozens of unset bits.
- **A number of all ones gives $0$**, since its width equals its popcount — the sample's $N = 1$.
- **$N \geq 1$ is guaranteed**, so `bit_length` is at least $1$ and never zero.
- **$N$ up to $10^{18}$** needs $60$ bits, which Python's arbitrary-precision integers handle natively — a 32-bit popcount table would not.
- **The answer is at most $59$**, reached by a value like $2^{59}$ whose single set bit sits at the top.
- **`bit_count` is the exact popcount**, so no loop over bits is needed.
- **The input is two lines**, the count then the values, read as one token stream.

## Dry run

| $N$ | binary | width | set bits | unset inside the width |
|---:|---|---:|---:|---:|
| 10 | $1010$ | 4 | 2 | `2` |
| 1 | $1$ | 1 | 1 | `0` |
| 8 | $1000$ | 4 | 1 | 3 |
