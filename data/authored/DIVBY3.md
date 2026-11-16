---
topic: Basic Math
subtopic: Ones on even positions modulo three; the answer is always 0, 1, 2, 3 or -1
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Powers of two alternate between $1$ and $-1$ modulo 3, so the number is divisible by 3 exactly when the ones on even positions and the ones on odd positions are equally many modulo 3. With $E$ ones on even indices out of `ones` in total this reads $E \equiv 2 \cdot \text{ones} \pmod 3$.

A swap of two equal neighbours does nothing; a swap of `01` or `10` moves one `1` to the other parity, changing $E$ by exactly $\pm 1$. So we need to shift $E$ by $+1$ or $-1$ (the other one would also be reachable as two steps the opposite way).

- Already satisfied: 0.
- $E$ can only take values between $\max(0, \text{ones} - \lfloor n/2 \rfloor)$ and $\min(\text{ones}, \lceil n/2 \rceil)$; if no value in that range has the right residue: $-1$.
- Some unequal adjacent pair moves $E$ in the needed direction: 1.
- Otherwise every available swap moves $E$ the wrong way; two of them on disjoint positions shift it by two, which is the same residue: 2.
- If the unequal pairs are too close together to be used independently, a third swap is needed: 3.

## Edge cases

- All zeros: the value is 0, already divisible.
- All ones of a length that is not balanced, such as `111`: no swap changes anything, answer $-1$.
- The range check is essential - a residue may be unreachable because there are not enough even or odd slots.
- Leading zeros are allowed, so the string is just a multiset of positions.

## Dry run

`S = 11001`: three ones, target residue $2 \cdot 3 \bmod 3 = 0$. Even indices 0, 2, 4 hold `1 0 1`, so $E = 2$.

$E$ may range from $\max(0, 3 - 2) = 1$ to $\min(3, 3) = 3$, and 3 has the right residue.

The pair at indices 1-2 is `10`; swapping it moves that one from an odd to an even index, $E = 3$. One swap: `10101` = 21.
