---
topic: Bit Manipulation
subtopic: Parity bitmask over a 26-letter alphabet
time: $O(N)$ per test case
space: $O(1)$
---
Only the **parity** of each letter's count matters, not the count itself, so the whole string compresses to 26 bits. Keep a mask and toggle one bit per character:

$$\text{mask} \;\mathrel{\oplus}= 1 \ll (c - \texttt{'a'})$$

A pair of identical letters toggles the same bit twice and cancels, so after the sweep a bit is set exactly for the letters appearing an odd number of times. That gives both answers at once: `mask == 0` means every letter is even, so print $-1$; otherwise the lowest set bit names the letter, extracted as `(mask & -mask).bit_length() - 1`.

This beats a frequency table on space ($O(1)$ instead of $O(26)$) and needs only one pass, which matters with $T$ up to $10^5$ and $\sum N$ up to $10^6$.

The common shortcut — XOR the raw character codes and print that character — is wrong in general: it only works when exactly one letter has odd count, and silently prints a garbage letter otherwise. The per-letter bitmask has no such blind spot, and it also makes the choice well defined if several letters were odd.

Note the parity argument implies $|S|$ odd $\iff$ some letter is odd, so the $-1$ case is exactly the even-length strings whose letters all pair up. The samples show all three shapes: `abcbacc` has `c` three times, `abcba` has `c` once, and `abccba` is fully paired, giving $-1$.

## Edge cases

- **A XOR-accumulated bitmask tracks parity per letter**, since seeing a letter twice toggles its bit back off — so a single pass leaves exactly the odd-occurring letters set.
- **No odd letter at all** → the mask is zero and the answer is $-1$, which the sample's `abccba` shows.
- **The lowest set bit is extracted with `mask & -mask`**, which isolates it in one operation and gives the alphabetically earliest odd letter.
- **Several letters may be odd**, in which case this reports the first — the statement speaks of "the" odd character, so the input is expected to have one, but the extraction is deterministic either way.
- **A length-one string** has that single letter odd.
- **Only lowercase letters appear**, so a $26$-bit mask suffices and the offset is from `a`.
- **Sum of $N \leq 10^6$** with $T$ up to $10^5$, so the per-case work is one pass and two bit operations — no $26$-slot array is allocated per case.

## Dry run

| string | letter counts | mask bits set | answer |
|---|---|---|---|
| `abcbacc` | a:2, b:2, c:3 | just `c` | `c` |
| `abcba` | a:2, b:2, c:1 | just `c` | `c` |
| `abccba` | a:2, b:2, c:2 | none | `-1` |
